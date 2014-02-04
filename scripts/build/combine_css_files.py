#!/usr/bin/python

import sys, os
from posixpath import curdir, sep, pardir, join, abspath, commonprefix

# Using this implementation of os.path.relpath because it does not exist in python 2.5, that is used by our build slaves.
# This function is copied from http://www.saltycrane.com/blog/2010/03/ospathrelpath-source-code-python-25/
def relpath(path, start=curdir):
    """Return a relative version of a path"""
    if not path:
        raise ValueError("no path specified")
    start_list = abspath(start).split(sep)
    path_list = abspath(path).split(sep)
    # Work out how much of the filepath is shared by start and path.
    i = len(commonprefix([start_list, path_list]))
    rel_list = [pardir] * (len(start_list)-i) + path_list[i:]
    if not rel_list:
        return curdir
    return join(*rel_list)

cssDir = sys.argv[1] + '/src/main/webapp/static/css'
tabletDirName = 'tablet/'
allStylesFilename = 'compressed_stylesheets_'+sys.argv[2]+'.scss'

# Delete the existing SCSS file with the combined CSS
allStylesFilePath = os.path.join(cssDir, allStylesFilename)
try:
    os.remove(allStylesFilePath)
except OSError:
    pass

# Get relative paths of all CSS files in the the CSS directory and its subdirectories.
fileSet = set()
for dir_, _, files in os.walk(cssDir):
    for filename in files:
        relDir = relpath(dir_, cssDir)
        relFile = os.path.join(relDir, filename)
        fileSet.add(relFile)

# Write the output to a new SCSS file
allStylesFile = open(allStylesFilePath, 'w+')

for filePath in fileSet:
    if tabletDirName in filePath: continue
    if filePath.endswith('.css') or filePath.endswith('.scss'):
        if filePath.startswith('./'):
            filePath = filePath[2:]
        filename, fileExtension = os.path.splitext(filePath)
        os.rename(os.path.join(cssDir, filePath), os.path.join(cssDir, filename+'.scss'))
        allStylesFile.write('@import "' + filename + '";\n')
allStylesFile.close()


