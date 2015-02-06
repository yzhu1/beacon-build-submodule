#!/usr/bin/python
import sys
from fogbugz import FogBugz
import optparse
import config, constants
import pickle
import os
import csv
import datetime
import requests
import getpass
import xml.etree.ElementTree as ET

def getargs():
    parser = optparse.OptionParser()
    parser.add_option("-a", "--assignedTo", dest="assignedTo",action="store",help="assigned to specified person")
    parser.add_option("-m", "--milestone", dest="milestone",action="store",help="specified milestone")
    parser.add_option("-t", "--team", dest="project",action="store",help="specified project")
    parser.add_option("-p", "--priority", dest="priority",action="store",help="specified priority")
    parser.add_option("-s", "--status", dest="status",action="store",help="specified status")
    parser.add_option("-f", "--filter", dest="filter",action="store",help="apply the specified filter")
    parser.add_option("-e", "--export",action="store_true", dest="export",help="exports results to csv")
    parser.add_option("--edit", action="store", dest="editMessage", help="edit cases")
    parser.add_option("--tags", action="store", dest="tags", help="comma separated list of tags")
    parser.add_option("--title", action="store", dest="title", help="title of the bug")
    parser.add_option("--username-environment-variable", action="store", dest="username_environment_variable", help="name of environment variable containing username")
    parser.add_option("--password-environment-variable", action="store", dest="password_environment_variable", help="name of environment variable containing password")
    parser.set_description('If the --edit command is provided, the --assignedTo, --milestone, --team, --priority, --status, --title and --tags options are used in updating the case. Otherwise, these options are included in the search .If you don\'t specify any of the options, then a fogbugz search will be performed based on whatever argument you provide according to the search syntax here: http://help.fogcreek.com/7480/search-syntax-and-the-search-axis?se_found=1. If no arguments are provided, then the script will display bugs based on your currently active filter. Max number of bugs which can be listed have been limited to 999 but this can be changed in config.py')
    parser.set_usage("%prog [options] [case ids ... ]")
    return parser.parse_args()

def build_query(opts, arglist):
    query = u''
    if opts.editMessage is None:
        #if not in edit mode and extra options are provided, use them in the search
        if opts.status:
            query = constants.STATUS + ':"' + opts.status + '" '
        if opts.assignedTo:
            query = constants.ASSIGNED_TO + ':"' + opts.assignedTo + '" ' + query
        if opts.milestone:
            query = constants.FIX_FOR + ':"'+opts.milestone.decode('utf-8') + '" ' + query
        if opts.project:
            query = constants.PROJECT + ':"'+opts.project.decode('utf-8') + '" ' + query
        if opts.priority:
            query = constants.PRIORITY + ':"'+opts.priority+'" ' + query

    query += ' '.join(arglist)
    return query

def addBeaconReleaseProperties(case, caseProperties):
    events = case.findAll('event')
    latestReleaseEvent = getLatestBeaconReleaseEvent(events)
    if latestReleaseEvent :
        caseProperties[constants.RELEASE_INFO] = latestReleaseEvent.find('s').string

def find_cases(fb, query, opts):
    required_columns = "ixBug,sTitle,sStatus,sProject,sPersonAssignedTo,ixPriority,sFixFor"
    resp = fb.search(q=query,cols=required_columns,max=config.MAX_SEARCH_RESULTS)
    casePropertiesList = []
    cases = resp.cases.findAll('case')
    if len(cases) > 0:
        if not opts.export:
            header = {}
            header[constants.CASE] = 'CASE'.center(len(config.URL)+11)
            header[constants.PRIORITY] = ' '
            header[constants.STATUS] = 'STATUS'.center(20)
            header[constants.PROJECT] = 'TEAM'.center(27)
            header[constants.MILESTONE] = 'MILESTONE'.center(20)
            header[constants.ASSIGNED_TO] = 'ASSIGNED TO'.center(13)
            header[constants.TITLE] = 'TITLE'.center(50)
            casePropertiesList.append(header)
    for case in cases:
        caseProperties = {}
        caseProperties[constants.CASE] = case.ixbug.string if opts.editMessage is not None else getFixedLengthString(config.URL + "?" + case.ixbug.string, len(config.URL)+11, True)
        caseProperties[constants.PRIORITY] = case.ixpriority.string
        caseProperties[constants.STATUS] = getFixedLengthString(case.sstatus.string.encode('utf-8'), 20, opts.export)
        caseProperties[constants.PROJECT] = getFixedLengthString(case.sproject.string.encode('ascii', 'ignore'), 27, opts.export)
        caseProperties[constants.MILESTONE] = getFixedLengthString(case.sfixfor.string.encode('utf-8'),20, opts.export)
        caseProperties[constants.ASSIGNED_TO] = getFixedLengthString(case.spersonassignedto.string.encode('utf-8'), 13, opts.export)
        caseProperties[constants.TITLE] = getFixedLengthString(case.stitle.string.encode('utf-8'), 50, opts.export)
        casePropertiesList.append(caseProperties)
    return casePropertiesList

