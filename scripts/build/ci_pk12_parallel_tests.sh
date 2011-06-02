#!/bin/bash

# See parallelTests.py for more details.

set -eu

apphomeenvvar=$1 # e.g., OUTCOMES_HOME
testsperbatch=$2 # e.g., 8, to farm 8 tests to each testdog at a time

# Copy the workspace to the testdogs, and run unit tests
echo "RUNNING UNIT TESTS IN PARALLEL"
find target/test/unit -name *Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py -s yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net -u autobuild -i /home/jenkins/.ssh/autobuild_key -w /home/autobuild/$JOB_NAME -v $apphomeenvvar -n $testsperbatch -c

# Run db updates on the testdogs and then all integration and webservice tests
echo "RUNNING INTEGRATION AND WEBSERVICE TESTS IN PARALLEL"
( find target/test/integration target/test/webservice \
) | grep Test.class \
  | xargs -i basename {} .class \
  | /opt/wgen-3p/python26/bin/python conf/base/scripts/build/parallelTests.py -s yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net -u autobuild -i /home/jenkins/.ssh/autobuild_key -w /home/autobuild/$JOB_NAME -v $apphomeenvvar -n $testsperbatch -d
