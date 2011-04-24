#!/usr/bin/python

'''
Runs tests, their names read from stdin, in parallel on an arbitrary set of slaves.

  - assumes you have run ant zip-test-bundle on the master in order to build a file
    called target/testbundle.zip containing everything the slaves need to run tests
  - (re-)creates a workspace on each slave
  - copies to and unzips testbundle.zip on each slave
  - runs ant prepare-db-for-parallel-tests, a task defining whatever pre-test schema
    setup is needed, on each slave
  - farms the tests out to the slaves in batches of the size you specify

Example usage (using localhost as the only slave):

find target/test/unit|grep Test.class|xargs -i basename {} .class | \
    python conf/base/scripts/build/parallelTests.py \
    -s localhost -u $USER -w /tmp/test -i ~/.ssh/id_rsa -v OUTCOMES_HOME -n 4

Instructions for setting up slaves are found here:
  https://wgencontractorwiki.mc.wgenhq.net/index.php/3-12_Platform/Development/Create_a_new_Test_Slave

'''

import sys
import time
import thread
import optparse
import threading
import subprocess

class SyncManager(object):

    def __init__(self, slaves):
        self._outputlock = threading.Lock()
        self._failuremessages = []
        self._failuresummaries = []
        self._successmessages = []
        self._lastStatusTime = 0
        self._slaveToCurrentTest = {}
        for slave in slaves:
            self._slaveToCurrentTest[slave] = 'setup...'

    def registerSlaveAvailable(self, slave):
        self._slaveToCurrentTest[slave] = None

    def waitForAvailableSlave(self, tests):
        # Block until a slave frees up, return that slave
        while 1:
            for slave in self._slaveToCurrentTest:
                if self._slaveToCurrentTest[slave] is None:
                    self._slaveToCurrentTest[slave] = ', '.join(tests)
                    return slave
            self.sleepAndCheckStatus()

    def registerTestsCompleted(self, slave, tests, succeeded, output):
        try:
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
        # Free up the slave that ran the test
        self.registerSlaveAvailable(slave)

    def waitForAllSlavesToBeAvailable(self):
        while filter(bool, self._slaveToCurrentTest.values()):
            self.sleepAndCheckStatus()

    def waitForAllTestsToFinishAndGetWhetherAnyFailed(self):
        self.waitForAllSlavesToBeAvailable()
        if self._successmessages:
            print '\nSUCCESSES:\n\n' + '\n'.join(self._successmessages)
        if self._failuremessages:
            print '\nFAILURES:\n\n' + '\n'.join(self._failuremessages)
            print '\nFAILURE SUMMARY:\n'
            for summary in self._failuresummaries:
                print '   ' + summary
        print '\nPARALLEL TESTS: %i batches of tests passed and %i failed\n' % (len(self._successmessages), len(self._failuremessages))
        return self._failuremessages != []

    def output(self, message):
        try:
            self._outputlock.acquire()
            print message
        finally:
            self._outputlock.release()

    def sleepAndCheckStatus(self):
        time.sleep(.1)
        if time.time() - self._lastStatusTime > 30:
            self._lastStatusTime = time.time()
            for slave, test in self._slaveToCurrentTest.items():
                self.output('  (status) %s is running %s' % (slave, test or 'nothing'))

def runSubprocess(cmd, manager, failonerror=False):
    # Print what's being run
    manager.output('  (launching) ' + cmd)
    # Start the process
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # Wait for it to complete
    returncode = process.wait()
    # Collect output
    output = process.stdout.read() + process.stderr.read()
    if failonerror:
        assert returncode == 0, output
    return returncode, output

