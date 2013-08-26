#!/usr/bin/python
import sys
sys.path.append('conf/base/scripts/dev/')
from fogbugz import FogBugz
import optparse
import fbSettings
import authenticationConfigs
import gitutils
import os
import csv
import datetime

def getargs():
    parser = optparse.OptionParser()
    parser.add_option("-a", "--assignedTo", dest="assignedTo",action="store",help="show only cases assigned to specified person")
    parser.add_option("-m", "--milestone", dest="milestone",action="store",help="show only cases for specified milestone")
    parser.add_option("-t", "--team", dest="project",action="store",help="show only cases for specified project")
    parser.add_option("-p", "--priority", dest="priority",action="store",help="show only cases for specified project")
    parser.add_option("-s", "--status", dest="status",action="store",help="show only cases with the specified status")
    parser.add_option("-c", "--commits", action="store_true", dest="show_commits",help="shows all branches and commits which have the case id in the branch name or commit message")
    parser.add_option("-e", "--export",action="store_true", dest="export",help="exports results to csv")
    parser.set_description('You need to have python and pip installed in order to use this script. \nAfter that run sudo pip install fogbugz. \nThen to set up your credentials, first go to https://fb.wgen.net/api.asp?cmd=logon&email=<email>&password=<password> to obtain your unique fogbugz token. Then create a file conf/base/scripts/dev/fogbugz/authenticationConfigs.py and add the line: \nTOKEN = "<your_token>" \n If you don\'t specify any of the options, then a fogbugzsearch will be performed based on whatever argument you provide which can include a space or comma separated list of bug ids. Max number of bugs which can be listed have been limited to 999 but this can be changed in fbSettings.py')
    parser.set_usage("%prog [options] [case ids ... ]")
    return parser.parse_args()

def build_query(opts, arglist):
    query = u''
    if opts.status:
        query = 'status:"'+opts.status+'" '
    if opts.assignedTo:
        query = 'assignedTo:"'+opts.assignedTo+'" ' + query
    if opts.milestone:
        query = 'fixFor:"'+opts.milestone.decode('utf-8')+'" ' + query
    if opts.project:
        query = 'project:"'+opts.project.decode('utf-8')+'" ' + query
    if opts.priority:
        query = 'priority:"'+opts.priority+'" ' + query
    if len(query) == 0 and len(arglist) > 0:
        query = ','.join(arglist)
    return query

def find_cases(query):
    fb = FogBugz(fbSettings.URL, authenticationConfigs.TOKEN)
    required_columns = "ixBug,sTitle,sStatus,sProject,sPersonAssignedTo,ixPriority,sFixFor"
    resp = fb.search(q=query,cols=required_columns,max=fbSettings.MAX_SEARCH_RESULTS)
    casePropertiesList = []
    cases = resp.cases.findAll('case')
    for case in cases:
        caseProperties = {}
        caseProperties['caseId'] = case.ixbug.string
        caseProperties['priority'] = case.ixpriority.string
        caseProperties['status'] = case.sstatus.string.encode('ascii', 'ignore')
        caseProperties['project'] = case.sproject.string.encode('ascii', 'ignore')
        caseProperties['milestone'] = case.sfixfor.string.encode('ascii', 'ignore')
        caseProperties['assignedTo'] = case.spersonassignedto.string.encode('ascii', 'ignore')
        caseProperties['title'] = case.stitle.string.encode('ascii', 'ignore')
        casePropertiesList.append(caseProperties)
    return casePropertiesList

def show_cases_info(caseList, opts):
    print "\nFound " + str(len(caseList)) + " Matching case(s):\n"
    for caseProperties in caseList:
        output = fbSettings.OUTPUT_FORMAT.format(**caseProperties)
        print output
        if opts.show_commits:
            related_branches = gitutils.find_branches_by_pattern("^  (.+FB"+caseProperties['caseId']+".+)")
            print "\n"+str(len(related_branches))+" Branch(es)"
            for branch in related_branches:
                print fbSettings.BLUE + branch + fbSettings.ENDC
            related_commits = gitutils.find_commits_by_pattern(caseProperties['caseId'])
            print "\n"+str(len(related_commits))+" Commit(s)"
            for commit in related_commits:
                sys.stdout.write(commit)
            print "\n"

def export_case_info(caseList, filename):
    f = open(filename, 'wb')
    print "\nExporting results to " + os.path.abspath(filename)
    keys = ['caseId', 'priority', 'status', 'project', 'milestone', 'assignedTo', 'title']
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(caseList)

def main(argv):
    (opts, arglist) = getargs()
    query = build_query(opts, arglist)
    caseList = find_cases(query)
    show_cases_info(caseList, opts)
    if opts.export:
        export_case_info(caseList, 'fbList_export'+str(datetime.datetime.now())+'.csv')

if __name__ == "__main__":
   main(sys.argv[1:])

