#!/usr/bin/python

'''
example usage:

find target/test/unit|grep Test.class|xargs -i basename {} .class | \
python conf/base/scripts/build/runParallelTests.py -H localhost -u dan -d /tmp/test -i /home/dan/.ssh/id_rsa -v THREETWELVE_HOME
'''

import sys
import thread
import optparse
import threading
import subprocess

class SyncManager(object):
    '''Manages synchronization: maintains threadsafe status information about hosts and test output.'''

    def __init__(self, hosts):
        self._outputlock = threading.Lock()
        self._failuremessages = []
        self._successmessages = []
        self._hostIsFree = {}
        for host in hosts:
            self._hostIsFree[host] = False

    def registerHostFree(self, host):
        self._hostIsFree[host] = True

    def waitForFreeHost(self):
        # Block until a host frees up, return that host
        while 1:
            for host in self._hostIsFree:
                if self._hostIsFree[host]:
                    self._hostIsFree[host] = False
                    return host

    def registerTestCompleted(self, host, test, succeeded, output):
        try:
            self._outputlock.acquire()
            if succeeded:
                print ' > PASSSED <%s>: %s' % (host, test)
                self._successmessages.append(output)
            else:
                print ' > FAILED <%s>: %s' % (host, test)
                print output
                self._failuremessages.append(output)
        finally:
            self._outputlock.release()
        # Free up the host that ran the test
        self.registerHostFree(host)

    def waitForAllHostsToBeFree(self):
        while 1:
            #if all(self._hostIsFree.values()):
            if False not in self._hostIsFree.values():
                return

    def waitForAllTestsToFinishAndGetWhetherAnyFailed(self):
        self.waitForAllHostsToBeFree()
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

def runSubprocess(cmd, manager, assertsuccess=False):
    # Print what's being run
    manager.output(cmd)
    # Start the process
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # Wait for it to complete
    returncode = process.wait()
    # Collect output
    output = process.stdout.read() + process.stderr.read()
    if assertsuccess:
        assert returncode == 0, output
    return returncode, output

def setupHost(host, manager, sshuser, identityfile, remotedir):

    try:
        for cmd in [
            'ssh -i %s %s@%s "rm -rf %s; mkdir %s"' % (identityfile, sshuser, host, remotedir, remotedir),
            'scp -i %s target/testbundle.zip %s@%s:%s/testbundle.zip' % (identityfile, sshuser, host, remotedir),
            'ssh -i %s %s@%s "cd %s && unzip testbundle.zip > /dev/null && ant prepare-db-for-integration-tests"' % (identityfile, sshuser, host, remotedir)]:
            runSubprocess(cmd, manager, assertsuccess=True)
        manager.output('> finished setting up %s' % host)
        manager.registerHostFree(host)
    except Exception, e:
        print e
        thread.interrupt_main()

def runTest(test, host, manager, sshuser, identityfile, remotedir, apphome):
    try:
        # Run the test remotely via ssh
        cmd = 'ssh -i %s %s@%s "cd %s && export %s=. && ant test-one-precompiled -Dtest=%s"' % (identityfile, sshuser, host, remotedir, apphome, test)
        returncode, output = runSubprocess(cmd, manager)
        output = '<run on %s> ' % host + output
        manager.registerTestCompleted(host, test, returncode == 0, output)
    except Exception, e:
        # Handle errors spawning the ssh process
        manager.registerTestCompleted(host, test, False, repr(e))

def runAllTests(hosts, tests, sshuser, identityfile, remotedir, apphome):
    manager = SyncManager(hosts)
    for host in hosts:
        thread.start_new_thread(setupHost, (host, manager, sshuser, identityfile, remotedir))
    manager.waitForAllHostsToBeFree()
    while tests:
        test = tests.pop()
        host = manager.waitForFreeHost()
        thread.start_new_thread(runTest, (test, host, manager, sshuser, identityfile, remotedir, apphome))
    somefailures = manager.waitForAllTestsToFinishAndGetWhetherAnyFailed()
    if somefailures:
        return 1
    else:
        return 0

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option('-H', dest='hosts', help='comma-separated list of hosts to run tests on')
    parser.add_option('-u', dest='sshuser', help='user to ssh as')
    parser.add_option('-d', dest='remotedir', help='remote directory to run tests in')
    parser.add_option('-i', dest='identityfile', help='ssh identity file')
    parser.add_option('-v', dest='apphome', help='applicatio home dir environment variable')

    (options, args) = parser.parse_args()
    assert not args, 'got unexpected command-line arguments: %r' % args
    assert options.hosts, 'please provide a comma-separated list of hosts'
    assert options.sshuser, 'please provide a user to ssh as'
    assert options.remotedir, 'please provide a remote directory where tests should be run'
    assert options.identityfile, 'please provide an ssh identity file'
    assert options.apphome, 'please provide the name of the application home dir environment variable'

    sshuser = options.sshuser.strip()
    remotedir = options.remotedir.strip()
    identityfile = options.identityfile.strip()
    apphome = options.apphome.strip()
    hosts = options.hosts.strip().split(',')
    print 'available hosts: %r' % hosts
    print 'will run tests as %s (using identify file %s) in remote dir %s setting environment variable %s=.' % (sshuser, identityfile, remotedir, apphome)

    # Get names of tests to run from stdin
    tests = map(str.strip, sys.stdin.readlines())
    print 'tests to run: %i' % len(tests)

    exitstatus = runAllTests(hosts, tests, sshuser, identityfile, remotedir, apphome)
    sys.exit(exitstatus)
