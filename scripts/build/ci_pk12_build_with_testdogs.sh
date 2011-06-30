#!/bin/bash

# This is the master build script for PK12 oib and outcomes ci builds.
# Our builds should not have to do anything other than set environment
# variables (as required by this script) and run this script!

set -eux

apphomeenvvar=$APP_HOME_ENV_VAR         # e.g., OUTCOMES_HOME or THREETWELVE_HOME
testsperbatch=$TESTS_PER_BATCH          # e.g., 8, to farm 8 tests to each testdog at a time
webapphostclass=$WEBAPP_HOSTCLASS       # e.g., mhcttwebapp
dbhostclass=$DB_HOSTCLASS               # e.g., mhcttdbitembank
app=$APP                                # e.g., itembank or outcomes
gitrepo=$GIT_REPO                       # e.g., itembank-web or outcomes
env=$ENV                                # e.g., futureci or currentci
migrationsappname=$MIGRATIONS_APP_NAME  # e.g., itembank or outcomes
autoreleasebox=$AUTORELEASE_BOX         # e.g., tmc142.mc.wgenhq.net (consult cmdb)
releaseversion=$RELEASE_VERSION         # e.g., mc13.0.0

# Set more environment variables
export ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit"
export RUN_ONLY_SMOKE=true
export ENV_PROPERTY_PREFIX=testdog${env}0 # Set to testdog0 that we can test up/down migrations on one testdog

# Clean workspace
rm -rf target

# ivy-resolve first so we can get WGSPRINGCORE_VERSION accurately
/opt/wgen-3p/ant-1.7.0/bin/ant ivy-resolve

# Tag this build in git.
git tag -a -f -m "Jenkins Build #$BUILD_NUMBER" $BUILD_TAG
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo +refs/tags/$BUILD_TAG:$BUILD_TAG

# Set properties that'll get templated into basic.ftl
export GIT_REVISION=`git log -1 --pretty=format:%H`
export WGSPRINGCORE_VERSION=`python conf/base/scripts/build/getWgspringcoreVersion.py`
echo "git.common.revision=$WGSPRINGCORE_VERSION" >> conf/build.properties
echo "git.revision=$GIT_REVISION" >> conf/build.properties
echo "build.number=$BUILD_NUMBER" >> conf/build.properties
echo "build.branch=$BUILD_BRANCH" >> conf/build.properties
echo "rpm.version=$RPM_VERSION" >> conf/build.properties

# Stop the webapps before messing with their dbs
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$AUTORELEASE_BOX /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\" -a \"release_start.sh ${webapphostclass}_stop.sh\"

# Compile, run static and unit tests, migrate one db up and down
/opt/wgen-3p/ant-1.7.0/bin/ant clean-deploy checkstyle template-lint jslint test-compile test-unit clear-schema load-baseline-database migrate-schema rollback-schema

# Run db updates on all the testdog dbs and then run all integration and webservice tests
echo "RUNNING INTEGRATION AND WEBSERVICE TESTS IN PARALLEL"
(   find ivy_lib/compile -name *wgspringcore*integration*jar -exec jar -tf \{} \; \
 && find target/test/integration target/test/webservice \
) | grep Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py \
    -s testdog${env}0,testdog${env}1,testdog${env}2,testdog${env}3 \
    -v $apphomeenvvar -n $testsperbatch -d

# Build webapp and db rpms
rm -rf $WORKSPACE/RPM_STAGING
mkdir -p $WORKSPACE/opt/tt/webapps/$app
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -D${app}dir=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-$app.spec
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -Dcheckoutroot=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-migrations-$app.spec

# Promote them to CI rpm repo
/opt/wgen/rpmtools/wg_createrepo $BUILD_RPM_REPO

# Deploy webapp, update bcfg, start webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\"

# Run webdriver tests in parallel on testdogs, first loading fixture data (-d)
echo "RUNNING WEBDRIVER TESTS"
if [ $RUN_ONLY_SMOKE = 'false' ]; then
    runslowtestsflag='-l'
else
    runslowtestsflag=
fi
find target/test/webdriver -name *Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py \
    -s testdog${env}0,testdog${env}1,testdog${env}2,testdog${env}3 \
    -v $apphomeenvvar -n $testsperbatch -d $runslowtestsflag

# All tests have passed!  The build is good!  Promote RPMs to QA RPM repo
cp $BUILD_RPM_REPO/mclass-tt-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
cp $BUILD_RPM_REPO/tt-migrations-$migrationsappname-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
/opt/wgen/rpmtools/wg_createrepo $NEXT_RPM_REPO

# Move the last-stable tag to the current commit
git branch -f last-stable-$BUILD_BRANCH
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$BUILD_BRANCH
