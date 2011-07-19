#!/usr/bin/python

import gitutils
import os
import sys

def make_cgit_url(repo_data, file_path, branch=None):
    pattern = "http://%s/cgit/cgit.cgi/%s/%s"
    url = pattern % (repo_data.get("server"), repo_data.get("root"), file_path)
    if None != branch:
        url += "?h=" + branch
    return url

def make_wiki_link(repo_data, file_path, branch=None):
    adjusted_path = os.path.relpath(file_path, gitutils.find_path_to_repo_root())
    url = make_cgit_url(repo_data, adjusted_path, branch)
    basename = os.path.basename(file_path)
    return "* [%s %s]" % (url, basename)

def main():
    argpath = sys.argv[1]
    current_branch = gitutils.find_branch()
    repo_info = gitutils.find_repo()
    print make_wiki_link(repo_info, argpath, current_branch)


if __name__ == "__main__":
    main()
