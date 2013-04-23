#!/usr/bin/python
import os
import re
import sys

# run-tests-smart.py [status] [<tree-ish> ...]
# run from project root directory to run tests that have been modified
# in the working tree or specified tree-ishes (like a hash or HEAD~1)

test_candidates = []
for argument in sys.argv[1::]:
    if argument == "status":
        command = os.popen("git status --porcelain")
    else:
        command = os.popen("git log -n 1 --summary " + argument)
    test_candidates.extend(command.readlines())
    command.close()

regex = re.compile("src/test/.*Test.java")
test_full_names = [x.strip() for x in test_candidates if regex.search(x.strip())]

test_names = []
for test_full_name in test_full_names:
    test_name = re.sub("^.* src/test/.*/", "**/", test_full_name)
    test_name = re.sub("java$", "class", test_name)
    test_names.append(test_name)

ant_argument = ",".join(test_names)

ant_command = "ant test-several-precompiled -Dtests=" + ant_argument
print "Running: " + ant_command
os.system(ant_command)
print "Ran: " + ant_command

