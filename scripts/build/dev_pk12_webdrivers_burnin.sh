#!/bin/bash

# This script runs a web driver test N times, and reports how many times it
# succeed or failed. This is useful to determine the stability of the test.
# This script is modeled on ci_pk12_build_with_testdogs.sh.
# This is a modification of the single test burn-in, the exception is to run all tests
# -e: Exit  immediately  if a simple command (see SHELL GRAMMAR above) exits with a non-zero status
# -u: Treat unset variables as an error when performing parameter expansion
# -x: output commands
set -eux

ANT="/opt/wgen-3p/ant-1.8.1/bin/ant"

# import libraries
SCRIPT_DIR=${BASH_SOURCE%/*}
source "$SCRIPT_DIR/ci_build_utils.sh" # defines functions in ci_build_utils pseudopackage

# meta-configuration utility:
ci_build_utils.setup_build_env

apphomeenvvar=$APP_HOME_ENV_VAR         # e.g., OUTCOMES_HOME or THREETWELVE_HOME
webapphostclass=$WEBAPP_HOSTCLASS       # e.g., mhcttwebapp
app=$APP                                # e.g., itembank or outcomes
gitrepo=$GIT_REPO                       # e.g., itembank-web or outcomes
env=$ENV                                # e.g., futureci or currentci
migrationsappname=$MIGRATIONS_APP_NAME  # e.g., oib or outcomes
autoreleasebox=$AUTORELEASE_BOX         # e.g., tmc142.mc.wgenhq.net (consult cmdb)
rpmversion=$RPM_VERSION                 # e.g., 13.0.0
releaseversion=$RELEASE_VERSION         # e.g., mc13.0.0
buildbranch=$BUILD_BRANCH               # e.g., master
buildrpmrepo=$BUILD_RPM_REPO            # e.g., $REPO_FUTURE_CI (CAN BE MULTIPLE REPOS)

# Optional parameters
runonlysmoke=${RUN_ONLY_SMOKE:-false}
extrawgrargs=${EXTRA_WGR_ARGS:-""}                       # e.g., --refspec 'refs/changes/97/5197/1'
releasestepstoskip=${RELEASE_STEPS_TO_SKIP:-""}          # e.g., mhcttoutcomeswebapp_rebuild_tile_cache.sh mhcttoutcomeswebapp_dbmigration.sh

# Set automatically by Jenkins
buildtag=$BUILD_TAG-$BUILD_BRANCH
buildnumber=$BUILD_NUMBER
workspace=$WORKSPACE

# Set more environment variables
export ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit"

# import libraries
SCRIPT_DIR=${BASH_SOURCE%/*}
source "$SCRIPT_DIR/ci_build_utils.sh" # defines functions in ci_build_utils pseudopackage

# Set the webapp home environment variable (needed to run integration, webservice, and webdriver tests)
export $apphomeenvvar=.

# Clean workspace
rm -rf target

# ivy-resolve first so we can get correct dependencies
$ANT ivy-resolve

# Tag this build in git.
git tag -a -f -m "Jenkins Build #$buildnumber" $buildtag
git push -f git@github.wgenhq.net:Beacon/$gitrepo +refs/tags/$buildtag:$buildtag

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
$ANT clean test-clean deploy test-compile

wgspringcoreintegrationtestpath=conf            # path to nowhere, if runwgspringcoreintegrationtests is false

ci_build_utils.publish_rpms $app $migrationsappname $rpmversion $buildnumber $workspace $buildrpmrepo

# Deploy webapp, update bcfg, start webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\" -A \"$releasestepstoskip\" $extrawgrargs

if [ $runonlysmoke = 'false' ]; then
    runslowtestsflag='-l'
else
    runslowtestsflag=
fi

# Prepare for running webdrivers locally
Xvfb :5 -screen 0 1024x768x24 >/dev/null 2>&1 & export DISPLAY=:5.0

# run tests
passedtests=0
i=0
while [ $i -lt $ITERATIONS ]; do
    testpassed=0
    $ANT prepare-db-for-parallel-tests
    set +e # allow tests to fail
    $ANT test-webdriver-precompiled
    if [ $? -eq 0 ]; then
        testpassed=1
    fi
    set -e
    passedtests=$(($passedtests+$testpassed))
    i=$(($i+1))
done

echo "Ran $ITERATIONS times with $passedtests successes";

if [ $passedtests -ne $ITERATIONS ]; then # not all tests passed. fail the build.
    exit 1;
fi

