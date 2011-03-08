#!/bin/bash

app=$1

# remove the code RPM
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV mhcttwebapp remove mclass-tt-$app

# build the RPM
rm -rf $WORKSPACE/RPM_STAGING
mkdir -p $WORKSPACE/opt/tt/webapps/$app
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -D${app}dir=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-$app.spec

# update rpm repo
/opt/wgen/rpmtools/wg_createrepo $BUILD_RPM_REPO

# deploy the rpm should update configs and install rpms.
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV mhcttwebapp install mclass-tt-$app
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV mhcttwebapp bcfgcliupdate

# start the webapp
/opt/wgen/funcdeploy/wg_funcdeploy.py -e $FUNC_ENV mhcttwebapp service tt-web-app start

# run webdriver tests on remote box
echo $JOB_NAME $ENV_PROPERTY_PREFIX $BUILD_TAG $BUILD_BRANCH "true" | ssh -i /home/tomcat/.ssh/autobuild_key autobuild@yad124.tt.wgenhq.net /home/autobuild/devel/3_12/$app-$app-future-ci/ci-webdriver.sh

# build migration rpms to QA repo and move code rpm to the same
cp $BUILD_RPM_REPO/mclass-tt-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $NEXT_RPM_REPO -r $WORKSPACE/RPM_STAGING -Dcheckoutroot=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-migrations-$app.spec

# update QA rpm repo
/opt/wgen/rpmtools/wg_createrepo $NEXT_RPM_REPO

## if build is successful, move the last-stable branch to the current commit
## (this should always be the last step in the build)
git branch -f last-stable-$BUILD_BRANCH
git push -f git@mcgit.mc.wgenhq.net:312/$app.git last-stable-$BUILD_BRANCH
