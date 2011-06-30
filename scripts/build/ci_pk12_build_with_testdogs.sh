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
rpmversion=$RPM_VERSION                 # e.g., 13.0.0
releaseversion=$RELEASE_VERSION         # e.g., mc13.0.0
buildbranch=$BUILD_BRANCH               # e.g., master
buildrpmrepo=$BUILD_RPM_REPO            # e.g., $REPO_FUTURE_CI
nextrpmrepo=$NEXT_RPM_REPO              # e.g., $REPO_FUTURE_QA
runonlysmoke=$RUN_ONLY_SMOKE            # e.g., true

# Set automatically by Jenkins
buildtag=$BUILD_TAG
buildnumber=$BUILD_NUMBER
workspace=$WORKSPACE

# Set more environment variables
export ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit"
export ENV_PROPERTY_PREFIX=testdog${env}0 # Set to testdog0 that we can test up/down migrations on one testdog

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
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\" -a \"release_start.sh ${webapphostclass}_stop.sh\"

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
rm -rf $workspace/RPM_STAGING
mkdir -p $workspace/opt/tt/webapps/$app
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $buildrpmrepo -r $workspace/RPM_STAGING -D${app}dir=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-$app.spec
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $buildrpmrepo -r $workspace/RPM_STAGING -Dcheckoutroot=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-migrations-$app.spec

# Promote them to CI rpm repo
/opt/wgen/rpmtools/wg_createrepo $buildrpmrepo

# Deploy webapp, update bcfg, start webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $env -f -s -g \"$webapphostclass\" -a \"release_start.sh ${webapphostclass}_rm_rpm.sh ${webapphostclass}_bcfg.sh ${webapphostclass}_start.sh\"

# Run webdriver tests in parallel on testdogs, first loading fixture data (-d)
echo "RUNNING WEBDRIVER TESTS"
if [ $runonlysmoke = 'false' ]; then
    runslowtestsflag='-l'
else
    runslowtestsflag=
fi
find target/test/webdriver -name *Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py \
    -s testdog${env}0 \
    -v $apphomeenvvar -n 1000 -d $runslowtestsflag

# All tests have passed!  The build is good!  Promote RPMs to QA RPM repo
cp $buildrpmrepo/mclass-tt-$app-$rpmversion-$buildnumber.noarch.rpm $nextrpmrepo
cp $buildrpmrepo/tt-migrations-$migrationsappname-$rpmversion-$buildnumber.noarch.rpm $nextrpmrepo
/opt/wgen/rpmtools/wg_createrepo $nextrpmrepo

# Move the last-stable tag to the current commit
git branch -f last-stable-$buildbranch
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$buildbranch
