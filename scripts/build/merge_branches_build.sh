#!/bin/bash

# Script for up-stream merges. (i.e release->master or master->next)

gitrepobaseurl="git@github.wgenhq.net:Beacon"
gitrepo=$1
headbranch=$2
basebranch=$3

echo "** Reset: $basebranch"
git fetch $gitrepobaseurlgit/$gitrepo
git reset --hard origin-$gitrepo/$basebranch

echo "** Checkout: $basebranch"
git checkout origin-$gitrepo $basebranch
echo "** Pull: $basebranch"
git pull origin-$gitrepo $basebranch

echo "** Merge $headbranch into $basebranch"
git merge origin-$gitrepo/$headbranch

echo "** Push merge commits to $basebranch"
git push origin-$gitrepo $basebranch
