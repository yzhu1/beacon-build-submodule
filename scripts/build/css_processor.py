#!/usr/bin/python
from __future__ import print_function, with_statement
import asset_processing_settings as settings
import os, sys
import re

# counts the number of css selectors in css files. Does not handle sass files.
def count_css_selectors(fileName):
    count = 0;
    patternRules = '([^\{]+\{(?:[^\{\}]|\{[^\{\}]*\})*\})'
    patternSelectors = '(?:\s*@media\s*[^\{]*(\{))?(?:\s*(?:[^,\{]*(?:(,)|(\{)(?:[^\}]*\}))))' #also looks inside media queries
    commentsPattern = '(\/\*[^*]*\*+([^/*][^*]*\*+)*\/)'
    with open (fileName, "r") as cssFile:
        data = cssFile.read()
        rules = re.findall(patternRules, data)
        for rule in rules:
            # remove comments
            rule = re.sub(commentsPattern, '', rule)
            selectorMatches = re.findall(patternSelectors, rule)
            for selectorMatch in selectorMatches:
                count = count + len(selectorMatches)
    return count;

# for all the css files in stylesFileList, changes the extension to scss and imports all in a new scss file
# and compiles the combined scss file using sass
def create_combined_sass_file(stylesFileList, appStaticDir, buildWebAssetsDir, rpmVersion, manifestFileName):
    cssDir = os.path.join(appStaticDir, settings.CSS_DIR)
    outputFilePath = os.path.join(cssDir, manifestFileName + settings.FILENAME_SEPARATOR + rpmVersion + settings.SASS_EXT)
    outputFile = open(outputFilePath, 'w+')
    for stylesFileName in stylesFileList:
        print('@import "' + stylesFileName + '";', file=outputFile)
    outputFile.close()
    os.system('sass --update ' + cssDir + ':' + buildWebAssetsDir + '/compile/css' + ' --style compressed ')
    compileStylesheet = os.path.join(buildWebAssetsDir, 'compile', 'css', manifestFileName + settings.FILENAME_SEPARATOR + rpmVersion + '.css')
    totalSelectorsCount = count_css_selectors(compileStylesheet)
    print('Total styles count for compiled css file: ' + str(totalSelectorsCount))
    if (totalSelectorsCount > 4095):
        raise Exception("selectors count is over 4095 limit for IE!")
    os.remove(outputFilePath)

