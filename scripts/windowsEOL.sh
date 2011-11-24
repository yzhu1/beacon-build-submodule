#!/bin/bash

SEARCH_DIR=../../../
set error = 0;
if test $(file `find $SEARCH_DIR -name *.java` | grep CRLF | wc -l) -ne 0 
then
    echo 'java'
	error=1;
fi

if test $(file `find $SEARCH_DIR -name *.js` | grep CRLF | wc -l) -ne 0 
then
    echo 'js'
	error=1;
fi

if test $(file `find $SEARCH_DIR -name *.scss` | grep CRLF | wc -l) -ne 0 
then
    echo 'scss'
	error=1;
fi

if test $(file `find $SEARCH_DIR -name *.ftl` | grep CRLF | wc -l) -ne 0 
then
    echo 'ftl'
	error=1;
fi

if [ "$error" = "1" ]; then
echo "Files with CRLF instead of LF" 
  file `find $SEARCH_DIR -name *.java` | grep CRLF | sed 's/  */\ /g' | sed 's/:.*$//'
  file `find $SEARCH_DIR -name *.js` | grep CRLF | sed 's/  */\ /g'| sed 's/:.*$//'
  file `find $SEARCH_DIR -name *.scss` | grep CRLF | sed 's/  */\ /g' | sed 's/:.*$//'
  file `find $SEARCH_DIR -name *.ftl` | grep CRLF | sed 's/  */\ /g' | sed 's/:.*$//'
  exit 1
fi
echo "There are no windows EOLs present"
