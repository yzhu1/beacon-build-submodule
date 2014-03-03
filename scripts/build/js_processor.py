#!/usr/bin/python
import asset_processing_settings as settings
import os, sys, shutil, glob

def copy_and_overwrite(rootSrcDir, rootDstDir):
    for srcDir, dirs, files in os.walk(rootSrcDir):
        dstDir = srcDir.replace(rootSrcDir, rootDstDir)
        if not os.path.exists(dstDir):
            os.mkdir(dstDir)
        for jsfile in files:
            srcFile = os.path.join(srcDir, jsfile)
            dstFile = os.path.join(dstDir, jsfile)
            if os.path.exists(dstFile):
                os.remove(dstFile)
            shutil.copy(srcFile, dstDir)

# combines all files in jsFilesList into one file
def create_combined_js_file(jsFilesList, appStaticDir, buildWebAssetsDir, rpmVersion, manifestFileName):
    jsDir = os.path.join(appStaticDir, settings.JS_DIR)
    minifiedJSDir = os.path.join(buildWebAssetsDir, 'compile', settings.JS_DIR)
    copy_and_overwrite(jsDir, minifiedJSDir) #incase we want to use unminified individual files
    tempCombinedFilePath = manifestFileName + settings.JS_EXT
    minifiedFilePath = os.path.join(minifiedJSDir, manifestFileName + settings.FILENAME_SEPARATOR + rpmVersion + settings.JS_EXT)
    tempCombinedFile = open(tempCombinedFilePath, 'w+')
    for jsFileName in jsFilesList:
        jsFile = open(os.path.join(jsDir, jsFileName + settings.JS_EXT))
        shutil.copyfileobj(jsFile, tempCombinedFile)
        jsFile.close()
    tempCombinedFile.close()
    yuiJarName = glob.glob('ivy_lib/build/yuicompressor*.jar')[0]
    os.system('java -jar ' + yuiJarName + ' ' + tempCombinedFilePath + ' -o ' + minifiedFilePath)
    print('Created combined and minified js file: ' + minifiedFilePath)
    os.remove(tempCombinedFilePath)
