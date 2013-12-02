#!/usr/bin/python
import sys
from fogbugz import FogBugz
import optparse
import fbSettings
import pickle
import os
import csv
import datetime
import requests
import getpass
import xml.etree.ElementTree as ET


def getargs():
    parser = optparse.OptionParser()
    parser.add_option("-a", "--assignedTo", dest="assignedTo",action="store",help="show only cases assigned to specified person")
    parser.add_option("-m", "--milestone", dest="milestone",action="store",help="show only cases for specified milestone")
    parser.add_option("-t", "--team", dest="project",action="store",help="show only cases for specified project")
    parser.add_option("-p", "--priority", dest="priority",action="store",help="show only cases for specified priority")
    parser.add_option("-s", "--status", dest="status",action="store",help="show only cases with the specified status")
    parser.add_option("-f", "--filter", dest="filter",action="store",help="apply the specified filter")
    parser.add_option("-r", "--release",action="store_true", dest="showReleaseInfo",help="gives additional info specific for release bugs (affects load times).")
    parser.add_option("-e", "--export",action="store_true", dest="export",help="exports results to csv")
    parser.set_description('You need to have python and pip installed in order to use this script. \nAfter that run sudo pip install fogbugz. Now you can start using the script. \n If you don\'t specify any of the options, then a fogbugz search will be performed based on whatever argument you provide which can include a space or comma separated list of bug ids. If no arguments are provided, then the script will display bugs based on your currently active filter. Max number of bugs which can be listed have been limited to 999 but this can be changed in fbSettings.py')
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

def getLatestBeaconReleaseEvent(events):
    for event in reversed(events):
        if "FIX DESCRIPTION" in event.text:
            return event

def addBeaconReleaseProperties(case, caseProperties):
    events = case.findAll('event')
    latestReleaseEvent = getLatestBeaconReleaseEvent(events)
    if latestReleaseEvent :
        beaconAttributesString = latestReleaseEvent.find('s').string
        beaconAttributesArray = beaconAttributesString.split('\n')
        defaultValue = "Not specified"
        caseProperties['release_STATUS'] = defaultValue
        caseProperties['release_MERGES'] = defaultValue
        caseProperties['release_COMMIT'] = defaultValue
        caseProperties['release_RISKS'] = defaultValue
        caseProperties['release_FIXDESCRIPTION'] = defaultValue
        caseProperties['release_BRANCH'] = defaultValue
        caseProperties['release_PROJECT'] = ""
        caseProperties['release_PROJECTS'] = ""
        for beaconAttributes in beaconAttributesArray:
            keyValueArray = beaconAttributes.split(':', 1)
            if(len(keyValueArray) == 2):
                key = keyValueArray[0].encode('ascii').replace(" ", "").replace("(S)", "")
                value = keyValueArray[1].strip().replace("\r", "")
                caseProperties["release_" + key] = value

def find_cases(fb, query, showReleaseInfo):
    required_columns = "ixBug,sTitle,sStatus,sProject,sPersonAssignedTo,ixPriority,sFixFor"
    if showReleaseInfo:
        required_columns += ",events"
    resp = fb.search(q=query,cols=required_columns,max=fbSettings.MAX_SEARCH_RESULTS)
    casePropertiesList = []
    cases = resp.cases.findAll('case')
    for case in cases:
        caseProperties = {}
        caseProperties['caseId'] = case.ixbug.string
        caseProperties['priority'] = case.ixpriority.string
        caseProperties['status'] = case.sstatus.string.encode('utf-8')
        caseProperties['project'] = case.sproject.string.encode('utf-8')
        caseProperties['milestone'] = case.sfixfor.string.encode('utf-8')
        caseProperties['assignedTo'] = case.spersonassignedto.string.encode('utf-8')
        caseProperties['title'] = case.stitle.string.encode('utf-8')
        if showReleaseInfo:
            addBeaconReleaseProperties(case, caseProperties)
        casePropertiesList.append(caseProperties)
    return casePropertiesList

