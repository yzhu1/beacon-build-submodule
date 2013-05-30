#!/usr/bin/python

import urllib
import urllib2
import optparse
import pdb
import types

class subdomain(object):
    production = "prd.som.mclassdc.net"
    preprod    = "pre.som.mclassdc.net"
    fqa        = "tt.wgenhq.net"
    cqa        = "tt.wgenhq.net"

class hostprefix(object):
    datacenter_format = "tt%swebapp"
    @classmethod
    def production(cls, appname):
        return cls.datacenter_format % appname
    @classmethod
    def preprod(cls, appname):
        return cls.production(appname)
    @classmethod
    def fqa(cls, appname):
        return "yet" if  "webassess" != appname else "yad"
    @classmethod
    def cqa(cls, appname):
        return cls.fqa(appname)

toggle_format = "http://{server}/{app}/liveops/webservices/feature/toggle?{query}"
query_format  = "http://{server}/{app}/liveops/webservices/feature/isEnabled?{query}";
lower_case_booleans = ['true','false']

# Configuration code
def hostlist(stem,subdomain, list_or_count):
    if types.IntType == type(list_or_count):
        number_list = range(1, 1+list_or_count)
    else:
        number_list = list_or_count
    fmt = "{stem}{hostidx}.{subdomain}"
    return [ fmt.format(stem=stem,subdomain=subdomain,hostidx=x) for x in number_list ]

def create_dashboard(appname,fqa_hosts,cqa_hosts,preprod_hosts,production_hosts):
    return  {
        'fqa' : hostlist(hostprefix.fqa(appname),subdomain.fqa, fqa_hosts),
        'cqa': hostlist(hostprefix.fqa(appname),subdomain.cqa, cqa_hosts),
        'preprod':hostlist(hostprefix.preprod(appname),subdomain.preprod, preprod_hosts),
        'production' : hostlist(hostprefix.production(appname),subdomain.production, production_hosts),
    }

feature_groups = {
    'rpt-out' : ['StudentStandardsRPT']
}

env_dashboard = {
    "outcomes" : create_dashboard("outcomes", [127], [136,137], 4, 4),
    "oib" : create_dashboard("oib",[126], [132,133], 4, 4,),
    "oa" : create_dashboard("webassess",[120,134], [118,137], 2, 2),
}

# Main workhorse functions
def toggle(hostname, appname, featurename, state):
    p = {'featureSetterName' : featurename, 'value' : state }
    print "Setting %s feature for host %s " % (featurename, hostname)
    url = toggle_format.format(server=hostname, app=appname, query=urllib.urlencode(p))
    urllib2.urlopen(url).close()
    query(hostname, appname, featurename)

def query(hostname, appname, featurename):
    p = { 'feature' : featurename }
    url = query_format.format(server=hostname, app=appname ,query=urllib.urlencode(p))
    output = urllib2.urlopen(url).readlines()
    if not output:
        response = "no output received"
    elif len(output) > 1:
        response = "implausible output (too many lines)"
    elif not output[0] in lower_case_booleans:
        response = "unknown response '%s'" % output[0]
    else:
        response = output[0]
    print "Feature {f} on {host}: {response}".format(f=featurename, host=hostname, response=response)

# Argument parse and validate
def getargs():
    parser = optparse.OptionParser()
    parser.add_option("-d", "--debug", action="store_true", dest="debug",
                      help="step through program in pdb")
    parser.add_option("-q", "--query", action="store_true", dest="query",
                      help="get the currently set value for this toggle")
    parser.add_option("-t", "--toggle", action="store", dest="toggle_value",
                      help="set the value for this toggle to VALUE", metavar="VALUE")
    parser.set_description(
        "Toggle features on and off in any environment you have network access to.")
    parser.set_usage("%prog [-q | -t value] environment application feature")

    (opts, args) = parser.parse_args()
    if (opts.query and opts.toggle_value is not None) or (opts.toggle_value is None and not opts.query):
        parser.error("exactly one of -q or -t is required")
    # validate toggle value
    if opts.toggle_value is not None and not opts.toggle_value in lower_case_booleans:
        parser.error("VALUE must be either true or false")
    if len(args) != 3:
        parser.error("incorrect number of arguments")
    # validate args
    (env, app, feature) = args
    if not app in env_dashboard:
        parser.error(
            "'application' argument must be one of the configured applications: " +
            ", ".join(env_dashboard.keys())
        )
    if not env in env_dashboard[app]:
        parser.error(
            "application '%s' does not have configuration for environment '%s' (supported: %s)"
            % (app, env, ", ".join(env_dashboard[app].keys()))
        )
    return (opts, args)

# Main function (dirt simple)
def main(opts,args):
    (env, app, feature) = args
    if feature in feature_groups:
        feature_list = feature_groups[feature]
    else:
        feature_list = [feature]
    host_list = env_dashboard[app][env]
    if opts.query:
        for host in host_list:
            for feature in feature_list:
                query(host, app, feature)
    else:
        for host in host_list:
            for feature in feature_list:
                toggle(host, app, feature, opts.toggle_value)

# TOP-LEVEL EXECUTED CODE
if '__main__' == __name__:
    (opts,argv) = getargs()
    if opts.debug: # set with -d on command-line
        pdb.runcall(main, opts, argv)
    else:
        main(opts, argv)
