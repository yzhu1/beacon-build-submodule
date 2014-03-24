#!/bin/bash

# Script for up-stream merges. (i.e release->master, master->next)

# Exit immediately if a command exits with a non-zero status.
set -e


headbranch=$1
basebranch=$2
excludefile=$3

echo "** Merge $headbranch into $basebranch"
if [ -z "$excludefile" ]; then
    git merge origin/$headbranch
else
    git merge --no-commit origin/$headbranch | grep -E 'fix conflicts and then commit the result|Already up-to-date'
    git checkout HEAD $excludefile
    git commit -m "Merged $headbranch to $basebranch. Changes to $excludefile were ignored." | grep -E 'nothing added to commit|no changes added to commit|nothing to commit|files changed'
fi

echo "** Push merge commits to $basebranch"
#git push origin HEAD:$basebranch
