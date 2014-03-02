#!/bin/bash

# Script for up-stream merges. (i.e release->master, master->next)

# Exit immediately if a command exits with a non-zero status.
set -e

gitrepo=$1
origin=origin-$gitrepo
headbranch=$2
basebranch=$3
excludefile=$4

echo "** Reset: $basebranch"
git fetch $origin
git reset --hard $origin/$basebranch

echo "** Checkout: $basebranch"
git checkout $origin/$basebranch
echo "** Pull: $basebranch"
git pull $origin $basebranch

echo "** Merge $headbranch into $basebranch"
if [ -z "$excludefile" ]; then
    git merge $origin/$headbranch
else
    git merge --no-commit $origin/$headbranch
    git reset HEAD $excludefile
    git checkout -- $excludefile
    git commit -m "Merged $headbranch to $basebranch. Changes to $excludefile were ignored."
fi

echo "** Push merge commits to $basebranch"
git push -f $origin $basebranch
