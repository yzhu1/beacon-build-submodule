#!/bin/bash

# This is the master build script for PK12 oib and outcomes ci builds.
# Our builds should not have to do anything other than set environment
# variables (as required by this script) and run this script!

# -e: Exit  immediately  if a simple command (see SHELL GRAMMAR above) exits with a non-zero status
# -u: Treat unset variables as an error when performing parameter expansion
# -x: After  expanding each simple command, for command, case command, select command, or arithmetic for command,
#     display the expanded value of PS4 (NOTE: this seems like pointless boilerplate to me)
set -eux

ANT="/opt/wgen-3p/ant-1.7.0/bin/ant"

apphomeenvvar=$APP_HOME_ENV_VAR         # e.g., OUTCOMES_HOME or THREETWELVE_HOME
testsperbatch=$TESTS_PER_BATCH          # e.g., 8, to farm 8 tests to each testdog at a time
webapphostclass=$WEBAPP_HOSTCLASS       # e.g., mhcttwebapp
dbhostclass=$DB_HOSTCLASS               # e.g., mhcttdbitembank
app=$APP                                # e.g., itembank or outcomes
gitrepo=$GIT_REPO                       # e.g., itembank-web or outcomes
env=$ENV                                # e.g., futureci or currentci
migrationsappname=$MIGRATIONS_APP_NAME  # e.g., oib or outcomes
autoreleasebox=$AUTORELEASE_BOX         # e.g., tmc142.mc.wgenhq.net (consult cmdb)
rpmversion=$RPM_VERSION                 # e.g., 13.0.0
releaseversion=$RELEASE_VERSION         # e.g., mc13.0.0
buildbranch=$BUILD_BRANCH               # e.g., master
buildrpmrepo=$BUILD_RPM_REPO            # e.g., $REPO_FUTURE_CI
nextrpmrepo=$NEXT_RPM_REPO              # e.g., $REPO_FUTURE_QA
runonlysmoke=$RUN_ONLY_SMOKE            # e.g., true
isnightlybuild=$IS_NIGHTLY_BUILD        # e.g., true
runwgspringcoreintegrationtests=$RUN_WGSPRINGCORE_INTEGRATION_TESTS # e.g., true

# Optional parameters
if [ -n "${EXTRA_WGR_ARGS+x}" ]       # e.g., --refspec 'refs/changes/17/2817/1'
then
        extrawgrargs=$EXTRA_WGR_ARGS
else
        extrawgrargs=""
fi

# Set automatically by Jenkins
buildtag=$BUILD_TAG-$BUILD_BRANCH
buildnumber=$BUILD_NUMBER
workspace=$WORKSPACE

# Set more environment variables
export ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=384m -XX:-UseGCOverheadLimit"

# Set the migration testdog if testdogs have been set
if [ -n "${TESTDOGS+x}" ]
then
	migrationstestdog=$(echo $TESTDOGS | cut -f1 -d ',') # Take the first testdog
	export ENV_PROPERTY_PREFIX=$migrationstestdog # To test the up/down migrations on one testdog
	webdrivertestdogs=${TESTDOGS} #default to the same testdogs used for integration tests
else
	# Set the webapp home environment variable (needed to run integration, webservice, and webdriver tests)
	export $apphomeenvvar=.	
fi

# Set the testdogs used to run webdriver tests
if [ -n "${WEBDRIVER_TESTDOGS+x}" ]
then
    webdrivertestdogs=${WEBDRIVER_TESTDOGS}
fi

# Clean workspace
rm -rf target

# ivy-resolve first so we can get wgspringcoreversion accurately
/opt/wgen-3p/ant-1.7.0/bin/ant ivy-resolve

# Tag this build in git.
git tag -a -f -m "Jenkins Build #$buildnumber" $buildtag
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo +refs/tags/$buildtag:$buildtag