def printHLine():
    rows, columns = os.popen('stty size', 'r').read().split()
    print '_' * int(columns) + "\n"

def show_cases_info(caseList, opts):
    print "Found " + str(len(caseList)) + " Matching case(s):"
    printHLine()
    for caseProperties in caseList:
        print fbSettings.BUG_INFO_FORMAT.format(**caseProperties)
        if opts.showReleaseInfo and 'release_STATUS' in caseProperties:
            print fbSettings.RELEASE_INFO_FORMAT.format(**caseProperties)
        printHLine()

def export_case_info(caseList, filename, hasReleaseInfo):
    f = open(filename, 'wb')
    print "Exporting results to " + fbSettings.YELLOW + os.path.abspath(filename) + fbSettings.ENDC
    keys = ['caseId', 'priority', 'status', 'project', 'milestone', 'assignedTo', 'title']
    if hasReleaseInfo:
        keys += ['release_STATUS', 'release_MERGES', 'release_PROJECT', 'release_RISKS', 'release_PROJECTS', 'release_FIXDESCRIPTION', 'release_BRANCH', 'release_COMMIT']

    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(caseList)

def setFilter(fb, filterString):
    resp = fb.listFilters()
    filters = resp.filters.findAll('filter')
    matchingFilter = ''
    for filter in filters:
        if filterString == filter.string or filterString == filter['sfilter']:
            print fbSettings.BLUE + "Applying new filter: " + filter['sfilter'] + " " + filter.string + fbSettings.ENDC
            matchingFilter = filter['sfilter']
            break
    if len(matchingFilter) > 0:
        fb.setCurrentFilter(sFilter=matchingFilter)
    else:
        print fbSettings.RED + "No filter found for: " + filterString + fbSettings.ENDC
        printAllFilters(fb)

def getCurrentFilter(fb):
    resp = fb.listFilters()
    filters = resp.filters.findAll('filter')
    for filter in filters:
        if filter.get('status', None) == 'current':
            return filter

def printAllFilters(fb):
    resp = fb.listFilters()
    filters = resp.filters.findAll('filter')
    print "Available filters are: "
    for filter in filters:
        print filter.string + "[" + filter['sfilter'] + "]"

def getAuthToken():
    email = raw_input("Username: ")
    password = getpass.getpass()
    params = {'cmd':'logon'}
    params['email'] = email
    params['password'] = password
    response = requests.post(fbSettings.AUTH_URL, params)
    root = ET.fromstring(response.text)
    return root.findall('token')[0].text

def main(argv):
    (opts, arglist) = getargs()
    tokenFilename = os.path.join(os.path.dirname(sys.argv[0]), "token.p")
    if os.path.exists(tokenFilename):
        authToken = pickle.load(open(tokenFilename,"rb"))
    else:
        authToken = getAuthToken()
        pickle.dump(authToken, open(tokenFilename,"wb"))
    try:
        fb = FogBugz(fbSettings.URL, authToken)
        currentFilter = getCurrentFilter(fb)
    except:
        print "Could not authenticate" + str(authToken)
        os.remove(tokenFilename)
        main(argv)
    if currentFilter and len(argv) == 0:
        print fbSettings.YELLOW + "Active filter: " + currentFilter.string + fbSettings.ENDC
    if opts.filter:
        setFilter(fb, opts.filter)
    query = build_query(opts, arglist)
    try:
        caseList = find_cases(fb, query, opts.showReleaseInfo)
    except Exception, err:
        print "No matching cases found. Exception: " + str(err)
        return
    show_cases_info(caseList, opts)
    if opts.export:
        fileName = 'fbList_export'+str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))+'.csv'
        export_case_info(caseList, fileName, opts.showReleaseInfo)

if __name__ == "__main__":
   main(sys.argv[1:])

