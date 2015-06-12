#!/usr/bin/python
import asset_processing_settings as settings
import asset_processor_utils as utils
import os, sys, shutil, glob

# combines all files in jsFilesList into one file
def create_combined_js_file(jsFilesList, appStaticDir, buildWebAssetsDir, fileVersion, manifestFileName):
    # directory which contains the app specific js files
    jsDir = os.path.join(appStaticDir, settings.JS_DIR)
    # directory which contains the js files from common projects
    commonJSDir = os.path.join(buildWebAssetsDir, settings.UNZIP_DIR)
    # directory from where javascript files would be served to apache
    minifiedJSDir = os.path.join(buildWebAssetsDir, settings.COMPILE_DIR, settings.JS_DIR)
    utils.copy_and_overwrite(jsDir, minifiedJSDir) #in case we want to use unminified individual files
    tempCombinedFilePath = manifestFileName + settings.JS_EXT
    minifiedFilePath = os.path.join(minifiedJSDir, manifestFileName + settings.FILENAME_SEPARATOR + fileVersion + settings.JS_EXT)
    tempCombinedFile = open(tempCombinedFilePath, 'w+')
    for jsFileName in jsFilesList:
        # search for the files in both application and common js directories
        filePath = os.path.join(jsDir, jsFileName + settings.JS_EXT)
        commonFilePath = utils.find_file(commonJSDir, jsFileName + settings.JS_EXT)
        found = False;
        if os.path.isfile(filePath):
            jsFile = open(filePath)
            found  = True;
        elif commonFilePath is not None:
            jsFile = open(commonFilePath)
            found  = True;
        if not found:
            raise Exception("javascript file " + jsFileName + " not found!")
        shutil.copyfileobj(jsFile, tempCombinedFile)
        jsFile.close()
    tempCombinedFile.close()
    yuiJarName = glob.glob('ivy_lib/build/yuicompressor*.jar')[0]
    os.system('java -jar ' + yuiJarName + ' ' + tempCombinedFilePath + ' -o ' + minifiedFilePath)
    print('Created combined and minified js file: ' + minifiedFilePath)
    os.remove(tempCombinedFilePath)
