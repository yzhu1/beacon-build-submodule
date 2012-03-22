import os
import sets
import sys

# Given the directory argument, 
filePrefix = os.getcwd() + sys.argv[1]
fileset = sets.Set()
duplicateDetected = False;
for path, dirs, files in os.walk(filePrefix):

    # Append to the file to the path minus the root directory
    filepath = path;
    filepath = filepath[len(filePrefix) + 1:]
    filepath = filepath[filepath.find("/"):]
    for index in range(0, len(files)):
        files[index] = filepath + "/" + files[index]

    # Look for any intersection between previously examined files and the next set    
    intersection = fileset.intersection(files) 
    if ((intersection is not None) and len(intersection) > 0):
        duplicateDetected = True
        break
    else:
        fileset.update(files)

# If a duplicate was found, return 1, else 0
sys.exit(1 if duplicateDetected else 0)