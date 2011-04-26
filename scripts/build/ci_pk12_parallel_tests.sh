#!/bin/bash

# See parallelTests.py for more details.

set -eu

apphomeenvvar=$1 # e.g., OUTCOMES_HOME
testsperbatch=$2 # e.g., 8, to farm 8 tests to each slave at a time

# Find all unit, integration, webservice and wgspringcore integration test names and pipe them to parallelTests.py
find target/test/unit target/test/integration target/test/webservice -name *Test.class \
  | xargs -i basename {} .class \
  | python conf/base/scripts/build/parallelTests.py -s yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net -u autobuild -i /home/tomcat/.ssh/autobuild_key -w /home/autobuild/$JOB_NAME -v $apphomeenvvar -n $testsperbatch
