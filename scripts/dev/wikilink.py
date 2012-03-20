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
    def __init__(self, linkformat, branch_format, repo):
        self._link_format = linkformat
        if branch_format.startswith("http"):
            self._branch_format = branch_format
        else:
            self._branch_format = linkformat + branch_format
        self._repository = repo

    @staticmethod
    def get_cgit_linker(repo):
        return wikilinker("http://{server}/cgit/cgit.cgi/{project_root}/tree/{path}", "?h={branch}", repo)

    @staticmethod
    def get_gitweb_linker(repo):
        return wikilinker("https://{server}/gerrit/gitweb?p={project_root}.git;a=blob;f={path}",
                          ";hb=refs/heads/{branch}", repo)

    def get_link_url(self, path):
        repo = self._repository
        rooted_path = repo.rooted_path(path)
        server = repo.server()
        root = repo.root()
        branch = repo.branch()
        if None != branch:
            url = self._branch_format.format(server=server,project_root=root, path=rooted_path, branch=branch)
        else:
            url = self._link_format.format(server=server,project_root=root, path=rooted_path)
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
    if r.port() == 2222:
        linker = wikilinker.get_gitweb_linker(r)
    else:
        linker = wikilinker.get_cgit_linker(r)
    for path in file_list:
        link = linker.make_wiki_link(path)
        print link



if __name__ == "__main__":
    # to debug:
    #pdb.runcall(main)
    main()
