#!/bin/bash

###############################################################################
#
# The purpose of this script is to prep the release branches of Beacon
# projects for release. This entails merging the last stable master branch
# into the release branch, fetching the last published ivy.xml file
# and pointing ivy.module.file property to that file in each project, and
# pushing those changes in each project repo.
# Using the last published ivy file eliminates the need to "freeze" module
# dependencies by setting properties in default.build.properties to specific
# module versions. 
# 
# This script is to be run by Jenkins.
#
###############################################################################

#== CONSTANTS =================================================================

TRUE=0
FALSE=1


#== GLOBALS ===================================================================

#boolean to hold value set by is_app_already_prepped() (default is FALSE)
already_prepped=$FALSE


#== FUNCTIONS =================================================================

#------------------------------------------------------------------------------
# init
#
# Set up the environment.
#
init() {
    # add ant path to PATH
    export PATH=$PATH:/opt/wgen-3p/ant-1.8.1/bin/

    # set variables for repos
    OIB_HOME=$WORKSPACE/oib
    OUTCOMES_HOME=$WORKSPACE/outcomes
    OA_HOME=$WORKSPACE/oa
    HARBOR_HOME=$WORKSPACE/harbor
    ANT_OPTS="-Xms128m -Xmx2048m -XX:MaxPermSize=256m -XX:-UseGCOverheadLimit"
    REPO_URL_BASE=git@github.com:amplifylitco
    OIB_REPO_URL=$REPO_URL_BASE/oib.git
    OUTCOMES_REPO_URL=$REPO_URL_BASE/outcomes.git
    OA_REPO_URL=$REPO_URL_BASE/assess.git
    HARBOR_REPO_URL=$REPO_URL_BASE/harbor.git
    
    # grab variable values from the Jenkins job
    RELEASE_VERSION=$RELEASE_VERSION
    BRANCH=$RELEASE_BRANCH
}

#------------------------------------------------------------------------------
# log <message>
#
# Output the given message as a log entry.
#
log() {
    echo -e "\n>>> $1 <<<\n"
}

#------------------------------------------------------------------------------
# log_header <header text>
#
# Output a header with the given text
#
log_header() {
    echo -e "\n================================================================================"
    echo "=== $1"
    echo -e "===\n"
}

#------------------------------------------------------------------------------
# test_ret_val <message> <app name>
#
# Tests the return value of the last command, and exits if failure.
#
test_ret_val() {
    if [ $? -ne 0 ]
    then
        log "**ERROR: $1 (in $2)**"
        exit 1
    fi
}

#------------------------------------------------------------------------------
# clone_repo <repo url> <repo home> <repo name>
#
# Clone a git repository.
#
clone_repo() {
    cd $WORKSPACE
    log "Removing $3 repo if present..."
    rm -rf $3
    log "Cloning repo: $3"
    git clone $1 $2
    test_ret_val "running 'git clone $1 $2'" "jenkins node"
    log "Repo $3 cloned, initializing and updating submodule"
    cd $2
    touch conf/build.properties
    git submodule init
    git submodule update --init --recursive
}

#------------------------------------------------------------------------------
# merge_master_to_release <repo home> <app name>
#
# Merges 'master' branch into the 'release' branch in the given repo, commits
# the merge, and pushes.
#
merge_master_to_release() {
    cd $1
    log "Merging 'master' into '$BRANCH' for $2"
    git checkout $BRANCH
    git merge --no-commit origin/last-stable-master
    test_ret_val "merge failed. You will have to manually resolve the conflicts:\n\t"\
"git merge --no-commit origin/last-stable-master\n\t"\
"[resolve conflicts]\n\t"\
"git checkout --theirs conf/default.build.properties\n\t"\
"git add conf/default.build.properties\n\t"\
"git add conf/base\n\t"\
"git commit -m \"Merge last-stable-master to release.\"\n\t"\
"push the merge commit, and run this build again." $2
    git checkout --theirs conf/default.build.properties
    git add conf/default.build.properties
    git add conf/base
    git commit -m "Merge last-stable-master to release."
    log "Push merge commits to '$BRANCH' for $2"
    git push origin $BRANCH
    test_ret_val "push to '$BRANCH' failed" $2
}

