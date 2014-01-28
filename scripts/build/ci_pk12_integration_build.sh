#!/bin/bash

# This is the master build script for PK12 oib and outcomes ci builds.
# Our builds should not have to do anything other than set environment
# variables (as required by this script) and run this script!

# -e: Exit  immediately  if a simple command (see SHELL GRAMMAR above) exits with a non-zero status
# -u: Treat unset variables as an error when performing parameter expansion
# -x: After  expanding each simple command, for command, case command, select command, or arithmetic for command,
#     display the expanded value of PS4 (NOTE: this seems like pointless boilerplate to me)
set -eux

ANT="/opt/wgen-3p/ant-1.8.1/bin/ant"

if [ -e "/opt/wgen-3p/python26/bin/python" ]
 then
  PYTHON="/opt/wgen-3p/python26/bin/python"
 else
  PYTHONi="/usr/bin/python2.6"
fi

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
runwgspringcoreintegrationtests=$RUN_WGSPRINGCORE_INTEGRATION_TESTS # e.g., true

# Optional parameters
othermigrationsappname=${OTHER_MIGRATIONS_APP_NAME:-""}  # e.g., a hack so that we can pretend outcomes and teacher portal are separate
extrawgrargs=${EXTRA_WGR_ARGS:-""}                       # e.g., --refspec 'refs/changes/97/5197/1'
allow_tests_bypass=${ALLOW_TESTS_BYPASS:-true}
runonlynonslow=${RUN_ONLY_NON_SLOW:-true}

# Set automatically by Jenkins
buildtag=$BUILD_TAG-$BUILD_BRANCH
buildnumber=$BUILD_NUMBER
workspace=$WORKSPACE

# Set more environment variables
export ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit"

gitrepobaseurl="git@github.wgenhq.net:Beacon"

# Set the migration testdog if testdogs have been set
if [ -n "${TESTDOGS+x}" ]
then
    migrationstestdog=$(echo $TESTDOGS | cut -f1 -d ',') # Take the first testdog
    export ENV_PROPERTY_PREFIX=$migrationstestdog # To test the up/down migrations on one testdog
else
    # Set the webapp home environment variable (needed to run integration, webservice, and webdriver tests)
    export $apphomeenvvar=. 
fi

# Clean workspace
rm -rf target

# ivy-resolve first so we can get wgspringcoreversion accurately
$ANT ivy-resolve

ivy_changes=$(grep -r --regexp="downloaded=\"true\"" --include="*.xml" $WORKSPACE/.ivy2/cache/resolution | wc -l)

# Tag this build in git.
git tag -a -f -m "Jenkins Build #$buildnumber" $buildtag
git push -f $gitrepobaseurl/$gitrepo +refs/tags/$buildtag:$buildtag

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

# Compile, run static and unit tests
$ANT clean test-clean deploy checkstyle template-lint jslint test-unit build-javadoc

integration_changes=$(echo $(git diff origin-$gitrepo/$buildbranch origin-$gitrepo/last-stable-integration-$buildbranch --name-only | grep -c -v --regexp="^src/test/webdriver\|^src/main/webapp/static"))

if [ $allow_tests_bypass = 'false' ] || [ $integration_changes -gt 0 ] || [ $ivy_changes -gt 0 ]; then

    # build javadoc, migrate one db up and down
    $ANT clear-schema load-baseline-database migrate-schema rollback-schema
    if [ $runonlynonslow = 'false' ]; then
        runslowtestsflag='-f'
    else
        runslowtestsflag=
    fi
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
        | $PYTHON conf/base/scripts/build/parallelTests.py \
              -s $TESTDOGS -v $apphomeenvvar $runslowtestsflag -n $testsperbatch \
              -d -t update-schema
    fi
else
    echo "NO CHANGES FOUND OUTSIDE OF WEBDRIVER TESTS AND STATIC FILES.  SKIPPING INTEGRATION TESTS."
fi

# Remove existing RPMs in the repo to ensure the one we build gets deployed
rm -f $buildrpmrepo/mclass-tt-$app-$rpmversion-*.noarch.rpm
rm -f $buildrpmrepo/tt-migrations-$migrationsappname-$rpmversion-*.noarch.rpm

# Build webapp and db rpms

rm -rf $workspace/RPM_STAGING
mkdir -p $workspace/opt/tt/webapps/$app
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $buildrpmrepo -r $workspace/RPM_STAGING \
        -D${app}dir=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-$app.spec
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $buildrpmrepo -r $workspace/RPM_STAGING \
        -Dcheckoutroot=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-migrations-$app.spec

if [ "$othermigrationsappname" != "" ]
then
    # Remove and rebuild the other migration RPM
    # Fairly specific to Outcomes - so we can pretend Teacher Portal is separate when it's really not
    rm -f $buildrpmrepo/tt-migrations-$othermigrationsappname-$rpmversion-*.noarch.rpm
    python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $buildrpmrepo -r $workspace/RPM_STAGING \
        -Dcheckoutroot=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-migrations-$othermigrationsappname.spec
fi

# Promote them to CI rpm repo
/opt/wgen/rpmtools/wg_createrepo $buildrpmrepo

# Add the last-stable-integration tag to the current commit
git branch -f last-stable-integration-$buildbranch
git push -f $gitrepobaseurl/$gitrepo.git last-stable-integration-$buildbranch

