#!/bin/bash

set -eux

export ANT_OPTS=-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit
export RUN_ONLY_SMOKE=true
export ENV_PROPERTY_PREFIX=testdog0

apphomeenvvar=$APP_HOME_ENV_VAR # e.g., OUTCOMES_HOME
testsperbatch=$TESTS_PER_BATCH # e.g., 8, to farm 8 tests to each testdog at a time
webapphostclass=$WEBAPP_HOSTCLASS
app=$APP
gitrepo=$GIT_REPO
webapp_service=$WEBAPP_SERVICE
env=$ENV
migrationsappname=$MIGRATIONS_APP_NAME
autoreleasebox=$AUTORELEASE_BOX
releaseversion=$RELEASE_VERSION
wgrenv=$WGR_ENV

alias ant='/opt/wgen-3p/ant-1.7.0/bin/ant'

ant ivy-resolve

rm -rf target

git tag -a -f -m "Hudson Build #$BUILD_NUMBER" $BUILD_TAG
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo +refs/tags/$BUILD_TAG:$BUILD_TAG

export GIT_REVISION=`git log -1 --pretty=format:%H`
export WGSPRINGCORE_VERSION=`python conf/base/scripts/build/getWgspringcoreVersion.py`

echo "git.common.revision=$WGSPRINGCORE_VERSION" >> conf/build.properties
echo "git.revision=$GIT_REVISION" >> conf/build.properties
echo "build.number=$BUILD_NUMBER" >> conf/build.properties
echo "build.branch=$BUILD_BRANCH" >> conf/build.properties
echo "rpm.version=$RPM_VERSION" >> conf/build.properties

# stop the webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$AUTORELEASE_BOX /opt/wgen/wgr/bin/wgr.py -r $RELEASE_VERSION -e $FUNC_ENV -f -s -g \"mhcttwebapp\" -a \"release_start.sh mhcttwebapp_stop.sh\"

# compile, run unit tests, lint, migrate up and down
ant ci-pk12

# Run db updates on the testdogs and then all integration and webservice tests
echo "RUNNING INTEGRATION AND WEBSERVICE TESTS IN PARALLEL"
(   find ivy_lib/compile -name *wgspringcore*integration*jar -exec jar -tf \{} \; \
 && find target/test/integration target/test/webservice \
) | grep Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py \
    -s testdog0,testdog1,testdog2,testdog3 \
    -v $apphomeenvvar -n $testsperbatch -d

# build rpms
rm -rf $WORKSPACE/RPM_STAGING
mkdir -p $WORKSPACE/opt/tt/webapps/$app
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -D${app}dir=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-$app.spec
python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $BUILD_RPM_REPO -r $WORKSPACE/RPM_STAGING -Dcheckoutroot=$WORKSPACE -Drpm_version=$RPM_VERSION -Dbuildnumber=$BUILD_NUMBER $WORKSPACE/rpm/tt-migrations-$app.spec

# promote them to CI rpm repo
/opt/wgen/rpmtools/wg_createrepo $BUILD_RPM_REPO

# deploy and update bcfg
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $wgrenv -f -s -g \"$webapphostclass\" -a \"release_start.sh ${webapphostclass}_stop.sh ${webapphostclass}_rm_rpm.sh ${webapphostclass}_bcfg.sh\"

# hack to set each testdog to use right db
ssh tomcat@yad107.tt.wgenhq.net "sed -i 's/wgspring\.db\.host.*/wgspring\.db\.host=yad114\.tt\.wgenhq\.net/' /opt/tt/app-config/oib.properties"
ssh tomcat@yad141.tt.wgenhq.net "sed -i 's/wgspring\.db\.host.*/wgspring\.db\.host=yad127\.tt\.wgenhq\.net/' /opt/tt/app-config/oib.properties"
ssh tomcat@yad142.tt.wgenhq.net "sed -i 's/wgspring\.db\.host.*/wgspring\.db\.host=yad128\.tt\.wgenhq\.net/' /opt/tt/app-config/oib.properties"
ssh tomcat@yad143.tt.wgenhq.net "sed -i 's/wgspring\.db\.host.*/wgspring\.db\.host=yad129\.tt\.wgenhq\.net/' /opt/tt/app-config/oib.properties"

# start the webapp
ssh -i /home/jenkins/.ssh/wgrelease wgrelease@$autoreleasebox /opt/wgen/wgr/bin/wgr.py -r $releaseversion -e $wgrenv -f -s -g \"$webapphostclass\" -a \"release_start.sh ${webapphostclass}_start.sh\"

# run webdriver tests in parallel on testdog
echo "RUNNING WEBDRIVER TESTS"
if [ $RUN_ONLY_SMOKE = 'false' ]; then
    runslowtestsflag='-l'
else
    runslowtestsflag=
fi
find target/test/webdriver -name *Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py -s testdog0,testdog1,testdog2,testdog3 -v $apphomeenvvar -n $testsperbatch -d$runslowtestsflag

# all tests have passed!  rpms may be promoted to QA
cp $BUILD_RPM_REPO/mclass-tt-$app-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
cp $BUILD_RPM_REPO/tt-migrations-$migrationsappname-$RPM_VERSION-$BUILD_NUMBER.noarch.rpm $NEXT_RPM_REPO
/opt/wgen/rpmtools/wg_createrepo $NEXT_RPM_REPO

## build is successful!  move the last-stable branch to the current commit
## (this should always be the last step in the build)
git branch -f last-stable-$BUILD_BRANCH
git push -f git@mcgit.mc.wgenhq.net:312/$gitrepo.git last-stable-$BUILD_BRANCH
