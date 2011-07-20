#!/usr/bin/python
import os
import re
import subprocess

# need to remember how auto-doc works...

def find_repo():
    matcher = re.compile("git\@([^:]+):(\S+)")
    config = os.popen("git config --get remote.origin.url")
    git_url = config.readline()
    config.close()
    (server,repo) = matcher.search(git_url).groups()
    (repo_base,repo_ext) = os.path.splitext(repo)
    return { "server" : server, "root" : repo_base }

def find_branch():
    branches = os.popen("git branch")
    matcher = re.compile("^\* (.+)") # matches "(no branch)" or a real branch name
    for branchline in branches.readlines():
        branchmatch = matcher.search(branchline)
        if None != branchmatch:
            found_branch = branchmatch.groups()[0]
            break
    branches.close()
    if ("(no branch)" != found_branch) & ("master" != found_branch):
        return found_branch
    else:
        return None

def find_path_to_repo_root():
    cdup_path = os.popen("git rev-parse --show-cdup").readline()
    return cdup_path.rstrip()

def find_with_repo_relative_path(path_to_root, pattern):
    find = subprocess.Popen(
        ["find", ".", "-name", pattern], shell=False, stdout=subprocess.PIPE)
    pathlist = []
    for line in find.stdout.readlines():
        pathlist.append(os.path.relpath(line.rstrip(), path_to_root))
    return pathlist
