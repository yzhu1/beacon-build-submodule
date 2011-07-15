#!/bin/sh
#
# liquibase.sh
#
# A simple wrapper to call the LiquiBase jar from the command line.
#
#   $ sh liquibase.sh <changelog_file> <liquibase_command>
#
# Requires the following environment variables to be set:
#
# LIQUIBASE_JAR: location of the liquibase jar
#
# LIQUIBASE_CLASSPATH: classpath additions needed by liquibase (postgres jdbc)
#
# LIQUIBASE_MIGRATIONS: location of the migrations files (xml def and sql scripts)
#
# LIQUIBASE_DB_HOST: hostname of db to run migrations against
#
# LIQUIBASE_DB_PORT: network port of db to run migrations against
#
# LIQUIBASE_DB_NAME: database name of db to run migrations against
#
# LIQUIBASE_DB_USER: user to run migrations as
#
# LIQUIBASE_DB_PWORD: password for db user
#
# LIQUIBASE_DB_SCHEMA: database schema

helpurl=http://www.liquibase.org/manual/command_line#liquibase_command_line

if [ -z $1 ] || [ -z $2 ]; then
    echo "usage: $0 <changelog_name> <liquibase_command>"
    echo 
    echo "help here: $helpurl"  
    echo
    exit 1
fi

if [ -z "${LIQUIBASE_DB_SCHEMA}" ]; then
    echo "Error: LIQUIBASE_DB_SCHEMA environment variable is not set"
    echo 
    exit 2
fi

CHANGELOG_NAME=$1
shift
LIQUIBASE_CMD=$@

CMD="java -Xmx1024m 
    -jar ${LIQUIBASE_JAR}
    --driver=org.postgresql.Driver
    --classpath=${LIQUIBASE_CLASSPATH}:${LIQUIBASE_MIGRATIONS}
    --changeLogFile=${LIQUIBASE_MIGRATIONS}/$CHANGELOG_NAME
    --logLevel=finest
    --url=jdbc:postgresql://${LIQUIBASE_DB_HOST}:${LIQUIBASE_DB_PORT}/${LIQUIBASE_DB_NAME}
    --username=${LIQUIBASE_DB_USER}
    --password=${LIQUIBASE_DB_PWORD}
    --defaultSchemaName=${LIQUIBASE_DB_SCHEMA}
    ${LIQUIBASE_CMD}"

echo $CMD

exec $CMD
