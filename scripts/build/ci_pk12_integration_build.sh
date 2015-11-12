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
runwgspringcoreintegrationtests=$RUN_WGSPRINGCORE_INTEGRATION_TESTS # e.g., true

# Optional parameters
extrawgrargs=${EXTRA_WGR_ARGS:-""}                       # e.g., --refspec 'refs/changes/97/5197/1'
allow_tests_bypass=${ALLOW_TESTS_BYPASS:-true}
runonlynonslow=${RUN_ONLY_NON_SLOW:-true}
allow_targeted_tests=${ALLOW_TARGETED_TESTS:-false}
publish_jars=${IVY_PUBLISH:-false}

set +x
# If the build branch is 'master', verify that the change is not a merge from the branch 'next'.
if [ "$buildbranch" = "master" ] && [ -f "./next_branch_sentinel" ]; then
    echo "ERROR: It seems that you are trying to merge the 'next' branch into 'master' - This is not allowed! Please revert your merge in the master branch."
    exit -1
fi
# If the build branch is 'next', verify that its file indicator exists.
if [ "$buildbranch" = "next" ] && [ ! -f "./next_branch_sentinel" ]; then
    echo "ERROR: Build failed because the 'next' branch is missing the file: './next_branch_sentinel'. This file is necessary to prevent disallowed merges (next->master)."
    exit -1
fi
set -x

# Set automatically by Jenkins
buildtag=$BUILD_TAG-$BUILD_BRANCH
buildnumber=$BUILD_NUMBER
workspace=$WORKSPACE

# Set more environment variables
export ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit"

# default to Github, but allow overrides
gitrepobaseurl=${GIT_REPO_BASE_URL:-"git@github.com:amplifylitco"} # e.g., "git@github.wgen.net:Beacon" for GitHub

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

# Compile, run static and unit tests
$ANT clean test-clean deploy checkstyle freestyle template-lint jslint test-unit build-javadoc

integration_changes=$(echo $(git diff origin/$buildbranch origin/last-stable-integration-$buildbranch --name-only | grep -c -v --regexp="^src/test/webdriver\|^src/main/webapp/static"))

if [ $allow_tests_bypass = 'false' ] || [ $integration_changes -gt 0 ] || [ $ivy_changes -gt 0 ]; then

    # build javadoc, migrate one db up and down
    $ANT clear-schema load-baseline-database migrate-schema rollback-schema
    if [ $runonlynonslow = 'false' ]; then
        runslowtestsflag='-f'
    else
        runslowtestsflag=
    fi
    if [ $runwgspringcoreintegrationtests == 'true' ]; then
        wgspringcoreintegrationtestpath=ivy_lib/test # correct path
    else
        wgspringcoreintegrationtestpath=conf            # path to nowhere, if runwgspringcoreintegrationtests is false
    fi

    non_java_changes=$(echo $(git diff origin/$buildbranch origin/last-stable-integration-$buildbranch --name-only | grep -c -v --regexp="\.java$"))
    if [ ! -n "${TESTDOGS+x}" ]
    then
        # no TESTDOGS: run tests through ant normally
        $ANT migrate-schema
        $ANT test-integration test-webservice
    elif [ $allow_targeted_tests = 'false' ] || [ $non_java_changes -gt 0 ] || [ $ivy_changes -gt 0 ]; then
        $ANT test-compile
        # Run db updates on all the testdog dbs and then run all integration and webservice tests
        if [ $non_java_changes -gt 0 ]; then
            echo "$non_java_changes NON JAVA CHANGES FOUND"
        elif [ $ivy_changes -gt 0 ]; then
            echo "$ivy_changes IVY CHANGES FOUND"
        fi
        echo "RUNNING ALL INTEGRATION AND WEBSERVICE TESTS IN PARALLEL"
        (   find $wgspringcoreintegrationtestpath -name *wgspring*integration*jar -exec jar -tf \{} \; \
         && find target/test/integration target/test/webservice \
    )   | grep Test.class \
        | xargs -I CLASSFILE basename CLASSFILE .class \
        | $PYTHON conf/base/scripts/build/parallelTests.py \
              -s $TESTDOGS -v $apphomeenvvar $runslowtestsflag -n $testsperbatch \
              -d -t update-schema
    else
        $ANT test-compile
        # run db updates on test dog dbs and then run integration and webservice tests affected by changes
        # dependencies detected with turbo-athena: https://github.com/burkemw3/turbo-athena/
        echo "RUNNING SOME INTEGRATION AND WEBSERVICE TESTS IN PARALLEL"
        git diff origin/$buildbranch origin/last-stable-integration-$buildbranch --name-only \
        | egrep -o "net/wgen/.*\.java" | sed -e "s:/:.:g" -e "s:\.java$::I" -e"s:^:-m :" \
        | xargs -x java -jar "conf/base/scripts/build/turbo-athena-v1.0.1.jar" -c "target/" -t "target/test/integration" -t "target/test/webservice"  \
        | sed -r -e 's:([a-zA-Z0-9]+\.)+::' \
        | $PYTHON conf/base/scripts/build/parallelTests.py \
            -s $TESTDOGS -v $apphomeenvvar $runslowtestsflag -n $testsperbatch \
            -d -t update-schema
    fi
else
    echo "NO CHANGES FOUND OUTSIDE OF WEBDRIVER TESTS AND STATIC FILES.  SKIPPING INTEGRATION TESTS."
fi

# Remove existing RPMs in the repo to ensure the one we build gets deployed
rm -f $buildrpmrepo/mclass-tt-$app-$rpmversion-*.noarch.rpm
rm -f $buildrpmrepo/tt-migrations-$migrationsappname-$rpmversion-*.noarch.rpm

# Build webapp and db rpms
ci_build_utils.publish_rpms $app $migrationsappname $rpmversion $buildnumber \
    $workspace "$buildrpmrepo $secondary_build_rpm_repo"

# Add the last-stable-integration tag to the current commit
git branch -f last-stable-integration-$buildbranch
git push -f $gitrepobaseurl/$gitrepo.git last-stable-integration-$buildbranch

# Create tag with release number, if the build branch is the release branch
if [ "$buildbranch" = "release" ]
then
    buildreleasetag=$gitrepo-$rpmversion
    git tag -a -f -m "Release build #$buildnumber" $buildreleasetag
    git push -f $gitrepobaseurl/$gitrepo +refs/tags/$buildreleasetag:$buildreleasetag
fi

if [ "true" == "$publish_jars" ]
then
    $ANT ivy-publish-only
fi
