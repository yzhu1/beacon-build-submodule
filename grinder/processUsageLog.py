import sys
import os
import os.path
import csv
import subprocess
import math
import re
# Go through every line of the file.
# create new map of request ids
# record get /post and url
# for each new request id
# add number of select queries
# add up number of undate queries
# add up number of commits
# Processed request in X milliseconds -- record that 
# record processed time. update statistics for this type of request.
# in the map Q'd by request
# update general statistics
### Metrics ###
class MetricStats:
    "Basic class for maintaining statistics on a given metric."
    def __init__(self,name):
        self.min = sys.maxint
        self.max = 0
        self.total = 0
        self.count = 0
        self.sigma = 0
        self.name = name
        self.raw = []
        self.finished = False

    def finish(self):
        "Compute sigma, average, etc. for metric."
        if self.finished:
            return
        self.finished = True
        self.raw.sort()
        avg = self.getAvg()
        if self.raw:
            self.sigma = math.sqrt(sum(map(lambda x:(x-avg)**2, self.raw))/len(self.raw))
        else:
            self.sigma = 0

    def addValue(self, value):
        "Add a data point for this metric."
        self.min = min(self.min, value)
        self.max = max(self.max, value)
        self.total = self.total + value
        self.count = self.count + 1
        self.raw.append(value)
        self.finished = False

    def getAvg(self):
        "Return average value (so far)."
        if (self.count == 0):
            return 0
        return int(round(self.total/float(self.count)))

    def getAtPercent(self, pct):
        "Return value at pct percent of the results."
        if (self.count == 0):
            return 0
        self.finish()  # compute values and sort if not yet done
        return self.raw[ int((pct*self.count)/100.0) ]

    def getMedian(self):
        return self.getAtPercent(50)

    def get90(self):
        return self.getAtPercent(90)

    def getMin(self):
        if (self.min == sys.maxint):
            return 0
        return self.min

    def addToDict(self, d):
        d[self.name+"Min"] = self.getMin()
        d[self.name+"Max"] = self.max
        d[self.name+"Avg"] = self.getAvg()
        d[self.name+"Tot"] = self.total
        d[self.name+"Med"] = self.getMedian()
        d[self.name+"90"] = self.get90()
        d[self.name+"Sigma"] = self.sigma

    def getColumnNames(self):
        d = [
            self.name+"Min",
            self.name+"Max",
            self.name+"Avg",
            self.name+"Tot",
            self.name+"Med",
            self.name+"90",
            self.name+"Sigma"
            ]
        return d

    def __str__(self):
        return ",".join( map(str, self.getAvg(), self.getMin(), self.max, self.total, self.count ) )

### Request stats for a test (or group of tests) ###
class RequestStats:
    "Statistics for a given test or group of tests."
    def __init__(self, reqId, name):
        self.statMap = {
            'elapsed' : 0,
            'numberOfSelects' :0,
            'numberOfUpdates' : 0,
	    'numberOfCommits' :0,
	    'startTime' :0,
            'endtime' : 0
            }
        self.name = name
	self.reqId = reqId
        self.count = 0
        self.failures = 0

    def processMap( self, m ):
        self.count = self.count + 1
	select =0
	update = 0
        commit = 0
        milliseconds =0
        for (key, value) in m.items():
	   if key == 'message':
		if re.search('select', value):
		    select+=1
                elif re.search('update', value):
                    update+=1
                elif re.match('commit', value):
                    commit+=1
		elif re.search('Processed request in ', value):
		    wordsInValue = re.split(' ', value)
                    milliseconds = int(wordsInValue[3])
                
        self.statMap["numberOfCommits"]=self.statMap["numberOfCommits"]+commit
	self.statMap["numberOfUpdates"]=self.statMap["numberOfUpdates"]+update
	self.statMap["numberOfSelects"]=self.statMap["numberOfSelects"]+select
	self.statMap["elapsed"]=self.statMap["elapsed"]+milliseconds


 

    def getColumnNames(self):
        d = [ 'name', 'count', 'reqId']
        for v in self.statMap.values():
            d += v.getColumnNames()
        return d
    def getTotalsIdentifierName(self):
	return self.name

