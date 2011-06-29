#!/usr/bin/python

'''
Reads in names of tests from stdin and runs them in parallel batches on an arbitrary
set of testdog machines.  Pretty much agnostic to whether you're using junit or pyunit,
Spring or Pylons, a db or no db.

  - optionally runs a task on each testdog preparing its schema for testing

  - farms the tests out to the testdogs in parallel batches of the size you specify
    (sending a batch of tests to be run serially on each testdog cuts down the Spring
    context startup time if you're using Spring)

Example usage (runs the pk12 outcomes integration tests on three testdogs):

find target/test/integration target/test/webservice -name *Test.class|xargs -i basename {} .class | \
    python conf/base/scripts/build/parallelTests.py \
    -s yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net \
    -v OUTCOMES_HOME \
    -n 8

Instructions for setting up new pk12-style testdogs: https://wgencontractorwiki.mc.wgenhq.net/index.php/3-12_Platform/Development/Create_a_new_Testdog.
'''

import os
import sys
import time
import thread
import random
import string
import optparse
from threading import Lock
from subprocess import Popen, PIPE

# Constant for now, can be parameterized if we want to use this script for non-ant or db-less projects
TESTDOG_DB_UPDATE_TASK = 'prepare-db-for-parallel-tests'

# Implemented here for ant
def getTaskToRunBatchOfTests(tests):
    return '/opt/wgen-3p/ant-1.7.0/bin/ant test-several-precompiled -Dtests=' + ','.join(['**/%s.class' % test for test in tests])

class SyncManager(object):

    def __init__(self, testdogs):
        self._outputlock = Lock()
        self._failuremessages = []
        self._successmessages = []
        self._lastTimeStatusGiven = 0
        self._testdogToCurrentBatchOfTests = {}
        for testdog in testdogs:
            self._testdogToCurrentBatchOfTests[testdog] = 'setup...'

    def makeTestdogAvailable(self, testdog):
        self._testdogToCurrentBatchOfTests[testdog] = None

    # Called only from this script's main thread, so no need for locking
    def getNextAvailableTestdog(self, tests):
        while 1:
            for testdog in self._testdogToCurrentBatchOfTests:
                if self._testdogToCurrentBatchOfTests[testdog] is None:
                    self._testdogToCurrentBatchOfTests[testdog] = ', '.join(tests)
                    return testdog
            # If we're going to keep waiting, give cpu a break and check status
            self.sleepAndCheckStatus()

    def registerBatchOfTestsCompleted(self, testdog, tests, succeeded, output):
        try:
            # Record the tests' output
            self._outputlock.acquire()
            testnames = ', '.join(tests)
            if succeeded:
                print '  (success) %s: %s PASSSED' % (testdog, testnames)
                self._successmessages.append(output)
            else:
                print output
                self._failuremessages.append(output)
        finally:
            self._outputlock.release()
        # Free up the testdog that ran the batch
        self.makeTestdogAvailable(testdog)

    def waitForAllTestdogsToBeAvailable(self):
        while filter(bool, self._testdogToCurrentBatchOfTests.values()):
            # If we're going to keep waiting, give cpu a break and check status
            self.sleepAndCheckStatus()

    def letTestsFinishAndGetWhetherAnyFailed(self):
        # Let the tests finish
        self.waitForAllTestdogsToBeAvailable()
        # Print their output
        print
        if self._successmessages:
            print 'PARALLEL TEST SUCCESSES:\n'
            print '\n'.join(self._successmessages)
        if self._failuremessages:
            print 'PARALLEL TEST FAILURES:\n'
            print '\n'.join(self._failuremessages)
        print '\nPARALLEL TESTS: %i batches of tests passed and %i failed\n' % (len(self._successmessages), len(self._failuremessages))
        # Return whether any tests failed
        return self._failuremessages != []

    def output(self, message):
        # Useful because several threads' writing to stdout is no good
        try:
            self._outputlock.acquire()
            print message
        finally:
            self._outputlock.release()

    def sleepAndCheckStatus(self):
        time.sleep(.5)
        # If it's been 30 seconds since last status update, report what each testdog is doing
        if time.time() - self._lastTimeStatusGiven > 30:
            self._lastTimeStatusGiven = time.time()
            for testdog, test in self._testdogToCurrentBatchOfTests.items():
                self.output('  (status) %s is running %s' % (testdog, test or 'nothing'))

def runSubprocess(cmd, manager, failonerror=False):
    # Run cmd in a new subprocess
    manager.output('  (launching) ' + cmd)
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    # Wait for it to complete, and collect its output
    returncode = process.wait()
    stdout, stderr = process.communicate()
    output = stdout + stderr
    if failonerror:
        assert returncode == 0, output
    return returncode, output

