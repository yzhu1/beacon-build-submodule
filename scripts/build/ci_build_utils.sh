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
    rm $rpm_target_dir/*
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
