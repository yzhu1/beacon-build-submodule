#!/bin/bash

set -e

db_user=$1
db_host=$2
db=$3
db_schema=$4

if [ -z $db_user ] || [ -z $db_host ] || [ -z $db ] || [ -z $db_schema ]
then
    echo "usage: $0 db_user db_host db_name db_schema"
    exit -1
fi

clear_sql_filename=/tmp/db_clear${RANDOM}.sql

this_dir=`dirname $0`
tmp_sql_file=/tmp/tt/itembank/sql/clear${RANDOM}.sql

# remove any existing temp sql
rm -f $tmp_sql_file
rm -f $clear_sql_filename

# generate the sql that will drop all db objects
mkdir -p `dirname $tmp_sql_file`
mkdir -p `dirname $clear_sql_filename`
# replace the schema name
sed -e "s|#SCHEMA#|$db_schema|" $this_dir/generate_clear_sql.sql.template > $tmp_sql_file

psql -t -h $db_host -U $db_user $db -f $tmp_sql_file > $clear_sql_filename
echo "Filename is $clear_sql_filename"
# HACK: mperpick get rid of the output of the search_path set command
sed -i.bak '1d' $clear_sql_filename

echo "the sql used to clear the db $db in $clear_sql_filename:"
cat $clear_sql_filename

echo
echo "running cleanup"
echo 

psql -t -h $db_host -U $db_user $db -f $clear_sql_filename

# clean-up
rm -f $tmp_sql_file
rm -f $clear_sql_filename
