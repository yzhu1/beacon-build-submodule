#!/bin/bash

set -eu

db_user=$1
db_host=$2
db_port=$3
db=$4

if [ -z $db_user ] || [ -z $db_host ] || [ -z $db_port ] || [ -z $db ]
then
    echo "usage: $0 db_user db_host db_port db_name"
    exit -1
fi

this_dir=`dirname $0`
validate_sql_filename=/tmp/validate-fk-names-${RANDOM}.sql
intermediate_filename=/tmp/validate-fk-names-intermediate-${RANDOM}.txt
output_filename=/tmp/validate-fk-names-output-${RANDOM}.txt

# replace the constraints to be excluded
sed -e "s|#EXCLUSIONS#|$EXCLUDED_CONSTRAINTS|" $this_dir/validate-foreign-key-names.sql.template > $validate_sql_filename
# get non-conforming foreign keys
psql -t -h $db_host -p $db_port -U $db_user $db -f $validate_sql_filename -o $intermediate_filename
# delete blank line(s), especially the last on psql appends
sed '/^$/d' $intermediate_filename > $output_filename

# check for non-conforming results
exit_status=0
if [[ -s $output_filename ]]; then
    echo 'Foreign keys should be in the format fk__source_table_name__source_column_name.'
    echo 'If the FK names would be longer than 63 characters, pick the best name you can'
    echo 'and use the wgspring.db.constraint-check.excluded-constraints build property.'
    echo 'There are invalid constraint names:'
    cat $output_filename
    exit_status=1
fi

# clean-up
rm -f $validate_sql_filename
rm -f $intermediate_filename
rm -f $output_filename

exit $exit_status
