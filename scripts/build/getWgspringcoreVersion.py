#!/usr/bin/python

import os
import re

if __name__ == '__main__':

    for jar in os.listdir('ivy_lib/compile'):
        if 'wgspringcore-app-src' in jar:
            wgspringcoreVersion = re.search('src-.*?\.jar', jar).group()[4:-4]
            print wgspringcoreVersion
            break
