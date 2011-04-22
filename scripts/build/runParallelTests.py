#!/usr/bin/python

'''
example usage:

echo -e 'UserInterceptorTest\nAssessmentTest\nWgenContentImportControllerTest\nPdfTextUtilTest' | python \
conf/base/scripts/build/runParallelTests.py -H localhost,10.15.1.203 -u dan -d /home/dan/devel/3_12/threetwelve
'''

import sys
import thread
import optparse
import threading
import subprocess

class TestManager(object):
    '''Manages synchronization: maintains threadsafe status information about hosts and test output.'''

    def __init__(self, hosts):
        self._outputlock = threading.Lock()
        self._hostslock = threading.Lock()
        self._failuremessages = []
        self._successmessages = []
        self._hostIsFree = {}
        for host in hosts:
            self._hostIsFree[host] = True

    def waitForFreeHost(self):
        # Block until a host frees up, return that host
        while 1:
            with self._hostslock:
                for host in self._hostIsFree:
                    if self._hostIsFree[host]:
                        self._hostIsFree[host] = False
                        return host

    def registerTestCompleted(self, didSucceed, output, host):
        # Store the test's output
        with self._outputlock:
            (self._successmessages if didSucceed else self._failuremessages).append(output)
        # Free up the host that ran the test
        with self._hostslock:
            self._hostIsFree[host] = True

    def waitForAllTestsToFinishAndGetWhetherAnyFailed(self):

        # Block until all hosts are free and therefore all tests finished
        while 1:
            with self._hostslock:
                if all(self._hostIsFree.values()):
                    break

        # Print all test output
        if self._successmessages:
            print '\nSUCCESSES:\n\n' + '\n'.join(self._successmessages)
        if self._failuremessages:
            print '\nFAILURES:\n\n' + '\n'.join(self._failuremessages)

        print '\n%s: %i successes and %i failures' % (sys.argv[0], len(self._successmessages), len(self._failuremessages))

        return self._failuremessages != []

def runTest(test, host, manager, sshuser, remotedir):
    # Put together an ssh command to run the test remotely
    cmd = ['ssh',
           '%s@%s' % (sshuser, host),
           'cd %s && ant one-precompiled -Dtest=%s' % (remotedir, test)]
    print 'running %s' % ' '.join(cmd)
    # Start that ssh process
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for it to complete
    returncode = process.wait()
    output = process.stdout.read() + '\n(run on %s)' % host
    manager.registerTestCompleted(returncode == 0, output, host)

def runAllTests(hosts, tests, sshuser, remotedir):
    manager = TestManager(hosts)
    while tests:
        test = tests.pop()
        host = manager.waitForFreeHost()
        thread.start_new_thread(runTest, (test, host, manager, sshuser, remotedir))
    exitstatus = 1 if manager.waitForAllTestsToFinishAndGetWhetherAnyFailed() else 0
    return exitstatus

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option('-H', dest='hosts', help='comma-separated list of hosts to run tests on')
    parser.add_option('-u', dest='sshuser', help='user to ssh as')
    parser.add_option('-d', dest='remotedir', help='remote directory to run tests in')

    (options, args) = parser.parse_args()
    assert not args, 'got unexpected command-line arguments: %r' % args
    assert options.hosts, 'please provide a comma-separated list of hosts'
    assert options.sshuser, 'please provide a user to ssh as'
    assert options.remotedir, 'please provide a remote directory where tests should be run'

    sshuser = options.sshuser
    remotedir = options.remotedir
    hosts = options.hosts.split(',')
    print 'available hosts: %r' % hosts

    # Get names of tests to run from stdin
    tests = map(str.strip, sys.stdin.readlines())
    print 'tests to run: %i' % len(tests)

    exitstatus = runAllTests(hosts, tests, sshuser, remotedir)
    sys.exit(exitstatus)
