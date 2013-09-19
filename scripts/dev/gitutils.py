#!/usr/bin/python
import os
import re

# need to remember how auto-doc works...

_pattern_strict = "^ssh://(?:(?:\w+)@)?([\w.]+)(?::(\d+))?/(\S+)$"
_pattern_loose = "(?:(?:\w+)\@)?([\w.]+)[:/](\S+)"

def find_repo_props():
    matcher = re.compile(_pattern_strict)
    config = os.popen("git config --get remote.origin.url")
    git_url = config.readline()
    config.close()
    match = matcher.search(git_url)
    if (None != match):
        (server, port, repo) = match.groups()
    else:
        matcher = re.compile(_pattern_loose)
        match = matcher.search(git_url)
        if None == match:
            print "Unable to match git repo URL '%s'" % git_url
            throw
        (server, repo) = match.groups()
        port = None
    (repo_base,repo_ext) = os.path.splitext(repo)
    return { "server" : server, "root" : repo_base, "port" : port }

def find_commits_by_pattern(pattern):
    commits = os.popen("git log --pretty=format:'%Creset%C(red bold)[%ad] %C(blue bold)%h  %Creset%s %C(green bold)(%an)%Creset' --abbrev-commit --date=short --all --grep " + pattern)
    found_commits = commits.readlines()
    commits.close()
    return found_commits

def find_branches_by_pattern(pattern):
    branches = os.popen("git branch")
    matcher = re.compile(pattern) 
    found_branches = []
    for branchline in branches.readlines():
        branchmatch = matcher.search(branchline)
        if None != branchmatch:
            found_branches.append(branchmatch.groups()[0])
    branches.close()
    return found_branches

def find_branch():
    found_branch = find_branches_by_pattern("^\* (.+)")[0] # matches "(no branch)" or a real branch name
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
    return gitrepo(props['server'], props['root'], props['port'], local_root, branch)

class gitrepo(object):
    def __init__(self, server, repo_root, repo_port, path_to_local_root, current_branch):
        self._repo_server = server
        self._repo_root = repo_root
        self._repo_port = repo_port
        self._path_to_local_root = path_to_local_root
        self._current_branch = current_branch

    def branch(self):
        return self._current_branch
    def server(self):
        return self._repo_server
    def root(self):
        return self._repo_root
    def port(self):
        if None == self._repo_port:
            return 22
        else:
            return int(self._repo_port)
    def branch_checked(self):
        branch = self._current_branch
        if (None == branch):
            branch = "HEAD"
        return branch
    def rooted_path(self, local_path):
        return os.path.relpath(local_path, self._path_to_local_root)

    def rooted_paths(self, pathlist):
        return map(self.rooted_path,pathlist)

    def branch_files(self, basecmd = "git diff --name-only `git merge-base origin/master {commit}`..{commit}"):
        if not "--name-only" in basecmd:
            basecmd += " --name-only"
        branch = self.branch_checked()
        cmd = basecmd.format(commit=branch)
        pathlist = [path.rstrip() for path in os.popen(cmd).readlines()]
        return self.rooted_paths(pathlist)

    def branch_commits(self):
        branch = self.branch_checked()
        cmd = "git log `git merge-base origin/master {commit}`.. --oneline"
        cmd = cmd.format(commit=branch)
        commitList = [commit_log[:7] for commit_log in os.popen(cmd).readlines()]
        return commitList

    def commit_message(self, commit):
        branch = self.branch_checked()
        cmd = "git log --pretty=oneline --abbrev-commit " + commit + "^!"
        return os.popen(cmd).readline().rstrip()[8:]
