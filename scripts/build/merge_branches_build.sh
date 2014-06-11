#!/bin/bash

# Script for up-stream merges. (i.e release->master, master->next)

# Exit immediately if a command exits with a non-zero status.
set -e


headbranch=$1
basebranch=$2
excludefile=$3

if git merge --no-commit --no-ff origin/$headbranch | grep -q "Automatic merge failed; fix conflicts and then commit the result."
then
	if git status | grep "modified:" | grep "conf/base"
	then
		git status
		echo "ERROR: conf/base needs to be manually merged!"
		exit 1
    fi
fi

# if the exclude file variable is set and if the file exists, ignore any modification to it
if [[ ! -z "$excludefile" ]] && [[ -e "$excludefile" ]]
then
	git checkout HEAD $excludefile
	git add $excludefile
	echo "** Changes to $excludefile ignored"
fi

# remove the ivy xml file that is used for release
ivyfile=`find * -maxdepth 1 -name ivy-beacon*.xml`
if [ ! -z $ivyfile ]
then
    git rm -f $ivyfile
    echo "** Removed ivy xml file for release: $ivyfilename"
fi


if git status | grep "both modified:"
then
	git status
	echo "ERROR: There're still unmerged conflicts, need manual merge!"
	exit 1
fi

if git status | grep "modified:"
then
	git commit -m "Jenkins: Merge $headbranch to $basebranch"
	git push origin HEAD:$basebranch
	echo "** Merged $headbranch to $basebranch"
else
	echo "** Nothing to merge."
fi
