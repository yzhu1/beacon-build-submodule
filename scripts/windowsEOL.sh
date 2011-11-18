#!/bin/bash

cd ../../../

if test $(file `find . -name *.java` | grep CRLF | wc -l) -ne 0 
then
	echo "The following Java files have windows line endings"
	file `find . -name *.java` | grep CRLF | sed 's/  */\ /g'
	exit 1
fi

if test $(file `find . -name *.js` | grep CRLF | wc -l) -ne 0 
then
	echo "The following javaScript files have windows line endings"
 file `find . -name *.js` | grep CRLF | sed 's/  */\ /g'
	exit 1
fi

if test $(file `find . -name *.scss` | grep CRLF | wc -l) -ne 0 
then
	echo "The following scss files have windows line endings"
	file `find . -name *.scss` | grep CRLF | sed 's/  */\ /g'
	exit 1
fi

if test $(file `find . -name *.ftl` | grep CRLF | wc -l) -ne 0 
then
	echo "The following FTL files have windows line endings"
	file `find . -name *.ftl` | grep CRLF | sed 's/  */\ /g'
	exit 1
fi

echo "There are no windows EOLs present"