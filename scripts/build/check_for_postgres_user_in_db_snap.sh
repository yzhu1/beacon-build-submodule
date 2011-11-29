#!/bin/bash

# If this fails, run sed -i 's/postgres/tt_manage/g' sql_snaps/<latest fixtures snap>

set -eu
snap=$1
echo "In the baseline and fixtures snapshots, we don't want any references to the postgres user"
echo "(Should be tt_manage instead, otherwise ci migrations will fail)"
echo "Checking for instances of 'postgres' in" $snap
exit `grep -c postgres $snap`
