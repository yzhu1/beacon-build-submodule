#!/usr/bin/python

import gitutils
import os
import subprocess
import sys
import pdb
import optparse
from collections import defaultdict

topReviewTemplate = ("=Overview=\n"
    +"*Hot Seat: \n"
    +"*Reviewers: \n"
    +"*Comments Expected By: (datetime)\n"
    +"=Files for Review=")

bottomReviewTemplate = ("=Fallout=\n"
    +"''Fallout list will be created here after review/discussion.''\n"
    +"=Comments=  \n"
    +"==<Your Name Here>==\n"
    +"[[Category:312 Platform]]\n"
    +"[[Category:Code Reviews]]\n")

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
    parser.add_option("-t", "--add-template",action="store_true", dest="template",help="add code review template to output")
    parser.add_option("-c", "--commits", action="store_true", dest="commits",help="link files that are changed by given commits")
    parser.set_description(
        "Generate links to files on the appropriate repository browsing application.  By default, "
        + "takes a list of patterns on the command line and generates a link for every file below "
        + "the current directory that matches one of those patterns."
        + "\n\nIf no patterns are given, reads a list of files to generate links for from STDIN."
        + "\nYou can also pass it a list of commits and it will generate links for all the files changed in those commits."
        )
    parser.set_usage("%prog [options] [pattern ... ]")
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
    @staticmethod
    def get_github_linker(repo):
        return wikilinker("https://{server}/{project_root}/tree/master/{path}",
                          "https://{server}/{project_root}/tree/{branch}/{path}", repo)
    @staticmethod
    def get_github_commit_linker(repo):
        return wikilinker("https://{server}/{project_root}/commit/{path}","",repo)

    @staticmethod
    def get_cgit_commit_linker(repo):
        return wikilinker("http://{server}/cgit/cgit.cgi/{project_root}/commit/?id={path}", "&h={branch}", repo)

    @staticmethod
    def get_gitweb_commit_linker(repo):
        return wikilinker("https://{server}/gerrit/gitweb?p={project_root}.git;a=commit;h={path}",
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

    def make_wiki_commit_link(self, commit, msg):
        url = self.get_link_url(commit)
        return "* [%s %s]" % (url, msg)

    def getFileMap (self, linkList):
        filesMap=defaultdict(list)
        for fileName in linkList:
            if "Test" in fileName:
                filesMap["4Tests"].append(fileName)
            elif "Controller" in fileName:
                filesMap["1Controllers"].append(fileName)
            elif "Service" in fileName:
                filesMap["2Services"].append(fileName)
            elif "Repository" in fileName:
                filesMap["3Repositories"].append(fileName)
            elif "DM" in fileName:
                filesMap["5Datamakers"].append(fileName)
            elif "ftl" in fileName:
                filesMap["6Freemarker"].append(fileName)
            elif "css" in fileName:
                filesMap["7css"].append(fileName)
            elif "js" in fileName and "java" not in fileName:
                filesMap["8JavaScript"].append(fileName)
            else:
                filesMap["9Others"].append(fileName)
        return filesMap

def main():
    (opts, arglist) = getargs()
    r = gitutils.get_repo()
    commits = []
    file_list = []
    if opts.branchfiles:
        file_list = r.branch_files()
    elif opts.commits and (0 < len(arglist)):
        commits = arglist
        for commit in commits:
            diff = "git diff " + commit + "^!"
            file_list = file_list + list(set(r.branch_files(diff)) - set(file_list))
    elif (0 < len(arglist)):
        file_list = []
        for argpath in arglist:
            file_list.extend(find_by_name(argpath))
    else:
        file_list = [filepath.strip() for filepath in sys.stdin.readlines()]
    if r.port() == 2222:
        linker = wikilinker.get_gitweb_linker(r)
        commit_linker = wikilinker.get_gitweb_commit_linker(r)
    elif "github" in r.server() :
        linker = wikilinker.get_github_linker(r)
        commit_linker = wikilinker.get_github_commit_linker(r)
    else:
        linker = wikilinker.get_cgit_linker(r)
        commit_linker = wikilinker.get_cgit_commit_linker(r)
    if opts.template:
        print topReviewTemplate
    linkList=list()
    for path in file_list:
        link = linker.make_wiki_link(path)
        linkList.append(link)
    fileMap = linker.getFileMap(linkList)
    fileKeys = fileMap.keys()
    fileKeys.sort();
    for fileKey in fileKeys:
        print "=="+fileKey[1:]+"=="
        for link in fileMap[fileKey]:
            print link
    if opts.template:
        if opts.branchfiles:
            commits = r.branch_commits()
        print "\n=Commits="
        for commit in commits:
            commit_msg = r.commit_message(commit)
            print commit_linker.make_wiki_commit_link(commit,commit_msg)
        print bottomReviewTemplate

if __name__ == "__main__":
    # to debug:
    #pdb.runcall(main)
    main()
