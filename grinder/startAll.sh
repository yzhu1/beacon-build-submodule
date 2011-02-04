#!/bin/bash
GRINDERPATH=$COMMON_HOME/grinder
GRINDERPROPERTIES=$GRINDERPATH/grinder.properties
CLASSPATH=$GRINDERPATH/lib/*.jar:$CLASSPATH
export CLASSPATH PATH GRINDERPROPERTIES
bash startConsole.sh &
bash startAgent.sh &