# Set properties that'll get templated into basic.ftl
gitrevision=`git log -1 --pretty=format:%H`
wgspringcoreversion=`python conf/base/scripts/build/getWgspringcoreVersion.py`
echo "git.common.revision=$wgspringcoreversion" >> conf/build.properties
echo "git.revision=$gitrevision" >> conf/build.properties
echo "build.number=$buildnumber" >> conf/build.properties
echo "build.branch=$buildbranch" >> conf/build.properties
echo "rpm.version=$rpmversion" >> conf/build.properties

# Stop the webapps before messing with their dbs
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\" -a \"release_start.sh ${webapphostclass}_stop.sh\" ${extrawgrargs}

# Compile, run static and unit tests, migrate one db up and down
$ANT clean test-clean deploy checkstyle template-lint jslint test-unit \
    clear-schema load-baseline-database migrate-schema rollback-schema

if [ $isnightlybuild != 'true' ]; then

    if [ $runwgspringcoreintegrationtests == 'true' ]; then
        wgspringcoreintegrationtestpath=ivy_lib/compile # correct path
    else
        wgspringcoreintegrationtestpath=conf            # path to nowhere, if runwgspringcoreintegrationtests is false
    fi

    if [ ! -n "${TESTDOGS+x}" ]
    then 
        # no TESTDOGS: run tests through ant normally
        $ANT migrate-schema
        $ANT test-integration test-webservice
    else
        $ANT test-compile
        # Run db updates on all the testdog dbs and then run all integration and webservice tests
        echo "RUNNING INTEGRATION AND WEBSERVICE TESTS IN PARALLEL"
        (   find $wgspringcoreintegrationtestpath -name *wgspringcore*integration*jar -exec jar -tf \{} \; \
         && find target/test/integration target/test/webservice \
	)   | grep Test.class \
	    | xargs -I CLASSFILE basename CLASSFILE .class \
	    | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py \
              -s $TESTDOGS \
              -v $apphomeenvvar -n $testsperbatch -d
    fi
    # Build webapp and db rpms
    rm -rf $workspace/RPM_STAGING
    mkdir -p $workspace/opt/tt/webapps/$app
    python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $buildrpmrepo -r $workspace/RPM_STAGING \
            -D${app}dir=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-$app.spec
    python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $buildrpmrepo -r $workspace/RPM_STAGING \
            -Dcheckoutroot=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-migrations-$app.spec

    # Promote them to CI rpm repo
    /opt/wgen/rpmtools/wg_createrepo $buildrpmrepo

else

    # Migrate schema back up so webapp may start
    $ANT clear-schema migrate-schema

fi

# Deploy webapp, update bcfg, start webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\" -A \"mhcttwebapp_rebuild_search_indexes.sh mhcttwebapp_rebuild_tile_cache.sh\" ${extrawgrargs}

# Run webdriver tests in parallel on testdogs, first loading fixture data (-d)
echo "RUNNING WEBDRIVER TESTS"
if [ $runonlysmoke = 'false' ]; then
    runslowtestsflag='-l'
else
    runslowtestsflag=
fi

if [ ! -n "${webdrivertestdogs+x}" ]
then
    # If no testdogs are configured, run the ant test-webdriver-precompiled locally
    Xvfb :5 -screen 0 1024x768x24 >/dev/null 2>&1 & export DISPLAY=:5.0
    $ANT test-webdriver-precompiled
else
    # Run the webdriver tests in parallel
    echo "--IN PARALLEL--"
    find target/test/webdriver -name *Test.class \
  | xargs -I CLASSFILE basename CLASSFILE .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py \
    -s $webdrivertestdogs \
    -v $apphomeenvvar -n $testsperbatch -d $runslowtestsflag
fi

if [ $isnightlybuild != 'true' ]; then

    # All tests have passed!  The build is good!  Promote RPMs to QA RPM repo
    cp $buildrpmrepo/mclass-tt-$app-$rpmversion-$buildnumber.noarch.rpm $nextrpmrepo
    cp $buildrpmrepo/tt-migrations-$migrationsappname-$rpmversion-$buildnumber.noarch.rpm $nextrpmrepo
    # call the create repo job downstream to avoid repo locking issues

    # Move the last-stable tag to the current commit
    git branch -f last-stable-$buildbranch
    git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$buildbranch

fi
