#!/bin/echo This file is not intended for direct execution

# Functions in this file should, by convention, start with "ci_build_utils.".  There is no
# enforcement ofthis convention available, it just serves as a marker.

## publish_rpms
## Arguments:
###     app: the application name (e.g. "oib")
###     migrations: the name of the migrations rpm (possibly the same as $app)
###     rpmversion: the root version (e.g. 22.3.0)
###     buildnumber: the jenkins build identifier
###     workspace: the workspace directory where we will create the RPM
###     rpm_repositories: one or more paths to RPM repositories where this RPM should be published
function ci_build_utils.publish_rpms() {
    app=$1
    migrations=$2
    rpmversion=$3
    buildnumber=$4
    workspace=$5
    rpm_repositories=${@:6}

    rpm_target_dir="$workspace/target/rpm"

    rm -rf $workspace/RPM_STAGING
    mkdir -p $workspace/opt/tt/webapps/$app
    mkdir -p $rpm_target_dir
    rm -f $rpm_target_dir/*
    # Build webapp and db rpms in local workspace
    python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $rpm_target_dir -r $workspace/RPM_STAGING \
        -D${app}dir=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-$app.spec
    python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $rpm_target_dir -r $workspace/RPM_STAGING \
        -Dcheckoutroot=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-migrations-$app.spec

    # not sure why this needs to exist, but no sense leaving it lying around
    rm -rf $workspace/opt

    # copy RPMs to each repository, and update
    for rpm_repo in $rpm_repositories
    do
        echo "building $app and $migrations RPMs for repository $rpm_repo"
        rm -f $rpm_repo/mclass-tt-$app-$rpmversion-*.noarch.rpm
        rm -f $rpm_repo/tt-migrations-$migrations-$rpmversion-*.noarch.rpm
        cp $rpm_target_dir/*.rpm $rpm_repo
        /opt/wgen/rpmtools/wg_createrepo $rpm_repo
    done
}

## setup_build_env

## No arguments, but reads the following environment variables:
### BASE_ENV (required - one of DEV/FUTURE/CURRENT)
### SKIP_BCFG (optional - if "true", does what it says)
### BUILD_EL6 (optional - if "true", uses the EL6 repository as the build repo, and promotes to both EL5 and EL6 repos)
### TESTDOG_COUNT (optional - if something that looks like a number, sets TESTDOGS to a reasonable value based on that number)

## After running, the following should be set or updated, assuming the jenkins environment is correctly configured
### ENV
### ENV_PROPERTY_PREFIX
### AUTORELEASE_BOX
### RELEASE_VERSION
### BUILD_BRANCH
### BUILD_RPM_REPO
### NEXT_RPM_REPO
### SECOND_NEXT_RPM_REPO (if required)
### EXTRA_WGR_ARG (if the global refspec is set)
### RELEASE_STEPS_TO_SKIP (if SKIP_BCFG is set)
### TESTDOGS (if TESTDOG_COUNT is set)

function ci_build_utils.setup_build_env() {
    # meta-configuration: figure out which Jenkins variables to look in for various properties
    REFSPEC_VAR=BEACON_${BASE_ENV}_REFSPEC
    if [ "DEV" == "${BASE_ENV}" ]
    then
        export ENV=dev
        AUTORELEASE_VAR=AUTORELEASE_DEV
        RPM_VERSION_VAR=FUTURE_RPM_VERSION
        BUILD_REPO_VAR=REPO_DEV
    else
        export ENV=`perl -e 'printf "\L$ENV{BASE_ENV}ci"'`
        AUTORELEASE_VAR=AUTORELEASE_${BASE_ENV}_CI
        RPM_VERSION_VAR=${BASE_ENV}_RPM_VERSION
        BUILD_REPO_VAR=REPO_${BASE_ENV}_CI
        NEXT_REPO_VAR=REPO_${BASE_ENV}_QA
    fi
    if [ "true" == "${BUILD_EL6:-}" ]
    then
        BUILD_REPO_VAR="${BUILD_REPO_VAR}_EL6"
        if [ -n "${NEXT_REPO_VAR:-}" ]
        then
            SECOND_NEXT_REPO_VAR=${NEXT_REPO_VAR}_EL6
        fi
    fi

    export RELEASE_VERSION=`perl -le' print {DEV=>"mcfuture",FUTURE=>"mcfuture", CURRENT=>"mccurrentci"}->{$ENV{BASE_ENV}} || "NO_RELEASE_VERSION"'`
    # strip off origin-whatever:
    BUILD_BRANCH=${GIT_BRANCH#origin*/}
    # then strip off last-stable-integration-, if present:
    export BUILD_BRANCH=${GIT_BRANCH#*last-stable-integration-}

    # set defaults if the variables are currently empty:
    if [ -z "${RPM_VERSION:-}" ];         then export RPM_VERSION=${!RPM_VERSION_VAR}; fi
    if [ -z "${MIGRATIONS_APP_NAME:-}" ]; then export MIGRATIONS_APP_NAME=$APP; fi
    if [ -z "${GIT_REPO:-}" ];            then export GIT_REPO=$APP; fi
    if [ -z "${WEBAPP_HOSTCLASS:-}" ];    then export WEBAPP_HOSTCLASS=mhctt${APP}webapp; fi


    export AUTORELEASE_BOX=${!AUTORELEASE_VAR}
    export BUILD_RPM_REPO=${!BUILD_REPO_VAR}
    export NEXT_RPM_REPO=${!NEXT_REPO_VAR:-}
    export SECOND_NEXT_RPM_REPO=${!SECOND_NEXT_REPO_VAR:-}
    export ENV_PROPERTY_PREFIX=$ENV
    if [ -n "${TESTDOG_COUNT:-}" ]
    then
        export TESTDOGS=`perl -e'print join ",", map "testdog$ENV{ENV}$_", 0..($ENV{TESTDOG_COUNT} - 1)'`
    fi

    if [ -n "${!REFSPEC_VAR:-}" ]; then export EXTRA_WGR_ARGS="--refspec '${!REFSPEC_VAR}'"; fi

    export RELEASE_STEPS_TO_SKIP="${RELEASE_STEPS_TO_SKIP:-} ${WEBAPP_HOSTCLASS}_nagios_notifications_disable.sh  ${WEBAPP_HOSTCLASS}_nagios_notifications_enable.sh"
    # this is highly jenkins-coupled: checking the box will set this environment variable to "true"
    if [ "true" == "${SKIP_BCFG:-}" ]
    then
        export RELEASE_STEPS_TO_SKIP="${RELEASE_STEPS_TO_SKIP} ${WEBAPP_HOSTCLASS}_bcfg.sh"
    fi
}
