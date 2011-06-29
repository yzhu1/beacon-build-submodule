#!/bin/bash

# If this fails, run sed -i 's/postgres/tt_manage/g' sql_snaps/<latest fixtures snap>

set -exu
snap=$1
echo "In the baseline and fixtures snapshots, we don't want any references to the postgres user -- should be tt_manage instead -- otherwise ci migrations will fail"
exit `grep postgres $snap|wc -l`