def setupSlave(slave, manager, sshuser, identityfile, slaveworkspace):

    try:
        for cmd in [
            # Clean out and re-create the workspace directory on the slave
            'ssh -i %s %s@%s "rm -rf %s; mkdir %s"' % (identityfile, sshuser, slave, slaveworkspace, slaveworkspace),
            # Copy testbundle.zip, which the host has built (with ant zip-test-bundle), into the slave workspace
            'scp -i %s target/testbundle.zip %s@%s:%s/testbundle.zip' % (identityfile, sshuser, slave, slaveworkspace),
            # Have the slave unzip testbundle.zip and run an ant target to get the slave's db ready for testing
            'ssh -i %s %s@%s "cd %s && unzip testbundle.zip > /dev/null && ant prepare-db-for-parallel-tests"' % (identityfile, sshuser, slave, slaveworkspace)]:
            runSubprocess(cmd, manager, failonerror=True)
        manager.output('  (ready) finished setting up %s' % slave)
        manager.registerSlaveAvailable(slave)
    except Exception, e:
        print e
        thread.interrupt_main()

def runTests(tests, slave, manager, sshuser, identityfile, slaveworkspace, apphomeenvvar):
    try:
        # Run the tests on the slave
        cmd = 'ssh -i %s %s@%s "cd %s && export %s=%s && ant test-several-precompiled -Dtests=%s"' % \
            (identityfile, sshuser, slave, slaveworkspace, apphomeenvvar, slaveworkspace, ','.join(['**/%s.class' % test for test in tests]))
        returncode, output = runSubprocess(cmd, manager)
        output = '<ran on %s> ' % slave + output
        manager.registerTestsCompleted(slave, tests, returncode == 0, output)
    except Exception, e:
        # Handle errors spawning the ssh process
        manager.registerTestsCompleted(slave, tests, False, repr(e))

def runAllTests(slaves, tests, sshuser, identityfile, slaveworkspace, apphomeenvvar, numtestsperslavesession):

    manager = SyncManager(slaves)
    for slave in slaves:
        thread.start_new_thread(setupSlave, (slave, manager, sshuser, identityfile, slaveworkspace))
    manager.waitForAllSlavesToBeAvailable()

    while tests:
        testsforslave = []
        while len(testsforslave) < numtestsperslavesession and tests:
            testsforslave.append(tests.pop())
        slave = manager.waitForAvailableSlave(testsforslave)
        thread.start_new_thread(runTests, (testsforslave, slave, manager, sshuser, identityfile, slaveworkspace, apphomeenvvar))

    somefailures = manager.waitForAllTestsToFinishAndGetWhetherAnyFailed()
    if somefailures:
        return 1
    else:
        return 0

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option('-s', dest='slaves', help='comma-separated list of slaves to run tests on')
    parser.add_option('-u', dest='sshuser', help='user to ssh to slaves as')
    parser.add_option('-w', dest='slaveworkspace', help='remote directory to run tests in')
    parser.add_option('-i', dest='identityfile', help='ssh identity file')
    parser.add_option('-v', dest='apphomeenvvar', help='e.g., THREETWELVE_HOME')
    parser.add_option('-n', dest='numtestsperslavesession', help='number of tests to delegate to each slave at a time')

    (options, args) = parser.parse_args()
    assert not args, 'got unexpected command-line arguments: %r' % args
    assert options.slaves, 'please provide a comma-separated list of slaves'
    assert options.sshuser, 'please provide a user to ssh to the slaves as'
    assert options.slaveworkspace, 'please provide a remote directory where tests should be run'
    assert options.identityfile, 'please provide an ssh identity file'
    assert options.apphomeenvvar, 'please provide the name of the application home dir environment variable, e.g., THREETWELVE_HOME'
    assert options.numtestsperslavesession, 'please provide the number of tests to delegate to each slave at a time'

    sshuser = options.sshuser.strip()
    slaveworkspace = options.slaveworkspace.strip()
    identityfile = options.identityfile.strip()
    apphomeenvvar = options.apphomeenvvar.strip()
    numtestsperslavesession = int(options.numtestsperslavesession.strip())
    slaves = options.slaves.strip().split(',')
    print 'available slaves: %r' % slaves

    # Get names of tests to run from stdin
    tests = map(str.strip, sys.stdin.readlines())
    numtestclasses = len(tests)
    print 'test classes to run: %i' % numtestclasses

    exitstatus = runAllTests(slaves, tests, sshuser, identityfile, slaveworkspace, apphomeenvvar, numtestsperslavesession)
    print 'ran %i test classes' % numtestclasses
    sys.exit(exitstatus)
