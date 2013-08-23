#!/opt/wgen-3p/python27/bin/python

import re
import os
import os.path
import optparse
import pdb
import sys
import datetime
import itertools

MAJOR = 'major'
MINOR = 'minor'
PATCHLEVEL = 'patch'
BUILD_NUMBER = 'build'

root_dir = "/opt/wgen/ivy/wgen"
dpp13numbers = "(?P<%s>\d+)\.(?P<%s>\d+)\.(?P<%s>\d+)-(?P<%s>\d+)" % (
    MAJOR, MINOR, PATCHLEVEL, BUILD_NUMBER
)

class build_info(object):
	def __init__(self, patchlevel, build_number, timestamp, files=None):
		self._patchlevel = patchlevel
		self._build_number = int(build_number)
		self._timestamp = timestamp
		self._files = []
		if files is not None:
			self._files.extend(files)

	def get_file_names(self):
		return self._files

	def get_file_paths(self):
		project = self._patchlevel.project
		return [ project.get_path(filename) for filename in self._files ]

	def get_number(self):
		return self._build_number

	def get_timestamp(self):
		return self._timestamp

	def add_file(self, filename):
		self._files.append(filename)

class patchlevel(object):
	def __init__(self, project, dict=None, major=None, minor=None, patchlevel=None):
		if dict:
			self.major = dict[MAJOR]
			self.minor = dict[MINOR]
			self.patchlevel = dict[PATCHLEVEL]
		else:
			self.major = major
			self.minor = minor
			self.patchlevel = patchlevel
		self.project = project
		self.builds = []

	def version_string(self):
		return "%s.%s.%s" % (self.major, self.minor, self.patchlevel)

	def add_build(self, build_number, timestamp):
		self.builds.append(build_info(self, build_number, timestamp))

	def get_build(self, build_number):
		numeric_build_number = int(build_number)
		for build in self.builds:
			if build.get_number() == numeric_build_number:
				return build
		raise Exception("Could not find build %s for patchlevel %s" % (build_number, self.version_string()))

	def latest_build(self):
		latest = self.builds[0]
		for build in self.builds:
			if build.get_number() > latest.get_number():
				latest = build
		return latest

	def build_count(self):
		return len(self.builds)

class project_build_holder(object):
	def __init__(self, project_name):
		self._h = {}
		self._bad_files = []
		self._ivy_matcher = re.compile("^ivy-%s.xml$" % dpp13numbers)
		self._general_matcher = re.compile("^[-\w]+-%s.[a-z]+$" % dpp13numbers)
		self.project_name = project_name

	def add_build_for_file(self, ivyfile):
		match = re.match(self._ivy_matcher, ivyfile)
		if match:
			mtime = os.path.getmtime(os.path.join(root_dir, self.project_name, ivyfile))
			filestamp = datetime.datetime.fromtimestamp(mtime)
			build_list = self.get_build_list(match.groupdict())
			build_list.add_build(match.group(BUILD_NUMBER), filestamp)

	def add_file_to_build(self, general_file):
		match = re.match(self._general_matcher, general_file)
		if match:
			version = match.groupdict()
			build = self.get_build_list(version, True).get_build(version[BUILD_NUMBER])
			build.add_file(general_file)
		else:
			self._bad_files.append(general_file)

	def get_path(self, filename):
		return os.path.join(root_dir, self.project_name, filename)

	def get_revisions(self, major=None, minor=None, patchlevel=None):
		if major is None:
			major_revs = self._h.values()
		else:
			major_revs = [self._h[int(major)]]
		# major_revs now is a list of hashes from int to hash of int to build_collection
		if minor is None:
			minor_revs = [ r.values() for r in major_revs ]
		else:
			int_minor = int(minor)
			minor_revs = [ [r[int_minor] for r in major_revs if int_minor in r ]]
		# minor_revs is now a list of hashes from int to build_collection
		build_list = [] # inefficient as hell
		for r in itertools.chain.from_iterable(minor_revs):
			if patchlevel is None:
				build_list.extend(r.values())
			elif int(patchlevel) in r:
				build_list.append(r[int(patchlevel)])
		return build_list

	def get_build_list(self, keydict, read_only=False):
		current_level = self._h
		needsall = False
		major_version = int(keydict[MAJOR])
		minor_version = int(keydict[MINOR])
		patch_level = int(keydict[PATCHLEVEL])
		if major_version not in current_level:
			if read_only:
				raise Exception("Major version %s of %s never built"
					% (major_version, self.project_name))
			current_level[major_version] = {}
			needsall = True
		current_level = current_level[major_version]
		if needsall or minor_version not in current_level:
			if read_only:
				raise Exception("Minor version %s.%s of %s never built"
					% (major_version, minor_version, self.project_name))
			current_level[minor_version] = {}
			needsall = True
		current_level = current_level[minor_version]
		if needsall or patch_level not in current_level:
			if read_only:
				raise Exception("Patchlevel %s.%s.%s of %s never built"
					% (major_version, minor_version, patch_level, self.project_name))
			current_level[patch_level] = patchlevel(self, keydict)
		return current_level[patch_level]

	def bad_file_names(self):
		return self._bad_files

	def bad_file_paths(self):
		return [self.get_path(filename) for filename in self._bad_files]

def clean(build_collection, min_keep_days=7, always_keep_latest=True):
	latest_build = None
	now = datetime.datetime.now()
	is_old = {}

	for build in build_collection.builds:
		if latest_build is None or latest_build.get_number() < build.get_number():
			latest_build = build
		build_age = (now - build.get_timestamp()).days
		is_old[build] = (build_age > min_keep_days)

	# now loop again, and use that information
	for build in build_collection.builds:
		if build == latest_build and always_keep_latest:
			print "Keeping build %s (latest)" % build.get_number()
		elif is_old[build]:
			print "Removing build %s" % build.get_number()
			for filename in build.get_file_paths():
				print "rm %s" % filename
		else:
			print "Keeping build %s (below age cutoff)" % build.get_number()

def main(module_name, build_to_dump=None):
	now = datetime.datetime.now()
	allfiles = os.listdir(os.path.join(root_dir, module_name))
	ivyfiles = [f for f in allfiles if f.startswith("ivy-")]

	revision_holder = project_build_holder(module_name)

	for ivyfile in ivyfiles:
		revision_holder.add_build_for_file(ivyfile)

	for patchlevel_object in revision_holder.get_revisions():
		latest_build = patchlevel_object.latest_build()
		latest_age = now - latest_build.get_timestamp()
		print "Revision %s has %s builds (%s is latest, at %s days old)" % (
			patchlevel_object.version_string(),
			patchlevel_object.build_count(), latest_build.get_number(), latest_age.days
		)

	for general_file in allfiles:
		revision_holder.add_file_to_build(general_file)

	print "Non-matching files: "
	for bad_path in revision_holder.bad_file_names():
		print bad_path

	if build_to_dump:
		print "Dumping requested build files:"
		patchlevel = revision_holder.get_build_list(
			{MAJOR:build_to_dump[0], MINOR:build_to_dump[1], PATCHLEVEL: build_to_dump[2]},
			True)
		build = patchlevel.get_build(build_to_dump[3])
		for file_name in build.get_file_paths():
			print file_name
		clean(patchlevel)

if __name__ == "__main__":
	# to debug:
	#pdb.runcall(main)
	modulename = "wgspringmodule-userappstate"
	toDump = None
	if 1 != len(sys.argv):
		modulename = sys.argv[1]
		if 6 == len(sys.argv):
			toDump = sys.argv[2:6]
	main(modulename, toDump)
