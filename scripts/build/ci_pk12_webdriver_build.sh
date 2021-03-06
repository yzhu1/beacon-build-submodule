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
  PYTHON="/usr/bin/python2.6"
fi

# import libraries
SCRIPT_DIR=${BASH_SOURCE%/*}
source "$SCRIPT_DIR/ci_build_utils.sh" # defines functions in ci_build_utils pseudopackage

# meta-configuration utility:
ci_build_utils.setup_build_env

apphomeenvvar=$APP_HOME_ENV_VAR         # e.g., OUTCOMES_HOME or THREETWELVE_HOME
testsperbatch=$TESTS_PER_BATCH          # e.g., 8, to farm 8 tests to each testdog at a time
webapphostclass=$WEBAPP_HOSTCLASS       # e.g., mhcttwebapp
app=$APP                                # e.g., itembank or outcomes
gitrepo=$GIT_REPO                       # e.g., itembank-web or outcomes
env=$ENV                                # e.g., futureci or currentci
migrationsappname=$MIGRATIONS_APP_NAME  # e.g., oib or outcomes
autoreleasebox=$AUTORELEASE_BOX         # e.g., tmc142.mc.wgenhq.net (consult cmdb)
rpmversion=$RPM_VERSION                 # e.g., 13.0.0
releaseversion=$RELEASE_VERSION         # e.g., mc13.0.0
buildbranch=$BUILD_BRANCH               # e.g., master
buildrpmrepo=$BUILD_RPM_REPO            # e.g., $REPO_FUTURE_CI
secondary_build_rpm_repo=${SECOND_RPM_REPO:-""} # e.g. $REPO_DEV_EL6
nextrpmrepo=${NEXT_RPM_REPO:-""}        # e.g., $REPO_FUTURE_QA
secondary_next_rpm_repo=${SECOND_NEXT_RPM_REPO:-""} # e.g. EL6 FQA

# Optional parameters
runonlysmoke=${RUN_ONLY_SMOKE:-true}
isnightlybuild=${IS_NIGHTLY_BUILD:-false}
extrawgrargs=${EXTRA_WGR_ARGS:-""}                       # e.g., --refspec 'refs/changes/97/5197/1'
releasestepstoskip=${RELEASE_STEPS_TO_SKIP:-""}          # e.g., mhcttoutcomeswebapp_rebuild_tile_cache.sh mhcttoutcomeswebapp_dbmigration.sh
webdrivertestdogs=${WEBDRIVER_TESTDOGS:-${TESTDOGS:-""}} # the testdogs used to run webdriver tests
allow_targeted_tests=${ALLOW_TARGETED_TESTS:-false}
skipbcfg=${SKIP_BCFG:-false}

# Set automatically by Jenkins
buildtag=$BUILD_TAG-$BUILD_BRANCH
buildnumber=$BUILD_NUMBER
workspace=$WORKSPACE

# Set more environment variables
export ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit"

# default to Github, but allow overrides
gitrepobaseurl=${GIT_REPO_BASE_URL:-"git@github.com:amplifylitco"} # e.g., "git@github.wgen.net:Beacon" for GitHub

# RPM-management variables
app_rpm_stem=mclass-tt-$app-$rpmversion
migration_rpm_stem=tt-migrations-$migrationsappname-$rpmversion

# check for story-build issues
bad_rpms=`find $buildrpmrepo $secondary_build_rpm_repo -noleaf -maxdepth 1 -name "$migration_rpm_stem-1?????.noarch.rpm" -o -name "$app_rpm_stem-1?????.noarch.rpm"`
if [ -n "$bad_rpms" ]
then
    echo "DANGER found story-build RPMs in future-ci repo: $bad_rpms"
    exit 1
fi

if [ "true" == "$skipbcfg" ]
then
    releasestepstoskip="$releasestepstoskip mhctt${app}webapp_bcfg.sh"
fi

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

# Compile
$ANT clean test-clean deploy test-compile

# Deploy webapp, update bcfg, start webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\" -A \"$releasestepstoskip\" $extrawgrargs

# check changes
non_webdriver_changes=$(echo $(git diff origin/$buildbranch origin/last-stable-webdriver-$buildbranch --name-only | grep -c -v --regexp="^src/test/webdriver"))

# Run webdriver tests in parallel on testdogs, first loading fixture data (-d)
echo "RUNNING WEBDRIVER TESTS"
if [ $runonlysmoke = 'false' ]; then
    runslowtestsflag='-l'
else
    runslowtestsflag=
fi

if [ "$webdrivertestdogs" == "" ]
then
    # If no testdogs are configured, run the ant test-webdriver-precompiled locally
    $ANT prepare-db-for-parallel-tests # load fixture data (works in all projects)
    Xvfb :5 -screen 0 1024x768x24 >/dev/null 2>&1 & export DISPLAY=:5.0
    $ANT test-webdriver-precompiled
elif [ $allow_targeted_tests = 'false' ] || [ $non_webdriver_changes -gt 0 ] || [ $ivy_changes -gt 0 ]; then
    # Run the webdriver tests in parallel
    echo "--IN PARALLEL--"
    find target/test/webdriver -name *Test.class \
  | xargs -I CLASSFILE basename CLASSFILE .class \
  | $PYTHON conf/base/scripts/build/parallelTests.py \
    -s $webdrivertestdogs \
    -v $apphomeenvvar -n $testsperbatch $runslowtestsflag \
    -d -t prepare-db-for-parallel-tests
else
    # Run only webdrivers affected by change
    echo "--AFFECTED WEBDRIVERS IN PARALLEL--"
    git diff origin/$buildbranch origin/last-stable-webdriver-$buildbranch --name-only \
    | egrep -o "net/wgen/.*\.java" | sed -e "s:/:.:g" -e "s:\.java$::I" -e"s:^:-m :" \
    | xargs -x java -jar "conf/base/scripts/build/turbo-athena-v1.0.1.jar" -c "target/test/webdriver" -t "target/test/webdriver"  \
    | sed -r -e 's:([a-zA-Z0-9]+\.)+::' \
    | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py \
        -s $TESTDOGS -v $apphomeenvvar $runslowtestsflag -n $testsperbatch \
        -d -t prepare-db-for-parallel-tests
fi

if [ $isnightlybuild != 'true' ] && [ "$nextrpmrepo" != "" ]  && [ "$buildbranch" != "release" ]; then
    # All tests have passed!  The build is good!  Promote RPMs to QA RPM repo

    # Copy the RPMs to the future-qa repo
    cp $buildrpmrepo/$app_rpm_stem-*.noarch.rpm $nextrpmrepo
    cp $buildrpmrepo/$migration_rpm_stem-*.noarch.rpm $nextrpmrepo
    if [ $secondary_next_rpm_repo != "" ]; then
        cp $buildrpmrepo/$app_rpm_stem-*.noarch.rpm $secondary_next_rpm_repo
        cp $buildrpmrepo/$migration_rpm_stem-*.noarch.rpm $secondary_next_rpm_repo
    fi

    # call the create repo job downstream to avoid repo locking issues

    # Add last-stable-webdriver tag to the current commit
    git branch -f last-stable-webdriver-$buildbranch
    git push -f $gitrepobaseurl/$gitrepo.git last-stable-webdriver-$buildbranch

    # Move the last-stable tag to the last-stable-integration tag
    git checkout last-stable-integration-$buildbranch
    git pull
    git branch -f last-stable-$buildbranch
    git push -f $gitrepobaseurl/$gitrepo.git last-stable-$buildbranch

fi