class TotalStats:
    "Statistics for a given test or group of tests."
    def __init__(self, name):
        self.statMap = {
            'elapsed' : MetricStats('elapsed'),
            'numberOfSelects' : MetricStats('numberOfSelects'),
            'numberOfUpdates' : MetricStats('numberOfUpdates'),
	    'numberOfCommits' : MetricStats('numberOfCommits'),
	    'startTime' : MetricStats('startTime'),
            'endtime' : MetricStats('endTime')
            }
        self.name = name
        self.count = 0
        self.failures = 0

    def processMap( self, m ):
        self.count = self.count + 1	
        for (key, value) in m.items():
            if self.statMap.has_key(key):
              	self.statMap[key].addValue(int(value))

    def makeMap( self ):
        d = { 'name' : self.name, 'count' : self.count }
        for v in self.statMap.values():
            v.addToDict(d)
        return d

    def getColumnNames(self):
        d = [ 'name', 'count']
        for v in self.statMap.values():
            d += v.getColumnNames()
        return d
 
def initialize():
    global testDict
    global totals
    testDict = {}
    totals = TotalStats("TOTAL")

def processFile( f ):
    global totalNumberOfRecords
    global totalNumberOfErrors
    numberOfRecords = 0
    numberOfErrors = 0
    requestDict = {}
    fields=['first','timeStamp','type','requestId','message']
    rdr = csv.DictReader(f,fieldnames=fields, delimiter='|')
    minTime = 0  # no maxint for longs? weird.
    maxTime = 0
    for line in rdr:
        tm = line['timeStamp']
        requestId = line['requestId']
	message = line['message']
        print line
        if requestId != None  and requestId != '':
	        if not requestDict.has_key(requestId):     
		    requestOutput = re.split(" ",message)
		    if requestOutput[0] == 'GET' or requestOutput[0] == 'POST':
		    	requestName = requestOutput[1]
	            else :
                        requestName = 'unkown request'
		    #figure out how to pop unkown requests off the requestDict
		    requestDict[requestId] = RequestStats(requestId, requestName)
	        requestDict[requestId].processMap( line )

	if re.search('Processed request', message):
	    print "PROCESSED ADDING TO TOTALS : " + message
	    requestStat = requestDict[requestId]
            totalsId = requestStat.getTotalsIdentifierName()
	    if not testDict.has_key(totalsId):  
		testDict[totalsId]= TotalStats(totalsId)
	    testDict[totalsId].processMap( requestStat.statMap )
	    totals.processMap(requestStat.statMap)
	    del requestDict[requestId]
        # do we need to update more totals here
    if not quiet:
        print "Sorting data..."
    elapsedms = maxTime-minTime
    if not quiet:
        print "Count:   %d" % totals.count
   
    totalNumberOfRecords += numberOfRecords
    totalNumberOfErrors += numberOfErrors
    #print_failure_rate(numberOfRecords, numberOfErrors, f.name)

def writeSummary( f ):
    fieldnames = TotalStats("shell").getColumnNames();
    wdr = csv.DictWriter(f, fieldnames)
    fnmap = {}
    for field in fieldnames:
        fnmap[field] = field
    wdr.writerow( fnmap )
    tdkeys = testDict.keys()
    tdkeys.sort()
    for key in tdkeys:
        v = testDict[key]
        wdr.writerow(v.makeMap())
    wdr.writerow(totals.makeMap())

def writeData( aspect, fn, testList ):
    f = open(fn,'w')
    f.write("# Gnuplot data for "+aspect+" aspect.\n" );
    for (name, data) in testList:
        f.write('%f "%s" %f %f %f %f %f %d\n' % 
                (data.order, name, 
                 data.statMap[aspect].getAvg(),
                 data.statMap[aspect].getAtPercent(10),
                 data.statMap[aspect].max,
                 data.statMap[aspect].getMin(),
                 data.statMap[aspect].getAtPercent(90),
                 data.getSuccessCount()))
    f.close()

