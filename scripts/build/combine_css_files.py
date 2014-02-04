#!/usr/bin/python

import sys
import os

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
        relDir = os.path.relpath(dir_, cssDir)
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


