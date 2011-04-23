#!/usr/bin/python

'''
Runs tests, their names read from stdin, in parallel.  Invoked by the test-parallel ant target.

example usage:

find target/test/unit|grep Test.class|xargs -i basename {} .class | \
    python conf/base/scripts/build/runParallelTests.py -s localhost -u $USER -w /tmp/test -i ~/.ssh/id_rsa -v THREETWELVE_HOME
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
        self._successmessages = []
        self._slaveIsAvailable = {}
        for slave in slaves:
            self._slaveIsAvailable[slave] = False

    def registerSlaveAvailable(self, slave):
        self._slaveIsAvailable[slave] = True

    def waitForAvailableSlave(self):
        # Block until a slave frees up, return that slave
        while 1:
            for slave in self._slaveIsAvailable:
                if self._slaveIsAvailable[slave]:
                    self._slaveIsAvailable[slave] = False
                    return slave
            time.sleep(.1)

    def registerTestCompleted(self, slave, test, succeeded, output):
        try:
            self._outputlock.acquire()
            if succeeded:
                print 'PASSSED: %s (%s)' % (test, slave)
                self._successmessages.append(output)
            else:
                print 'FAILED: %s (%s)' % (test, slave)
                print output
                self._failuremessages.append(output)
        finally:
            self._outputlock.release()
        # Available up the slave that ran the test
        self.registerSlaveAvailable(slave)

    def waitForAllSlavesToBeAvailable(self):
        while False in self._slaveIsAvailable.values():
            time.sleep(.1)

    def waitForAllTestsToFinishAndGetWhetherAnyFailed(self):
        self.waitForAllSlavesToBeAvailable()
        # Print all test output
        if self._successmessages:
            print '\nSUCCESSES:\n\n' + '\n'.join(self._successmessages)
        if self._failuremessages:
            print '\nFAILURES:\n\n' + '\n'.join(self._failuremessages)
        print '\n%s: %i successes and %i failures\n' % (sys.argv[0], len(self._successmessages), len(self._failuremessages))
        return self._failuremessages != []

    def output(self, message):
        try:
            self._outputlock.acquire()
            print message
        finally:
            self._outputlock.release()

def runSubprocess(cmd, manager, failonerror=False):
    # Print what's being run
    manager.output(cmd)
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
        manager.output('> finished setting up %s' % slave)
        manager.registerSlaveAvailable(slave)
    except Exception, e:
        print e
        thread.interrupt_main()

def runTest(test, slave, manager, sshuser, identityfile, slaveworkspace, apphomeenvvar):
    try:
        # Run the test remotely via ssh
        cmd = 'ssh -i %s %s@%s "cd %s && export %s=. && ant test-one-precompiled -Dtest=%s"' % (identityfile, sshuser, slave, slaveworkspace, apphomeenvvar, test)
        returncode, output = runSubprocess(cmd, manager)
        output = '<run on %s> ' % slave + output
        manager.registerTestCompleted(slave, test, returncode == 0, output)
    except Exception, e:
        # Handle errors spawning the ssh process
        manager.registerTestCompleted(slave, test, False, repr(e))

def runAllTests(slaves, tests, sshuser, identityfile, slaveworkspace, apphomeenvvar):
    manager = SyncManager(slaves)
    for slave in slaves:
        thread.start_new_thread(setupSlave, (slave, manager, sshuser, identityfile, slaveworkspace))
    manager.waitForAllSlavesToBeAvailable()
    while tests:
        test = tests.pop()
        slave = manager.waitForAvailableSlave()
        thread.start_new_thread(runTest, (test, slave, manager, sshuser, identityfile, slaveworkspace, apphomeenvvar))
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

    (options, args) = parser.parse_args()
    assert not args, 'got unexpected command-line arguments: %r' % args
    assert options.slaves, 'please provide a comma-separated list of slaves'
    assert options.sshuser, 'please provide a user to ssh to the slaves as'
    assert options.slaveworkspace, 'please provide a remote directory where tests should be run'
    assert options.identityfile, 'please provide an ssh identity file'
    assert options.apphomeenvvar, 'please provide the name of the application home dir environment variable, e.g., THREETWELVE_HOME'

    sshuser = options.sshuser.strip()
    slaveworkspace = options.slaveworkspace.strip()
    identityfile = options.identityfile.strip()
    apphomeenvvar = options.apphomeenvvar.strip()
    slaves = options.slaves.strip().split(',')
    print 'available slaves: %r' % slaves

    # Get names of tests to run from stdin
    tests = map(str.strip, sys.stdin.readlines())
    print 'tests to run: %i' % len(tests)

    exitstatus = runAllTests(slaves, tests, sshuser, identityfile, slaveworkspace, apphomeenvvar)
    sys.exit(exitstatus)
