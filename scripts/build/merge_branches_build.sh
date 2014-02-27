#!/bin/bash

# Script for up-stream merges. (i.e release->master or master->next)

gitrepobaseurl="git@github.wgenhq.net:Beacon"
gitrepo=$1
headbranch=$2
basebranch=$3

git fetch $gitrepobaseurlgit/$gitrepo
git checkout origin-$gitrepo $basebranch
git merge origin-$gitrepo/$headbranch
git push -f origin-$gitrepo $basebranch 
