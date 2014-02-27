#!/bin/bash

# Script for up-stream merges. (i.e release->master, master->next)

# Exit immediately if a command exits with a non-zero status.
set -e

gitrepo=$1
origin=origin-$gitrepo
headbranch=$2
basebranch=$3

echo "** Reset: $basebranch"
git fetch $origin
git reset --hard $origin/$basebranch

echo "** Checkout: $basebranch"
git checkout $origin/$basebranch
echo "** Pull: $basebranch"
git pull $origin $basebranch

echo "** Merge $headbranch into $basebranch"
git merge $origin/$headbranch

echo "** Push merge commits to $basebranch"
git push -f $origin $basebranch
