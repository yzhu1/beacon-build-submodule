#!/usr/bin/python
import os
import re

# need to remember how auto-doc works...

def find_repo_props():
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


def get_repo():
    props = find_repo_props()
    local_root = find_path_to_repo_root()
    branch = find_branch()
    return gitrepo(props['server'], props['root'], local_root, branch)

class gitrepo(object):
    def __init__(self, server, repo_root, path_to_local_root, current_branch):
        self._repo_server = server
        self._repo_root = repo_root
        self._path_to_local_root = path_to_local_root
        self._current_branch = current_branch

    def branch(self):
        return self._current_branch
    def server(self):
        return self._repo_server
    def root(self):
        return self._repo_root

    def rooted_path(self, local_path):
        return os.path.relpath(local_path, self._path_to_local_root)

    def rooted_paths(self, pathlist):
        return map(self.rooted_path,pathlist)