#!/usr/bin/python
import os, shutil

# recursively find a file in the given directory
def find_file(directory, requiredFileNameWithRelativePath):
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            fullFilePath = os.path.join(root, filename)
            if fullFilePath.endswith(requiredFileNameWithRelativePath):
                return fullFilePath


def copy_and_overwrite(rootSrcDir, rootDstDir):
    for srcDir, dirs, files in os.walk(rootSrcDir):
        dstDir = srcDir.replace(rootSrcDir, rootDstDir)
        if not os.path.exists(dstDir):
            os.makedirs(dstDir)
        for jsfile in files:
            srcFile = os.path.join(srcDir, jsfile)
            dstFile = os.path.join(dstDir, jsfile)
            if os.path.exists(dstFile):
                os.remove(dstFile)
            shutil.copy(srcFile, dstDir)
