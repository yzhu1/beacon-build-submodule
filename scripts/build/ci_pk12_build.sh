#!/bin/bash

set -ex

webapphostclass=$1
app=$2
gitrepo=$3
webapp_service=$4
env=$5
apphomeenvvar=$6
webdrivertestsperbatch=$7
migrationsappname=$8
autoreleasebox=$9
releaseversion=${10}
wgrenv=${11}

# build rpms
rm -rf $WORKSPACE/RPM_STAGING
mkdir -p $WORKSPACE/opt/tt/webapps/$app
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -D${app}dir=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-$app.spec
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -Dcheckoutroot=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-migrations-$app.spec

# promote them to CI rpm repo
/opt/wgen/rpmtools/wg_createrepo $BUILD_RPM_REPO

# deploy and start the webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $wgrenv -f -s -g \"$webapphostclass\" -a \"release_start.sh ${webapphostclass}_stop.sh ${webapphostclass}_rm_rpm.sh ${webapphostclass}_bcfg.sh ${webapphostclass}_start.sh\"

# run webdriver tests in parallel on testdog
echo "RUNNING WEBDRIVER TESTS"
find target/test/webdriver -name *Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py -s yad128.tt.wgenhq.net -u autobuild -i /home/jenkins/.ssh/autobuild_key -w /home/autobuild/$JOB_NAME -v $apphomeenvvar -n $webdrivertestsperbatch -p $ENV_PROPERTY_PREFIX

# all tests have passed!  rpms may be promoted to QA
cp $BUILD_RPM_REPO/mclass-tt-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
cp $BUILD_RPM_REPO/tt-migrations-$migrationsappname-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
/opt/wgen/rpmtools/wg_createrepo $NEXT_RPM_REPO

## build is successful!  move the last-stable branch to the current commit
## (this should always be the last step in the build)
git branch -f last-stable-$BUILD_BRANCH
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$BUILD_BRANCH
