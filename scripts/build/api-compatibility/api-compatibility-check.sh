#!/bin/sh

# expect arguments: ivy version
if [ $# -ne 1 ]; then
    echo "usage: `basename $0` <ivy version in the form major.minor.revision-build>"
    exit 1
fi

IVY_VERSION=$1
SCRIPTS=`dirname ${BASH_SOURCE}`

BUILD_JAR_DIR="target/jar"
BASELINE_JAR_DIR="target/baseline-jars"

# cleanup old compatibility reports
rm -rf compat_reports

# this could be made fancier and more general, but that seems like poor value for our money right now
function findlocaljar() {
    jarfile=$1
    if [ -e "$BUILD_JAR_DIR/$jarfile" ]
    then
        echo "$BUILD_JAR_DIR/$jarfile"
    elif [ -e "$BUILD_JAR_DIR/test/$jarfile" ]
    then
        echo "$BUILD_JAR_DIR/test/$jarfile"
    fi
}

RESULT=0

function new_compat_test() {
    REVISION=$1
    JAR_NAME=$2
    IVY_JAR="$BASELINE_JAR_DIR/$REVISION/$JAR_NAME"
    PRETTY_JAR_NAME=`basename $JAR_NAME .jar`
    LOCAL_JAR=`findlocaljar $JAR_NAME`
    echo Comparing $IVY_JAR to $LOCAL_JAR
    ${SCRIPTS}/japi-compliance-checker.pl -l $PRETTY_JAR_NAME -o $IVY_JAR -v1 $REVISION -n $LOCAL_JAR -v2 "current-build"

    if [ $? -ne 0 ]; then
        echo "$JAR_NAME is not compatible"
        RESULT=1
    fi
}

for ARTIFACT in `(cd $BASELINE_JAR_DIR/$IVY_VERSION; ls *jar)`
do
    new_compat_test $IVY_VERSION $ARTIFACT
done

${SCRIPTS}/api-compatibility-report.pl > compat_reports/index.html

if [ $RESULT -ne 0 ]; then
    echo "it looks like the public API changed. please either keep the public API consistent, or increment the patch level"
    exit 1
fi