#------------------------------------------------------------------------------
# is_app_already_prepped <repo home>
#
# Checks if the app has already been prepared for release.
# Returns $TRUE or $FALSE
#
is_app_already_prepped() {
    cd $1
    git checkout $BRANCH
    ls ivy-beacon-*$RELEASE_VERSION-*.xml
    if [ $? -ne 0 ]
    then
        already_prepped=$FALSE
    else
        already_prepped=$TRUE
    fi
}

#------------------------------------------------------------------------------
# fetch_and_set_ivy_file <repo home> <app name>
#
# Fetches the last published ivy file (ivy.xml)--uses the ant target
# fetch-last-published-ivy-file, which creates the file "ivy-[project name]-[version].xml".
# For example, ivy-beacon-oib-current-244.xml.
# Once the file is fetched, it is renamed to use the release version, the revision version
# is reset and the ivy.module.file property is set to point to this ivy file
# in conf/default.build.properties; changes are then pushed to the repo.
#
fetch_and_set_ivy_file() {
    cd $1
    # remove any old ivy files leftover from previous release
    git rm ./ivy-beacon-*.xml
    ant ivy-get-settings
    log "Fetching last published ivy file for $2"
    ant fetch-last-published-ivy-file -DpublishedRevision=current-+
    fetchedivyfilename=`find * -maxdepth 1 -name ivy-beacon*.xml`
    ivyfilename=${fetchedivyfilename/current/$RELEASE_VERSION}
    log "Received $fetchedivyfilename, renaming to $ivyfilename"
    mv $fetchedivyfilename $ivyfilename
    # override the ivy.module.file property by appending to conf/default.build.proprties
    echo "ivy.module.file=\${app.dir}/$ivyfilename" >> conf/default.build.properties
    # unfreeze the revision so that jar files can be published
    sed -i -r 's/revision="current-[0-9]+"/revision="\${project.revision}"/' $ivyfilename
}

#------------------------------------------------------------------------------
# commit_and_push <repo home> <app name>
#
# Commits and pushes changes to the given repo.
#
commit_and_push() {
    cd $1
    log "Commiting and pushing new ivy file and property to branch '$BRANCH' in $2"

    #assert that the commit has a modification to conf/default.build.properties and new ivy file
    #
    # This is now commented out to bypass projects whose release branch
    # preparation successfully completed. For example, if oib completed
    # but outcomes failed due to a merge conflict, and the conflict was
    # resolved and the build rerun, oib will try to prep again but will
    # fail because it's expecting changes, but the expected changes were
    # already pushed in the previous run.
    #
    # This should be more robust--perhaps check if a project's release branch
    # has already been prepped, and if so, move on to the next project.
    #
    #gitStatus=`git status -s`
    #git status -s | grep "conf/default.build.properties"
    #test_ret_val "commit should include a modification to conf/default.build.properties--git status -s shows:\n$gitStatus\n" $2
    #git status -s | grep "ivy-beacon.*\.xml"
    #test_ret_val "commit should include a new ivy xml file--git status -s shows:\n$gitStatus\n" $2

    git add --all
    git commit -m "Point ivy.module.file property to $ivyfilename"
    git push origin $BRANCH
}

#------------------------------------------------------------------------------
# prepare_release_branch <repo url> <repo home> <app name>
#
# Prepares the release branch for the given project.
#
prepare_release_branch() {
    log_header $3
    clone_repo $1 $2 $3
    is_app_already_prepped $2
    if [ $already_prepped -eq $FALSE ]
    then
        merge_master_to_release $2 $3
        fetch_and_set_ivy_file $2 $3
        commit_and_push $2 $3
    else
        log "$3's release branch has already been prepared. Moving on..."
    fi
}

#== end FUNCTIONS =============================================================

init

prepare_release_branch $OIB_REPO_URL $OIB_HOME oib
prepare_release_branch $OUTCOMES_REPO_URL $OUTCOMES_HOME outcomes
prepare_release_branch $OA_REPO_URL $OA_HOME oa
prepare_release_branch $HARBOR_REPO_URL $HARBOR_HOME harbor

exit 0