def setupTestdog(testdog, manager, updatedb):
    try:
        if updatedb:
            runSubprocess('export ENV_PROPERTY_PREFIX=%s && /opt/wgen-3p/ant-1.7.0/bin/ant %s' % (testdog, TESTDOG_DB_UPDATE_TASK), manager, failonerror=True)
        manager.output('  (ready) finished setting up %s' % testdog)
        manager.makeTestdogAvailable(testdog)
    except Exception, e:
        print e
        thread.interrupt_main()

def runBatchOfTests(tests, testdog, manager, apphomeenvvar, runonlysmoketests):
    try:
        testlogfile = 'test.log' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        open(testlogfile, 'w') # create the file
        cmd = 'Xvfb :5 -screen 0 1024x768x24 >/dev/null 2>&1 & export DISPLAY=:5.0 && ' \
            + 'export ENV_PROPERTY_PREFIX=%s && ' % testdog \
            + 'export RUN_ONLY_SMOKE=%s && ' % ('true' if runonlysmoketests else 'false') \
            + 'export %s=. && %s ' % (apphomeenvvar, getTaskToRunBatchOfTests(tests)) \
            + '&> %s; exitstatus=\$? && tail -n 100 %s && exit \$exitstatus"' % (testlogfile, testlogfile)
        returncode, output = runSubprocess(cmd, manager)
        output = '<ran on %s> ' % testdog + output
        # Download and print the contents of test.log
        if returncode != 0:
            manager.output('tests failed on %s: %s' % (testdog, open(testlogfile, 'r').read()))
            os.remove(testlogfile)
        manager.registerBatchOfTestsCompleted(testdog, tests, succeeded=(returncode==0), output=output)
    except Exception, e:
        manager.registerBatchOfTestsCompleted(testdog, tests, succeeded=False, output=repr(e))

def runAllTests(testdogs, tests, apphomeenvvar, testsperbatch, updatedb, runonlysmoketests):
    # Do setup on each testdog
    manager = SyncManager(testdogs)
    for testdog in testdogs:
        thread.start_new_thread(setupTestdog, (testdog, manager, updatedb))
    manager.waitForAllTestdogsToBeAvailable()
    # Farm out the tests in batches until they're all gone
    while tests:
        batch = []
        while tests and len(batch) < testsperbatch:
            batch.append(tests.pop())
        testdog = manager.getNextAvailableTestdog(batch)
        thread.start_new_thread(runBatchOfTests, (batch, testdog, manager, apphomeenvvar, runonlysmoketests))
    # Report the overall exit status
    somefailures = manager.letTestsFinishAndGetWhetherAnyFailed()
    if somefailures:
        return 1
    else:
        return 0

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option('-s', dest='testdogs', help='comma-separated list of testdogs to run tests on')
    parser.add_option('-v', dest='apphomeenvvar', help='e.g., THREETWELVE_HOME')
    parser.add_option('-n', dest='testsperbatch', help='number of tests to delegate to each testdog at a time')
    parser.add_option('-d', dest='updatedb', action='store_true', help='do your testdogs\' dbs need to be updated?')
    parser.add_option('-l', dest='runonlysmoketests', default=True, action='store_false', help='run slow tests')

    (options, args) = parser.parse_args()
    assert not args, 'got unexpected command-line arguments: %r' % args
    assert options.testdogs, 'please provide a comma-separated list of testdogs'
    assert options.apphomeenvvar, 'please provide the name of the application home dir environment variable, e.g., THREETWELVE_HOME'
    assert options.testsperbatch, 'please provide the number of tests to delegate to each testdog at a time'

    testdogs = options.testdogs.strip().split(',')
    apphomeenvvar = options.apphomeenvvar.strip()
    testsperbatch = int(options.testsperbatch.strip())
    updatedb = bool(options.updatedb)
    runonlysmoketests = bool(options.runonlysmoketests)

    # Get names of tests to run from stdin
    tests = map(str.strip, sys.stdin.readlines())
    # Shuffle tests to give testdogs an even burden
    random.shuffle(tests)
    numtestclasses = len(tests)
    print 'RUNNING PARALLEL TESTS'
    print 'test classes to run: %i' % numtestclasses
    print 'available testdogs: %r' % testdogs

    exitstatus = runAllTests(testdogs, tests, apphomeenvvar, testsperbatch, updatedb, runonlysmoketests)
    print 'ran %i test classes\n' % numtestclasses
    sys.exit(exitstatus)
