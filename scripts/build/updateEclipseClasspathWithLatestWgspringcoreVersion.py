#!/usr/bin/python

# updates .classpath with the latest version of wgspringcore found in ivy_lib/compile

import os
import re

if __name__ == '__main__':

    for jar in os.listdir('ivy_lib/compile'):
        if 'wgspringcore-app-src' in jar:
            wgspringcoreVersion = re.search('src-.*?\..*?\..*?\.', jar).group()[4:-1]
            cp = open('.classpath', 'r').read()
            cp = re.sub('wgspringcore-.*?-.*?\..*?\..*?\.jar', lambda match: '-'.join(match.group().split('-')[:-1]) + '-%s.jar' % wgspringcoreVersion, cp)
            open('.classpath', 'w').write(cp)
            break
