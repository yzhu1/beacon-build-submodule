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
beacon_shared_web_assets_revision=${11}

workspace=$WORKSPACE
gitrepo=$GIT_REPO
origin=origin-$gitrepo
default_build_properties_filename=default.build.properties
default_build_properties_file=./conf/${default_build_properties_filename}
releasebranch=release

# resolve dependency modules from the current repo
if grep -Fq "mclass-dependencies.default.branch" $default_build_properties_file
then
	echo "Set mclass-dependencies.default.branch to current"
	sed -i "s/^mclass-dependencies.default.branch.*/mclass-dependencies.default.branch = current/g" $default_build_properties_file
else
	echo "Append line : mclass-dependencies.default.branch = current"
	echo "mclass-dependencies.default.branch = current" >> $default_build_properties_file
fi

# freeze module versions: no-op of the corresponding build parameter is not set
if [[ ! -z "$wgspringcore_revision" ]] && test "$wgspringcore_revision" != "-"
then
	echo "freezed wgspringcore.revision to $wgspringcore_revision"
	sed -i "s/^wgspringcore.revision.*/wgspringcore.revision = ${wgspringcore_revision}/g" $default_build_properties_file
fi

# userappstate
if [[ ! -z "$wgspringmodule_userappstate_revision" ]] && test "$wgspringmodule_userappstate_revision" != "-"
then
	echo "freezed wgspringmodule.userappstate.revision at $wgspringmodule_userappstate_revision"
	sed -i "s/^wgspringmodule.userappstate.revision.*/wgspringmodule.userappstate.revision = ${wgspringmodule_userappstate_revision}/g" $default_build_properties_file
fi

# mathml
if [[ ! -z "$wgspringmodule_mathml_revision" ]] && test "$wgspringmodule_mathml_revision" != "-"
then
	echo "freezed wgspringmodule.mathml.revision at $wgspringmodule_mathml_revision"
	sed -i "s/^wgspringmodule.mathml.revision.*/wgspringmodule.mathml.revision = ${wgspringmodule_mathml_revision}/g" $default_build_properties_file
fi

# wgspring web common
if [[ ! -z "$wgspringmodule_web_common_revision" ]] && test "$wgspringmodule_web_common_revision" != "-"
then
	echo "freezed wgspringmodule.web-common.revision at $wgspringmodule_web_common_revision"
	sed -i "s/^wgspringmodule.web-common.revision.*/wgspringmodule.web-common.revision = ${wgspringmodule_web_common_revision}/g" $default_build_properties_file
fi

# core_lib_java
if [[ ! -z "$core_lib_java_revision" ]] && test "$core_lib_java_revision" != "-"
then
	echo "freezed mclass-dependencies.core-lib-java.revision at $core_lib_java_revision"
	sed -i "s/^mclass-dependencies.core-lib-java.revision.*/mclass-dependencies.core-lib-java.revision = ${core_lib_java_revision}/g" $default_build_properties_file
fi

# mas client
if [[ ! -z "$mas_client_revision" ]] && test "$mas_client_revision" != "-"
then
	echo "freezed mclass-dependencies.mas.revision at $mas_client_revision"
	sed -i "s/^mclass-dependencies.mas.revision.*/mclass-dependencies.mas.revision = ${mas_client_revision}/g" $default_build_properties_file
fi

# ui toolkit
if [[ ! -z "$amplify_ui_toolkit_revision" ]] && test "$amplify_ui_toolkit_revision" != "-"
then
	echo "freezed mclass-dependencies.amplify-ui-toolkit.revision at $amplify_ui_toolkit_revision"
	sed -i "s/^mclass-dependencies.amplify-ui-toolkit.revision.*/mclass-dependencies.amplify-ui-toolkit.revision = ${amplify_ui_toolkit_revision}/g" $default_build_properties_file
fi

# branding web assets
if [[ ! -z "$branding_web_assets_revision" ]] && test "$branding_web_assets_revision" != "-"
then
	echo "freezed branding-web-assets.revision at $branding_web_assets_revision"
	sed -i "s/^branding-web-assets.revision.*/branding-web-assets.revision = ${branding_web_assets_revision}/g" $default_build_properties_file
fi

# tinymce
if [[ ! -z "$tinymce_revision" ]] && test "$tinymce_revision" != "-"
then
	echo "freezed tinymce-jquery.revision at $tinymce_revision"
	sed -i "s/^tinymce-jquery.revision.*/tinymce-jquery.revision = ${tinymce_revision}/g" $default_build_properties_file
fi

# java logging
if [[ ! -z "$java_logging_revision" ]] && test "$java_logging_revision" != "-"
then
	echo "freezed java-logging.revision at $java_logging_revision"
	sed -i "s/^java-logging.revision.*/java-logging.revision = ${java_logging_revision}/g" $default_build_properties_file
fi

# BSWA
if [[ ! -z "$beacon_shared_web_assets_revision" ]] && test "$beacon_shared_web_assets_revision" != "-"
then
	echo "freezed beacon-shared-web-assets.revision at $beacon_shared_web_assets_revision"
	sed -i "s/^beacon-shared-web-assets.revision.*/beacon-shared-web-assets.revision = ${beacon_shared_web_assets_revision}/g" $default_build_properties_file
fi

if git status | grep "modified:" | grep -q "${default_build_properties_filename}"
then
	git add $default_build_properties_file
	git commit $default_build_properties_file -m "Release preparation: Freeze the project's module versions."
	git push $origin HEAD:$releasebranch
fi

