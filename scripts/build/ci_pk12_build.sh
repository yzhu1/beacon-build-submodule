#!/bin/bash

set -e

hostclass=$1
app=$2
gitrepo=$3
webapp_service=$4
env=$5

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

# run webdriver tests on remote box
remote_webdriver_workspace=/home/autobuild/devel/3_12/$app-$app-$env-ci
scp -i /home/tomcat/.ssh/autobuild_key target/webdriverbundle.zip autobuild@yad124.tt.wgenhq.net:$remote_webdriver_workspace/webdriverbundle.zip
ssh -i /home/tomcat/.ssh/autobuild_key autobuild@yad124.tt.wgenhq.net "echo '#!/bin/bash' > webdriver.sh && \
echo 'set -e' >> webdriver.sh && \
echo 'export RUN_ONLY_SMOKE=true' >> webdriver.sh && \
echo 'export ENV_PROPERTY_PREFIX=$1' >> webdriver.sh && \
echo 'Xvfb :5 -screen 0 1024x768x24 >/dev/null 2>&1 &' >> webdriver.sh && \
echo 'export DISPLAY=:5.0' >> webdriver.sh && \
echo 'cd $2' >> webdriver.sh && \
echo 'rm -rf tmp' >> webdriver.sh && \
echo 'mkdir tmp' >> webdriver.sh && \
echo 'hostname' >> webdriver.sh && \
echo 'pwd' >> webdriver.sh && \
echo 'unzip webdriverbundle.zip -d tmp' >> webdriver.sh && \
echo 'cd tmp' >> webdriver.sh && \
echo 'ant test-webdriver-precompiled' >> webdriver.sh && \
chmod +x webdriver.sh && \
./webdriver.sh $ENV_PROPERTY_PREFIX $remote_webdriver_workspace"

# build migration rpms to QA repo and move code rpm to the same
cp $BUILD_RPM_REPO/mclass-tt-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $NEXT_RPM_REPO -r $WORKSPACE/RPM_STAGING -Dcheckoutroot=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-migrations-$app.spec

# update QA rpm repo
/opt/wgen/rpmtools/wg_createrepo $NEXT_RPM_REPO

## if build is successful, move the last-stable branch to the current commit
## (this should always be the last step in the build)
git branch -f last-stable-$BUILD_BRANCH
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$BUILD_BRANCH
