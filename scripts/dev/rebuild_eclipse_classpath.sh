#!/bin/bash

# Scans ivy_lib/ and generates a .classpath file (which you should gitignore) for eclipse to use.
# This is an alternative to using the IvyDE plugin.  This scripts gets invoked at the end of
# ivy-resolve if you have use.eclipse.ivyde.plugin=false in your build.properties.

# To set use.eclipse.ivyde.plugin=false everywhere:
#   find $THREETWELVE_HOME/.. -name build.properties -exec sh -c "echo use.eclipse.ivyde.plugin=false >> {}" \;

set -e

# Second parameter is a file to use for the header (project-specific source
# directories, etc., starting from "<?xml...")
header=$1

if [[ -z $header || ! -e $header ]]; then 
    header=conf/base/scripts/dev/eclipse.classpath.header
fi

echo "rebuilding eclipse classpath using header $header"

classpathline() {
  echo "$1" >> .classpath
}

# Write out head of .classpath
cat $header > .classpath

# Find all unique jars under ivy_lib/
jars=`find ivy_lib -name *.jar | xargs -I JAR basename JAR | sort -u`

# Find all binary jars for which we have a source jar
bin_jars_with_src_available=
for jar in $jars; do
  if [[ $jar == *src* ]]; then
    bin_jars_with_src_available=$bin_jars_with_src_available" "`echo $jar|sed 's/-src//'`
  fi
done

# Write out ivy entries in .classpath
for jar in $jars; do
  if [[ $bin_jars_with_src_available != *$jar* ]]; then # Don't create dup entries for bin jars for which we have sources
    if [ -e "ivy_lib/compile/"$jar ]; then # Find a path to this jar in any ivy_lib/ subdirectory that has it; try compile/ first for speed
      jar="ivy_lib/compile/"$jar
    else
      jar=`find ivy_lib/ -name $jar|head -1`
    fi
    if [[ $jar == *src* ]]; then # If this is a source jar, write out an entry with both bin and src
      bin=`echo $jar|sed 's/-src//'`
      classpathline "    <classpathentry kind='lib' path='$bin' sourcepath='$jar' />"
    else                         # Otherwise, write out a regular entry
      classpathline "    <classpathentry kind='lib' path='$jar' />"
    fi
  fi
done

classpathline '</classpath>'
