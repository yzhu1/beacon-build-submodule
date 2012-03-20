#!/usr/bin/python

import gitutils
import os
import subprocess
import sys
import pdb
import optparse

def find_by_name(pattern):
    find = subprocess.Popen(
        ["find", ".", "-name", pattern], shell=False, stdout=subprocess.PIPE)
    pathlist = []
    for line in find.stdout.readlines():
        pathlist.append(line.rstrip())
    return pathlist

def getargs():
    parser = optparse.OptionParser()
    parser.add_option("-b", "--branch-files", dest="branchfiles",action="store_true",help="link files that are changed on this branch")
    return parser.parse_args()

class wikilinker(object):
    def __init__(self, linkformat, branch_handler, repo):
        self._link_format = linkformat
        self._branch_handler = branch_handler
        self._repository = repo

    @staticmethod
    def get_cgit_linker(repo):
        def handler(base_url, branchname):
            url = base_url
            if None != branchname:
                url += "?h=" + branchname
            return url
        return wikilinker("http://%s/cgit/cgit.cgi/%s/tree/%s", handler, repo)

    def get_link_url(self, path):
        repo = self._repository
        rooted_path = repo.rooted_path(path)
        server = repo.server()
        root = repo.root()
        branch = repo.branch()
        url = self._link_format % (server, root, rooted_path)
        if None != branch:
            url = self._branch_handler(url, branch)
        return url

    def make_wiki_link(self, path):
        url = self.get_link_url(path)
        basename = os.path.basename(path)
        return "* [%s %s]" % (url, basename)

def main():
    (opts, arglist) = getargs()
    r = gitutils.get_repo()
    if opts.branchfiles:
        file_list = r.branch_files()
    elif (0 < len(arglist)):
        file_list = []
        for argpath in arglist:
            file_list.extend(find_by_name(argpath))
    else:
        file_list = [filepath.strip() for filepath in sys.stdin.readlines()]
    # print file_list
    linker = wikilinker.get_cgit_linker(r)
    for path in file_list:
        link = linker.make_wiki_link(path)
        print link



if __name__ == "__main__":
    # to debug:
    #pdb.runcall(main)
    main()
