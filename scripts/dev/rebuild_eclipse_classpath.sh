#!/bin/bash

# Scans ivy_lib/ and generates a .classpath file (which you should gitignore) for eclipse to use.
# This is an alternative to using the IvyDE plugin.  This scripts gets invoked at the end of
# ivy-resolve if you have use.eclipse.ivyde.plugin=false in your build.properties.

# To set use.eclipse.ivyde.plugin=false everywhere:
#   find $THREETWELVE_HOME/.. -name build.properties -exec sh -c "echo use.eclipse.ivyde.plugin=false >> {}" \;

set -e

echo 'rebuilding eclipse classpath'

# Find all unique jars under ivy_lib/
jars=`find ivy_lib -name *.jar|xargs -i basename {}|sort|uniq`

# Find all binary jars for which we have a source jar
bin_jars_with_src_available=
for jar in $jars; do
  if [[ $jar == *src* ]]; then
    bin_jars_with_src_available=$bin_jars_with_src_available" "`echo $jar|sed 's/-src//'`
  fi
done

classpathentry() {
  echo "$1" >> .classpath
}

# Write out head of .classpath
echo "<?xml version='1.0' encoding='UTF-8'?>" > .classpath
classpathentry "<classpath>"
classpathentry "	<classpathentry kind='src' path='src/main/java'/>"
classpathentry "	<classpathentry including='*-context.xml' kind='src' path='src/test/resources'/>"
classpathentry "	<classpathentry kind='src' path='target/web-assets/unzip/wgspringcore-web-assets/web/WEB-INF'/>"
classpathentry "	<classpathentry kind='src' path='target/web-assets/unzip/wgspringcore-web-assets/resources'/>"
classpathentry "	<classpathentry excluding='java/' kind='src' path='src/test/webdriver/util'/>"
classpathentry "	<classpathentry excluding='java/' kind='src' path='src/test/integration/util'/>"
classpathentry "	<classpathentry kind='src' path='src/main/webapp/WEB-INF'/>"
classpathentry "	<classpathentry kind='src' path='src/main/resources'/>"
classpathentry "	<classpathentry kind='src' path='src/test/java'/>"
classpathentry "	<classpathentry kind='src' path='src/test/integration/controller/java'/>"
classpathentry "	<classpathentry kind='src' path='src/test/integration/service/java'/>"
classpathentry "	<classpathentry kind='src' path='src/test/integration/util/java'/>"
classpathentry "	<classpathentry kind='src' path='src/test/webdriver/java'/>"
classpathentry "	<classpathentry kind='src' path='src/test/webdriver/util/java'/>"
classpathentry "	<classpathentry kind='src' path='src/test/webservice/util/java'/>"
classpathentry "	<classpathentry kind='src' path='src/test/webservice/java'/>"
classpathentry "	<classpathentry kind='con' path='org.eclipse.jst.j2ee.internal.web.container'/>"
classpathentry "	<classpathentry kind='con' path='org.eclipse.jst.j2ee.internal.module.container'/>"
classpathentry "	<classpathentry kind='con' path='org.eclipse.jdt.launching.JRE_CONTAINER'/>"
classpathentry "	<classpathentry kind='output' path='target/eclipse/classes'/>"

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
      classpathentry "    <classpathentry kind='lib' path='$bin' sourcepath='$jar' />"
    else                         # Otherwise, write out a regular entry
      classpathentry "    <classpathentry kind='lib' path='$jar' />"
    fi
  fi
done

classpathentry '</classpath>'
