import func_module
from func.minion import sub_process

import os
import pwd
import subprocess
import sys

class WgMigration(func_module.FuncModule):
    version = "1.0"
    api_version = "1.0"
    description = "Liquibase migration runner"

    migrations_root = os.path.sep + os.path.join("opt", "tt", "migrations")
    liquibase_script = os.path.join(migrations_root, "bin", "liquibase.sh")
    config_file = os.path.join(migrations_root, "conf", "migrations.env")

    # This function has been taken from func.minion.modules.command
    @staticmethod
    def __run(command, user=None, env=None):
        """
        Runs a command, returning the stdout
        NOT FOR USE WITH INTERACTIVE COMMANDS.
        """
        # Set the uid if required
        if user:
            os.setuid(pwd.getpwnam(user).pw_uid)

        cmdref = sub_process.Popen(command, stdout=sub_process.PIPE,
                                   stderr=sub_process.PIPE, shell=True,
                                   close_fds=True, env=env)
        data = cmdref.communicate()
        if cmdref.returncode != 0:
            raise Exception("stdout: %s stderr: %s" % (data[0], data[1]))
        return data[0], data[1]

    def __run_liquibase(self, changelog_name, command, schema):
        env_cmd = self._get_env_command()
        schema_cmd = self._get_schema_command(schema)
        liquibase_cmd = self._get_liquibase_command(changelog_name, command)
        cmd = "%s; %s; %s" % (env_cmd, schema_cmd, liquibase_cmd)
        return cmd, self.__run(cmd)

    @staticmethod
    def _get_changelog_name(version, app, phase):
        name = "%s_%s_%s" % (app, version, phase)
        name += ".xml"
        return name

    def _get_env_command(self):
        return "source %s" % (self.config_file)

    def _get_schema_command(self, schema_name):
        return "export LIQUIBASE_DB_SCHEMA=%s" % (schema_name)

    def _get_liquibase_command(self, changelog_name, command):
        return "%s %s %s" % (self.liquibase_script, changelog_name, command)

    def _get_schema_name(self, app):
        fp = open(os.path.join(self.migrations_root, "migrations", app, "schema"))
        return fp.read().strip()

    def migrate(self, version, app, phase):
        changelog_name = self._get_changelog_name(version, app, phase)
        schema_name = self._get_schema_name(app)
        return self.__run_liquibase(changelog_name, "update", schema_name)

    def revert(self, version, app, phase, tag=None):
        if not tag:
            tag = version
        changelog_name = self._get_changelog_name(version, app, phase)
        schema_name = self._get_schema_name(app)
        return self.__run_liquibase(changelog_name, "rollback %s" % (tag), schema_name)

    def tag(self, version, app, phase, tag=None):
        if not tag:
            tag = version
        changelog_name = self._get_changelog_name(version, app, phase)
        schema_name = self._get_schema_name(app)
        return self.__run_liquibase(changelog_name, "tag %s" % (tag), schema_name)
