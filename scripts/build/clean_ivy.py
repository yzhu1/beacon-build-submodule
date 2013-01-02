#!/usr/bin/python

import re
import os
import os.path
import optparse
import pdb
import sys

MAJOR = 'major'
MINOR = 'minor'
PATCHLEVEL = 'patch'
BUILD_NUMBER = 'build'

dpp13numbers = "(?P<%s>\d+)\.(?P<%s>\d+)\.(?P<%s>\d+)-(?P<%s>\d+)" % (
    MAJOR, MINOR, PATCHLEVEL, BUILD_NUMBER
)

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
		current_level[keydict[PATCHLEVEL]] = []
	return current_level[keydict[PATCHLEVEL]]

def main(module_name):
	allfiles = os.listdir("/opt/wgen/ivy/wgen/" + module_name)
	ivyfiles = [f for f in allfiles if f.startswith("ivy-")]

	ivymatcher = re.compile("^ivy-%s.xml$" % dpp13numbers)
	badfiles = []
	revision_map = {}

	for ivyfile in ivyfiles:
		match = re.match(ivymatcher,ivyfile)
		if match:
			build_list = get_build_list(revision_map, match.groupdict())
			build_list.append(int(match.group(BUILD_NUMBER)))
		else:
			badfiles.append(ivyfile)

	for top_level_tuple in revision_map.items():
		(major_revision, minor_revision_map) = top_level_tuple
		for minor_level_tuple in minor_revision_map.items():
			(minor_revision, patchlevel_map) = minor_level_tuple
			for patchlevel_tuple in patchlevel_map.items():
				(patchlevel, builds) = patchlevel_tuple
				latest_build = max(builds)
				build_count = len(builds)
				print "Revision %s.%s.%s has %s builds (%s is latest)" % (
				    major_revision, minor_revision, patchlevel, build_count, latest_build
				)

	print "Non-matching files: "
	print badfiles

if __name__ == "__main__":
	# to debug:
	#pdb.runcall(main)
	modulename = "wgspringmodule-userappstate"
	if 1 != len(sys.argv):
		modulename = sys.argv[1]
	main(modulename)
