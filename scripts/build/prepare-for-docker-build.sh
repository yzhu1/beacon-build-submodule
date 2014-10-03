#!/bin/bash

#
# This script prepares the docker root directory (directory where the
# Dockerfile is located) for Docker to build the image for the webapp.
# When adding files from the host to a docker image, Docker's ADD
# command cannot reference any path above the directory the Dockerfile
# resides in. Thus, we need to copy any files that the Dockerfile needs
# that live outside the docker root directory structure to somewhere
# inside the docker root directory structure.
#
# An alternative to this would be to have the Dockerfile live in the app
# root directory, thus making all files in the app repo fair game for
# the Dockerfile. However, by copying these static files into one location
# in the docker directory we can consolidate all static content into one
# ADD command in the Dockerfile, thus making the docker build step faster
# (as each command in the Dockerfile creates a new filesystem layer, which
# generally takes longer than mere cp commands in shell).
#

# -e: Exit  immediately  if a simple command (see SHELL GRAMMAR above) exits with a non-zero status
# -u: Treat unset variables as an error when performing parameter expansion
set -eu

ANT="/opt/wgen-3p/ant-1.8.1/bin/ant"
DOCKER_DIR=$WORKSPACE/conf/docker

# build the war file and target/web-assets
ant war

# copy files that Dockerfile is dependent on to the docker root directory
cp $WORKSPACE/target/*.war $DOCKER_DIR/
cp -r $WORKSPACE/src/main/webapp/static $DOCKER_DIR/static
cp -r $WORKSPACE/target/web-assets/compile/css $DOCKER_DIR/static/css
cp -r $WORKSPACE/target/web-assets/unzip/wgspringmodule-web-common-web-assets/web/static/common $DOCKER_DIR/static/common
cp -r $WORKSPACE/target/web-assets/unzip/wgspringmodule-mathml-web-assets/web/static/mathml $DOCKER_DIR/static/mathml
cp -r $WORKSPACE/target/web-assets/unzip/tinymce-jquery-web-assets/web/static/tinymce-jquery $DOCKER_DIR/static/tinymce-jquery
#Harbor and OA to not use amplify toolkit
if [ -d "$WORKSPACE/target/web-assets/unzip/amplify-ui-toolkit-web-assets/web" ]
then
    cp -r $WORKSPACE/target/web-assets/unzip/amplify-ui-toolkit-web-assets/web $DOCKER_DIR/static/amplify-ui
fi
