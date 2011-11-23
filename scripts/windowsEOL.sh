#!/bin/bash

cd ../../../
set error = false;
if test $(file `find . -name *.java` | grep CRLF | wc -l) -ne 0 
then
	error=true;
fi

if test $(file `find . -name *.js` | grep CRLF | wc -l) -ne 0 
then
	error=true;
fi

if test $(file `find . -name *.scss` | grep CRLF | wc -l) -ne 0 
then
	error=true;
fi

if test $(file `find . -name *.ftl` | grep CRLF | wc -l) -ne 0 
then
	error=true;
fi
if $error ; then
echo "Files with CRLF instead of LF" 
  file `find . -name *.java` | grep CRLF | sed 's/  */\ /g' | sed 's/:.*$//'
  file `find . -name *.js` | grep CRLF | sed 's/  */\ /g'| sed 's/:.*$//'
  file `find . -name *.scss` | grep CRLF | sed 's/  */\ /g' | sed 's/:.*$//'
  file `find . -name *.ftl` | grep CRLF | sed 's/  */\ /g' | sed 's/:.*$//'
  exit 1
fi
echo "There are no windows EOLs present"