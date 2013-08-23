#!/usr/bin/python

import re
import os
import os.path
import optparse
import pdb
import sys
import datetime

MAJOR = 'major'
MINOR = 'minor'
PATCHLEVEL = 'patch'
BUILD_NUMBER = 'build'

root_dir = "/opt/wgen/ivy/wgen"
dpp13numbers = "(?P<%s>\d+)\.(?P<%s>\d+)\.(?P<%s>\d+)-(?P<%s>\d+)" % (
    MAJOR, MINOR, PATCHLEVEL, BUILD_NUMBER
)
dpp13format = "%s.%s.%s-%s"
now = datetime.datetime.now()
class patchlevel(object):
	def __init__(self,dict=None,major=None,minor=None,patchlevel=None):
		if dict:
			self.major = dict[MAJOR]
			self.minor = dict[MINOR]
			self.patchlevel = dict[PATCHLEVEL]
		else:
			self.major = major
			self.minor = minor
			self.patchlevel = patchlevel
		self.builds = []

	def version_string(self):
		return "%s.%s.%s" % (self.major, self.minor, self.patchlevel)

	def add_build(self,build_number,timestamp):
		self.builds.append({BUILD_NUMBER : int(build_number), "TIMESTAMP":timestamp, "FILES": []})

	def get_build(self, build_number):
		numeric_build_number = int(build_number)
		for build in self.builds:
			if build[BUILD_NUMBER] == numeric_build_number:
				return build
		raise Exception("Could not find build %s for patchlevel %s" % (build_number, self.version_string()))

	def latest_build(self):
		latest = self.builds[0]
		for build in self.builds:
			if build[BUILD_NUMBER] > latest[BUILD_NUMBER]:
				latest = build
		return latest

	def build_count(self):
		return len(self.builds)

def get_build_list(h, keydict):
	current_level = h
	needsall = False
	if keydict[MAJOR] not in current_level:
		current_level[keydict[MAJOR]] = {}
		needsall = True
	current_level = current_level[keydict[MAJOR]]
	if needsall or keydict[MINOR] not in current_level:
		current_level[keydict[MINOR]] = {}
		needsall = True
	current_level = current_level[keydict[MINOR]]
	if needsall or keydict[PATCHLEVEL] not in current_level:
		current_level[keydict[PATCHLEVEL]] = patchlevel(keydict)
	return current_level[keydict[PATCHLEVEL]]

def main(module_name, build_to_dump=None):
	allfiles = os.listdir(os.path.join(root_dir, module_name))
	ivyfiles = [f for f in allfiles if f.startswith("ivy-")]

	ivymatcher = re.compile("^ivy-%s.xml$" % dpp13numbers)
	generalmatcher = re.compile("^[-\w]+-%s.[a-z]+$" % dpp13numbers)
	badfiles = []
	revision_map = {}

	for ivyfile in ivyfiles:
		match = re.match(ivymatcher,ivyfile)
		if match:
			mtime = os.path.getmtime(os.path.join(root_dir, module_name, ivyfile))
			filestamp = datetime.datetime.fromtimestamp(mtime)
			build_list = get_build_list(revision_map, match.groupdict())
			build_list.add_build(int(match.group(BUILD_NUMBER)), filestamp)
		else:
			badfiles.append(ivyfile)

	for top_level_tuple in revision_map.items():
		(major_revision, minor_revision_map) = top_level_tuple
		for minor_level_tuple in minor_revision_map.items():
			(minor_revision, patchlevel_map) = minor_level_tuple
			for patchlevel_tuple in patchlevel_map.items():
				(patch_level, patchlevel_object) = patchlevel_tuple
				latest_build = patchlevel_object.latest_build()
				latest_age = now - latest_build["TIMESTAMP"]
				print "Revision %s has %s builds (%s is latest, at %s days old)" % (
				    patchlevel_object.version_string(),
				    patchlevel_object.build_count(), latest_build[BUILD_NUMBER], latest_age.days
				)

	for general_file in allfiles:
		match = re.match(generalmatcher, general_file)
		if match:
			version = match.groupdict()
			build = get_build_list(revision_map, version).get_build(version[BUILD_NUMBER])
			build["FILES"].append(general_file)

	print "Non-matching files: "
	print badfiles
	if build_to_dump:
		print "Dumping requested build files:"
		patchlevel = get_build_list(revision_map, {MAJOR:build_to_dump[0], MINOR:build_to_dump[1], PATCHLEVEL: build_to_dump[2]})
		build = patchlevel.get_build(build_to_dump[3])
		for file_name in build["FILES"]:
			print file_name

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
