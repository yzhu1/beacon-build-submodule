#!/bin/bash

# Script for up-stream merges. (i.e release->master, master->next)

gitrepobaseurl="git@github.wgenhq.net:Beacon"
gitrepo=$1
headbranch=$2
basebranch=$3

git fetch $gitrepobaseurlgit/$gitrepo
git checkout $basebranch
git merge origin-$gitrepo/$headbranch
git push $gitrepobaseurlgit/$gitrepo $basebranch
