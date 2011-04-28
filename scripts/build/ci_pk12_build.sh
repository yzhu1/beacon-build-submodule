#!/bin/bash

set -e

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

# update rpm repo
/opt/wgen/rpmtools/wg_createrepo $BUILD_RPM_REPO

# deploy the rpm should update configs and install rpms.
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV $hostclass install mclass-tt-$app
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV $hostclass bcfgcliupdate

# start the webapp
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV $hostclass service $webapp_service start

# run webdriver tests in parallel on slave
find target/test/webdriver -name *Test.class \
  | xargs -i basename {} .class \
  | python conf/base/scripts/build/parallelTests.py -s yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net -u autobuild -i /home/tomcat/.ssh/autobuild_key -w /home/autobuild/$JOB_NAME -v $apphomeenvvar -n $webdrivertestsperbatch -p $ENV_PROPERTY_PREFIX

# build migration rpms to QA repo and move code rpm to the same
cp $BUILD_RPM_REPO/mclass-tt-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $NEXT_RPM_REPO -r $WORKSPACE/RPM_STAGING -Dcheckoutroot=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-migrations-$app.spec

# update QA rpm repo
/opt/wgen/rpmtools/wg_createrepo $NEXT_RPM_REPO

## if build is successful, move the last-stable branch to the current commit
## (this should always be the last step in the build)
git branch -f last-stable-$BUILD_BRANCH
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$BUILD_BRANCH
