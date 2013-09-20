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

    rm -rf $workspace/RPM_STAGING
    mkdir -p $workspace/opt/tt/webapps/$app

    for rpm_repo in $rpm_repositories
    do
        echo "building $app and $migrations RPMs for repository $rpm_repo"
        rm -f $rpm_repo/mclass-tt-$app-$rpmversion-*.noarch.rpm
        rm -f $rpm_repo/tt-migrations-$migrations-$rpmversion-*.noarch.rpm
        # Build webapp and db rpms
        python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $rpm_repo -r $workspace/RPM_STAGING \
                -D${app}dir=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-$app.spec
        python /opt/wgen/rpmtools/wg_rpmbuild.py -v -o $rpm_repo -r $workspace/RPM_STAGING \
                -Dcheckoutroot=$workspace -Drpm_version=$rpmversion -Dbuildnumber=$buildnumber $workspace/rpm/tt-migrations-$app.spec
    done
    # Promote them to CI rpm repo
    for rpm_repo in $rpm_repositories
    do
        echo "Running createrepo for $rpm_repo"
        /opt/wgen/rpmtools/wg_createrepo $rpm_repo
    done
}