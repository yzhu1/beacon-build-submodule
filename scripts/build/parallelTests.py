#!/usr/bin/python

'''
Reads in names of tests from stdin and runs them in parallel batches on an arbitrary
set of slave machines.  Pretty much agnostic to whether you're using junit or pyunit,
Spring or Pylons, a db or no db.

  - assumes you've run something like "ant zip-test-bundle" on the machine where you're
    running this script in order to build a file named target/testbundle.zip containing
    everything the slaves need to run tests

  - (re-)creates a workspace on each slave, then copies in and unzips testbundle.zip

  - runs a task on each slave preparing its schema for testing if necessary

  - farms the tests out to the slaves in parallel batches of the size you specify
    (sending a batch of tests to be run serially on each slave cuts down the Spring
    context startup time if you're using Spring)

Example usage (runs the pk12 outcomes integration tests on three slaves):

find target/test/integration target/test/webservice -name *Test.class|xargs -i basename {} .class | \
    python conf/base/scripts/build/parallelTests.py \
    -s yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net \
    -u autobuild \
    -i ~/.ssh/id_rsa \
    -w /home/autobuild/tmp \
    -v OUTCOMES_HOME \
    -n 8

Instructions for setting up new pk12-style slaves: https://wgencontractorwiki.mc.wgenhq.net/index.php/3-12_Platform/Development/Create_a_new_Test_Slave.
'''

import sys
import time
import thread
import optparse
from threading import Lock
from subprocess import Popen, PIPE

# Constants for now, can be parameterized if we want to use this script for non-ant or db-less projects
SLAVE_SELF_SETUP_TASK = 'ant prepare-db-for-parallel-tests'
def getTaskToRunBatchOfTests(tests):
    return 'ant test-several-precompiled -Dtests=' + ','.join(['**/%s.class' % test for test in tests])

class SyncManager(object):

    def __init__(self, slaves):
        self._outputlock = Lock()
        self._failuremessages = []
        self._failuresummaries = []
        self._successmessages = []
        self._lastTimeStatusGiven = 0
        self._slaveToCurrentBatchOfTests = {}
        for slave in slaves:
            self._slaveToCurrentBatchOfTests[slave] = 'setup...'

    def makeSlaveAvailable(self, slave):
        self._slaveToCurrentBatchOfTests[slave] = None

    # Called only from this script's main thread, so no need for locking
    def getNextAvailableSlave(self, tests):
        while 1:
            for slave in self._slaveToCurrentBatchOfTests:
                if self._slaveToCurrentBatchOfTests[slave] is None:
                    self._slaveToCurrentBatchOfTests[slave] = ', '.join(tests)
                    return slave
            # If we're going to keep waiting, give cpu a break and check status
            self.sleepAndCheckStatus()

    def registerBatchOfTestsCompleted(self, slave, tests, succeeded, output):
        try:
            # Record the tests' output
            self._outputlock.acquire()
            testnames = ', '.join(tests)
            if succeeded:
                print '  (success) %s: %s PASSSED' % (slave, testnames)
                self._successmessages.append(output)
            else:
                print '  (failure) %s: FAILURE AMONG %s' % (slave, testnames)
                print output
                self._failuremessages.append(output)
                self._failuresummaries.append('%s: some tests failed in this batch: %s' % (slave, testnames))
        finally:
            self._outputlock.release()
        # Free up the slave that ran the batch
        self.makeSlaveAvailable(slave)

    def waitForAllSlavesToBeAvailable(self):
        while filter(bool, self._slaveToCurrentBatchOfTests.values()):
            # If we're going to keep waiting, give cpu a break and check status
            self.sleepAndCheckStatus()

    def letTestsFinishAndGetWhetherAnyFailed(self):
        # Let the tests finish
        self.waitForAllSlavesToBeAvailable()
        # Print their output
        print
        if self._successmessages:
            print 'PARALLEL TEST SUCCESSES:\n'
            print '\n'.join(self._successmessages)
        if self._failuremessages:
            print 'PARALLEL TEST FAILURES:\n'
            print '\n'.join(self._failuremessages)
            print
            print 'FAILURE SUMMARY:\n'
            for summary in self._failuresummaries:
                print '   ' + summary
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
        time.sleep(.1)
        # If it's been 30 seconds since last status update, report what each slave is doing
        if time.time() - self._lastTimeStatusGiven > 30:
            self._lastTimeStatusGiven = time.time()
            for slave, test in self._slaveToCurrentBatchOfTests.items():
                self.output('  (status) %s is running %s' % (slave, test or 'nothing'))

def runSubprocess(cmd, manager, failonerror=False):
    # Run cmd in a new subprocess
    manager.output('  (launching) ' + cmd)
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    # Wait for it to complete, and collect its output
    returncode = process.wait()
    output = process.stdout.read() + process.stderr.read()
    if failonerror:
        assert returncode == 0, output
    return returncode, output