def edit_cases(fb, caseIdList, opts):
    arguments = {}
    if opts.status:
        arguments['ixStatus'] = getStatusCode(fb, opts.status)
    if opts.assignedTo:
        arguments['ixPersonAssignedTo'] = getPersonCode(fb, opts.assignedTo)
    if opts.milestone:
        arguments['ixFixFor'] = getFixForCode(opts.milestone)
    if opts.project:
        arguments['ixProject'] = getProjectCode(fb, opts.project)
    if opts.priority:
        arguments['ixPriority'] = opts.priority
    if opts.title:
        arguments[constants.TITLE] = opts.title
    if opts.tags:
        arguments[constants.TAGS] = opts.tags
    confirm = raw_input("This will modify " + str(len(caseIdList)) + " case(s) with the attributes: " + str(arguments) + "! Press Y to continue :")
    if (confirm.lower() != 'y'):
        print "Aborted"
        return
    for caseId in caseIdList:
        fb.edit(ixbug=caseId, sEvent=opts.editMessage, **arguments)


def getAvailableColumns():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(columns)

def printHLine():
    print '-' * getAvailableColumns() + "\r"

def getFixedLengthString(data, length, noEllipses):
    if len(data) > length and not noEllipses:
        fixedLengthData = (data[:length-2] + '..')
    elif len(data) < length:
        fixedLengthData = data.ljust(length)
    else:
        fixedLengthData = data
    return fixedLengthData

def checkAndAddEllipsesToResultRow(data):
    noFormattingStr = data.replace(config.BLUE,"").replace(config.GREEN,"").replace(config.YELLOW,"").replace(config.RED,"").replace(config.ITALIC,"").replace(config.UNDERLINE,"").replace(config.MAGENTA,"").replace(config.ENDC,"")
    if len(noFormattingStr) > getAvailableColumns():
        return (noFormattingStr[:getAvailableColumns()-2] + '..')
    return data


def show_cases_info(caseList, opts):
    print "Found " + str(len(caseList)) + " Matching case(s):"
    printHLine()
    for caseProperties in caseList:
        print checkAndAddEllipsesToResultRow(config.BUG_INFO_FORMAT.format(**caseProperties)) + config.ENDC
        printHLine()

def export_case_info(caseList, filename):
    f = open(filename, 'wb')
    print "Exporting results to " + config.YELLOW + os.path.abspath(filename) + config.ENDC
    keys = [constants.CASE, constants.PRIORITY, constants.STATUS, constants.PROJECT, constants.MILESTONE, constants.ASSIGNED_TO, constants.TITLE]

    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writer.writerow(keys)
    dict_writer.writerows(caseList)

def setFilter(fb, filterString):
    resp = fb.listFilters()
    filters = resp.filters.findAll('filter')
    matchingFilter = ''
    for filter in filters:
        if filterString == filter.string or filterString == filter['sfilter']:
            print config.BLUE + "Applying new filter: " + filter['sfilter'] + " " + filter.string + config.ENDC
            matchingFilter = filter['sfilter']
            break
    if len(matchingFilter) > 0:
        fb.setCurrentFilter(sFilter=matchingFilter)
    else:
        print config.RED + "No filter found for: " + filterString + config.ENDC
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

