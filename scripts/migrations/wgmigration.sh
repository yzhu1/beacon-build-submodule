#!/bin/bash
#
# wgmigration.sh
#
# Liquibase migration runner
#
#   $ bash wgmigration.sh <env_filepath> <schema_name> <liquibase_dbchangelog_filename> <migration_tag>
#
# Runs a command, returning the stdout
#
# Example Usage:
#
#   $ bash wgmigration.sh /opt/tt/migrations/conf/migrations.env itembank oib_7.2.0_migrate.xml 7.2.0


if [ "$#" != "4" ]; then
    echo "usage: $0  <env_filepath> <schema_name> <liquibase_dbchangelog_filename> <migration_tag>\n"
    exit 1
fi

ENV_FILEPATH=$1
SCHEMA_NAME=$2
CHANGLOG_FILENAME=$3
MIGRATION_TAG=$4

source $ENV_FILEPATH

export LIQUIBASE_DB_SCHEMA=$SCHEMA_NAME

set -e
set -x

/opt/tt/migrations/bin/liquibase.sh $CHANGLOG_FILENAME migrate
/opt/tt/migrations/bin/liquibase.sh $CHANGLOG_FILENAME tag $MIGRATION_TAG