def setupSlave(slave, manager, sshuser, identityfile, slaveworkspace):
    try:
        # 1. Clean out and re-create a workspace directory on the slave
        # 2. Copy testbundle.zip, which the host has built (with ant zip-test-bundle), into the slave's workspace
        # 3. Have the slave unzip testbundle.zip and run a task to get its db ready for testing
        for cmd in [
            'ssh -i %s %s@%s "rm -rf %s; mkdir %s"' % (identityfile, sshuser, slave, slaveworkspace, slaveworkspace),
            'scp -i %s target/testbundle.zip %s@%s:%s/testbundle.zip' % (identityfile, sshuser, slave, slaveworkspace),
            'ssh -i %s %s@%s "cd %s && unzip testbundle.zip > /dev/null && %s"' % (identityfile, sshuser, slave, slaveworkspace, SLAVE_SELF_SETUP_TASK)
            ]:
            runSubprocess(cmd, manager, failonerror=True)
        manager.output('  (ready) finished setting up %s' % slave)
        manager.makeSlaveAvailable(slave)
    except Exception, e:
        print e
        thread.interrupt_main()

def runBatchOfTests(tests, slave, manager, sshuser, identityfile, slaveworkspace, apphomeenvvar):
    try:
        cmd = 'ssh -i %s %s@%s "cd %s && export %s=%s && %s"' % \
                     (identityfile,
                         sshuser,
                            slave,
                                   slaveworkspace,
                                                apphomeenvvar,
                                                   slaveworkspace,
                                                         getTaskToRunBatchOfTests(tests))
        returncode, output = runSubprocess(cmd, manager)
        output = '<ran on %s> ' % slave + output
        manager.registerBatchOfTestsCompleted(slave, tests, succeeded=(returncode==0), output=output)
    except Exception, e:
        manager.registerBatchOfTestsCompleted(slave, tests, succeeded=False, output=repr(e))

def runAllTests(slaves, tests, sshuser, identityfile, slaveworkspace, apphomeenvvar, testsperbatch):
    # Do setup on each slave
    manager = SyncManager(slaves)
    for slave in slaves:
        thread.start_new_thread(setupSlave, (slave, manager, sshuser, identityfile, slaveworkspace))
    manager.waitForAllSlavesToBeAvailable()
    # Farm out the tests in batches until they're all gone
    while tests:
        batch = []
        while tests and len(batch) < testsperbatch:
            batch.append(tests.pop())
        slave = manager.getNextAvailableSlave(batch)
        thread.start_new_thread(runBatchOfTests, (batch, slave, manager, sshuser, identityfile, slaveworkspace, apphomeenvvar))
    # Report the overall exit status
    somefailures = manager.letTestsFinishAndGetWhetherAnyFailed()
    if somefailures:
        return 1
    else:
        return 0

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option('-s', dest='slaves', help='comma-separated list of slaves to run tests on')
    parser.add_option('-u', dest='sshuser', help='user to ssh to slaves as')
    parser.add_option('-i', dest='identityfile', help='ssh identity file')
    parser.add_option('-w', dest='slaveworkspace', help='remote workspace directory to run tests in')
    parser.add_option('-v', dest='apphomeenvvar', help='e.g., THREETWELVE_HOME')
    parser.add_option('-n', dest='testsperbatch', help='number of tests to delegate to each slave at a time')

    (options, args) = parser.parse_args()
    assert not args, 'got unexpected command-line arguments: %r' % args
    assert options.slaves, 'please provide a comma-separated list of slaves'
    assert options.sshuser, 'please provide a user to ssh to the slaves as'
    assert options.identityfile, 'please provide an ssh identity file'
    assert options.slaveworkspace, 'please provide a remote directory where tests should be run'
    assert options.apphomeenvvar, 'please provide the name of the application home dir environment variable, e.g., THREETWELVE_HOME'
    assert options.testsperbatch, 'please provide the number of tests to delegate to each slave at a time'

    slaves = options.slaves.strip().split(',')
    sshuser = options.sshuser.strip()
    identityfile = options.identityfile.strip()
    slaveworkspace = options.slaveworkspace.strip()
    apphomeenvvar = options.apphomeenvvar.strip()
    testsperbatch = int(options.testsperbatch.strip())

    # Get names of tests to run from stdin
    tests = map(str.strip, sys.stdin.readlines())
    numtestclasses = len(tests)
    print 'test classes to run: %i' % numtestclasses
    print 'available slaves: %r' % slaves

    exitstatus = runAllTests(slaves, tests, sshuser, identityfile, slaveworkspace, apphomeenvvar, testsperbatch)
    print 'ran %i test classes' % numtestclasses
    sys.exit(exitstatus)
