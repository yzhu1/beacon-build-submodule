#!/bin/bash

set -ex

hostclass=$1
app=$2
gitrepo=$3
webapp_service=$4
env=$5
apphomeenvvar=$6
webdrivertestsperbatch=$7

# remove the code RPM
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV $hostclass remove mclass-tt-$app

# build the RPM
rm -rf $WORKSPACE/RPM_STAGING
mkdir -p $WORKSPACE/opt/tt/webapps/$app
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -D${app}dir=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-$app.spec

# update CI rpm repo
/opt/wgen/rpmtools/wg_createrepo $BUILD_RPM_REPO

# deploy the rpm should update configs and install rpms.
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV $hostclass install mclass-tt-$app
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV $hostclass bcfgcliupdate

# start the webapp
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV $hostclass service $webapp_service start

# run webdriver tests in parallel on testdog
echo "RUNNING WEBDRIVER TESTS"
find target/test/webdriver -name *Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py -s yad128.tt.wgenhq.net -u autobuild -i /home/jenkins/.ssh/autobuild_key -w /home/autobuild/$JOB_NAME -v $apphomeenvvar -n $webdrivertestsperbatch -p $ENV_PROPERTY_PREFIX

# all tests have passed!  rpms may be promoted to QA

# build migration rpms to CI repo
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -Dcheckoutroot=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-migrations-$app.spec

# update CI rpm repo
/opt/wgen/rpmtools/wg_createrepo $BUILD_RPM_REPO

# move both rpms to the QA repo
cp $BUILD_RPM_REPO/mclass-tt-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
cp $BUILD_RPM_REPO/tt-migrations-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO

# update QA rpm repo
/opt/wgen/rpmtools/wg_createrepo $NEXT_RPM_REPO

## build is successful!  move the last-stable branch to the current commit
## (this should always be the last step in the build)
git branch -f last-stable-$BUILD_BRANCH
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$BUILD_BRANCH
