#!/bin/bash

# Script to freeze the modules versions for the 'release' branch

# Exit immediately if a command exits with a non-zero status.
set -e

# Modules' versions set from the build paramerters
wgspringcore_revision=${1}
wgspringmodule_userappstate_revision=${2}
wgspringmodule_mathml_revision=${3}
wgspringmodule_web_common_revision=${4}
core_lib_java_revision=${5}
mas_client_revision=${6}
amplify_ui_toolkit_revision=${7}
branding_web_assets_revision=${8}
tinymce_revision=${9}
java_logging_revision=${10}

workspace=$WORKSPACE
gitrepo=$GIT_REPO
origin=origin-$gitrepo
default_build_properties_file=./conf/default.build.properties

cd $workspace/

git fetch $origin

sed -i 's/^mclass-dependencies.default.branch.*/mclass-dependencies.default.branch = current/g' $default_build_properties_file

sed -i "s/^wgspringcore.revision.*/wgspringcore.revision = ${wgspringcore_revision}/g" $default_build_properties_file
sed -i "s/^wgspringmodule.userappstate.revision.*/wgspringmodule.userappstate.revision = ${wgspringmodule_userappstate_revision}/g" $default_build_properties_file
sed -i "s/^wgspringmodule.mathml.revision.*/wgspringmodule.mathml.revision = ${wgspringmodule_mathml_revision}/g" $default_build_properties_file
sed -i "s/^wgspringmodule.web-common.revision.*/wgspringmodule.web-common.revision = ${wgspringmodule_web_common_revision}/g" $default_build_properties_file
sed -i "s/^mclass-dependencies.core-lib-java.revision.*/mclass-dependencies.core-lib-java.revision = ${core_lib_java_revision}/g" $default_build_properties_file
sed -i "s/^mclass-dependencies.mas.revision.*/mclass-dependencies.mas.revision = ${mas_client_revision}/g" $default_build_properties_file
sed -i "s/^mclass-dependencies.amplify-ui-toolkit.revision.*/mclass-dependencies.amplify-ui-toolkit.revision = ${amplify_ui_toolkit_revision}/g" $default_build_properties_file
sed -i "s/^branding-web-assets.revision.*/branding-web-assets.revision = ${branding_web_assets_revision}/g" $default_build_properties_file
sed -i "s/^tinymce-jquery.revision.*/tinymce-jquery.revision = ${tinymce_revision}/g" $default_build_properties_file
sed -i "s/^java-logging.revision.*/java-logging.revision = ${java_logging_revision}/g" $default_build_properties_file

git add $default_build_properties_file
git commit $default_build_properties_file -m "Release build script: Freeze the project's module versions."
git push $origin release
