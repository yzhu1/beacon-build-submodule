#!/bin/bash

# Finds all integration and webservice tests (webdriver coming soon) and runs them on $slaves as $masteruser in an automatically created $slaveworkspace remote directory.
# Prereq: ant zip-test-bundle
# See parallelTests.py for more details.

# example dev usage (swap your name in for dan) for outcomes:
# time ./conf/base/scripts/build/run_parallel_tests.sh yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net autobuild ~/.ssh/id_rsa /home/autobuild/dan-outcomes OUTCOMES_HOME 8

# example ci usage (get $JOB_NAME from hudson) for outcomes:
# time ./conf/base/scripts/build/run_parallel_tests.sh yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net autobuild /home/tomcat/.ssh/autobuild_key /home/autobuild/$JOB_NAME OUTCOMES_HOME 8

set -eu

slaves=$1                  # e.g., yad127.tt.wgenhq.net,yad128.tt.wgenhq.net,yad129.tt.wgenhq.net
masteruser=$2              # e.g., autobuild
identityfile=$3            # e.g., /home/tomcat/.ssh/autobuild_key
slaveworkspace=$4          # e.g., /home/autobuild/$JOB_NAME
apphomeenvvar=$5           # e.g., OUTCOMES_HOME
numtestsperslavesession=$6 # e.g., 8, to farm 8 tests to each slave at a time

find target/test/integration target/test/webservice \
  | grep Test.class \
  | xargs -i basename {} .class \
  | python conf/base/scripts/build/parallelTests.py -s $slaves -u $masteruser -i $identityfile -w $slaveworkspace -v $apphomeenvvar -n $numtestsperslavesession
