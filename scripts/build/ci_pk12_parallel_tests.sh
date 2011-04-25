#!/bin/bash

# Prereq: run "ant zip-test-bundle" to build a file named target/testbundle.zip containing everything the slaves need to run tests.
# See parallelTests.py for more details.

set -eu

apphomeenvvar=$1 # e.g., OUTCOMES_HOME
testsperbatch=$2 # e.g., 8, to farm 8 tests to each slave at a time

# Find all unit, integration, webservice and wgspringcore integration test names and pipe them to parallelTests.py
(   find ivy_lib/compile -name *wgspringcore*integration*jar -exec jar -tf \{} \; \
 && find target/test/unit target/test/integration target/test/webservice \
) | grep Test.class \
  | xargs -i basename {} .class \
  | python conf/base/scripts/build/parallelTests.py -s yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net -u autobuild -i /home/tomcat/.ssh/autobuild_key -w /home/autobuild/$JOB_NAME -v $apphomeenvvar -n $testsperbatch