def writeChart( title, aspect, unit, base, dir, testList, yMax=None ):
    dfn = os.path.join(dir,base + "_"+aspect.lower()+".dat")
    showCount = aspect == "elapsed"
    if not quiet:
        print "Writing %s" % dfn
    writeData( aspect, dfn, testList )
    fn = os.path.join(dir,base + "_"+aspect.lower()+".gnu")
    if not quiet:
        print "Writing %s" % fn
    f = open(fn,'w')
    f.write( "set terminal png nocrop enhanced font arial 10 size %d,650\n" % max(600,len(testList)*30) )
    outfile = base + "_" + aspect.lower()
    if yMax:
        outfile = "%s_%ds_zoom" % (outfile, yMax)
    f.write( "set output '%s.png'\n" % os.path.join( dir, (outfile)) )
    f.write( "set key off\n" )
    f.write( "set xrange [-0.5:%f]\n" % (len(testList) + 0.5) )
    f.write( "set style fill solid 0.5 border\n" )
    f.write( "set xtics out rotate by 90  (" )
    f.write( ",".join( [ '"%s" %i' % (name.replace('%', 'X'), data.order) for (name, data) in testList ] ) )
    f.write( ")\n" )
    f.write( 'set title "%s"\n' % title )
    f.write( 'set boxwidth 1\n' )
    f.write( 'set ylabel "%s"\n' % unit )
    if yMax:
        f.write( "set yrange [0:%d]\n" % (yMax*1000) )
    if showCount:
        f.write( 'set y2label "samples taken (x)"\n' )
        f.write( 'set y2tics out\n' )
        maxCount = max( map( lambda(_,dat): dat.getSuccessCount(), testList ) )
        f.write( "set y2range [0:%d]\n" % maxCount )
    f.write( "plot '%s' using 1:4:5:6:7 with candlesticks" % dfn )
    f.write( ", '%s' using 1:3 with points" %dfn )
    if showCount:
        f.write( ", '%s' using 8 with points axis x1y2" % dfn )
    f.write("\n" )
    f.close()
    global gnuplotPath
    if (gnuplotPath):
        subprocess.call([gnuplotPath,fn])
    os.remove(dfn)
    os.remove(fn)


def parse_results(fname):
    initialize()
    (dir, bn) = os.path.split( fname )
    (base, _) = os.path.splitext( bn )
    print "Processing " + fname
    processFile( open( fname ) )

    # fix paths by name, not test name
    testList = [(x.name, x) for x in testDict.values()]
    testList.sort( key=lambda (x,y):x )
    idx = 0
    for (_,data) in testList:
        data.order = idx
        idx = idx + 1

    outliers = []
   # for (_,data) in testList:
   #     outliers = outliers + data.getOutliers( 'elapsed', open(fname) )
   # olname = os.path.join(dir, base + "_outliers.csv" )
    outname = os.path.join(dir, base + "_summary.csv")
    if not quiet:
        print "Producing " + outname
    writeSummary(open(outname, 'w'))
   # if not quiet:
   #     print "Producing " + olname
    rdr = csv.reader( open( fname ) )
    samplesFieldNames = rdr.next()
    #writeOutliers(open(olname, 'w'), outliers, samplesFieldNames)
 

global quiet
quiet = False
global totalNumberOfRecords
global totalNumberOfErrors
totalNumberOfRecords = 0
totalNumberOfErrors = 0
if __name__ == "__main__":

    if '--help' in sys.argv:
        print 'Usage:'
        print 'processUsageLog.py <FILE>'
        print '  If FILE is supplied it will be parsed'
        sys.exit(2)
    if '-q'  in sys.argv:
        quiet = True
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    

    parse_results(fname)