def getProjectCode(fb, projectNameOrCode,
                 sort_by=('ixProject', 'ixArea')):
    resp = fb.listProjects()
    projects = resp.projects.findAll('project')
    for project in projects:
        if projectNameOrCode == project.sproject.string or projectNameOrCode == project.ixproject.string:
            print "Team code found: " + (project.ixproject.string)
            return project.ixproject.string
        if projectNameOrCode.lower() in project.sproject.string.lower():
            print  project.sproject.string + " - " + (project.ixproject.string)
    return getProjectCode(fb, raw_input("Please select valid team name or code: "))

def getPersonCode(fb, sEmail=None):
    if sEmail:
        res = fb.viewPerson(sEmail=sEmail)
    else:
        raise ValueError('Must supply email')
    if res.people.person == None:
        return getPersonCode(fb, raw_input("Please provide valid email for person being assigned to: "))
    return res.people.person.ixperson.string

def getStatusCode(fb, statusNameOrCode, sort_by=('ixCategory', 'iOrder')):
    resp = fb.listStatuses()
    statuses = resp.statuses.findAll('status')
    for status in statuses:
        if statusNameOrCode == status.sstatus.string or statusNameOrCode == status.ixstatus.string:
            print "Status code found: " + (status.ixstatus.string)
            return status.ixstatus.string
        if statusNameOrCode.lower() in status.sstatus.string.lower():
            print  status.sstatus.string + " - " + (status.ixstatus.string)
    return getStatusCode(fb, raw_input("Please select valid status name or code: "))

def getFixForCode(fb, fixForNameOrCode, sort_by=('ixCategory', 'iOrder')):
    resp = fb.listFixFors()
    fixFors = resp.fixfors.findAll('fixfor')
    for fixFor in fixFors:
        if fixForNameOrCode == fixFor.sfixfor.string or fixForNameOrCode == fixFor.ixfixfor.string:
            print "Milestone code found: " + (fixFor.ixfixfor.string)
            return fixFor.ixfixfor.string
        if fixForNameOrCode.lower() in fixFor.sfixfor.string.lower():
            print  fixFor.sfixfor.string + " - " + (fixFor.ixfixfor.string)
    return getFixForCode(fb, raw_input("Please select valid milestone name or code: "))

def getAuthToken(opts):
    if opts.username_environment_variable and None != os.environ.get(opts.username_environment_variable):
        email = os.environ.get(opts.username_environment_variable)
    else:
        email = raw_input("Username: ")

    if opts.password_environment_variable and None != os.environ.get(opts.password_environment_variable):
        password = os.environ.get(opts.password_environment_variable)
    else:
        password = getpass.getpass()

    params = {'cmd':'logon'}
    params['email'] = email
    params['password'] = password
    response = requests.post(config.AUTH_URL, params)
    root = ET.fromstring(response.text)
    return root.findall('token')[0].text

def main(argv):
    (opts, arglist) = getargs()
    tokenFilename = os.path.join(os.path.dirname(sys.argv[0]), "token.p")
    if os.path.exists(tokenFilename):
        authToken = pickle.load(open(tokenFilename,"rb"))
    else:
        authToken = getAuthToken(opts)
        pickle.dump(authToken, open(tokenFilename,"wb"))
    try:
        fb = FogBugz(config.URL, authToken)
        currentFilter = getCurrentFilter(fb)
    except:
        print "Could not authenticate" + str(authToken)
        os.remove(tokenFilename)
        main(argv)
    if currentFilter and len(argv) == 0:
        print config.YELLOW + "Active filter: " + currentFilter.string + config.ENDC
    if opts.filter:
        setFilter(fb, opts.filter)
    query = build_query(opts, arglist)
    try:
        caseList = find_cases(fb, query, opts)
    except (KeyboardInterrupt, SystemExit):
        print " Aborted."
    except Exception, err:
        print "Exception occured: " + str(err)
        return
    if opts.export or opts.editMessage is not None:
        fileName = 'fb_export'+str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))+'.csv'
        export_case_info(caseList, fileName)
    try:
        if opts.editMessage is not None:
            caseIdList = [case[constants.CASE] for case in caseList[1:]]
            print 'Matching Cases:' + (','.join(caseIdList))
            edit_cases(fb, caseIdList, opts)
            return
        else:
            show_cases_info(caseList, opts)
    except (KeyboardInterrupt, SystemExit):
        print " Aborted."

if __name__ == "__main__":
   main(sys.argv[1:])

