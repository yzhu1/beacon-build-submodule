'''python port of rebuild_eclipse_classpath.sh

From the original notes:

# Scans ivy_lib/ and generates a .classpath file (which you should gitignore) for eclipse to use.
# This is an alternative to using the IvyDE plugin.  This scripts gets invoked at the end of
# ivy-resolve if you have use.eclipse.ivyde.plugin=false in your build.properties.

# To set use.eclipse.ivyde.plugin=false everywhere:
#   find $THREETWELVE_HOME/.. -name build.properties -exec sh -c "echo use.eclipse.ivyde.plugin=false >> {}" \;
'''

import sys
import os
import xml.dom.minidom as minidom
import re

IVY_LIB = "ivy_lib"
DEFAULT_HEADER = "conf/base/scripts/dev/eclipse.classpath.header"
DEBUG = False
RE_JARNAME = re.compile(r'^([a-z0-9\-]+)\-([0-9\.]+)\.jar$')

def _grep_src_dirs(dom):
    class_path_entries = dom.getElementsByTagName("classpathentry")
    src_paths = []
    for entry in class_path_entries:
        kind = entry.getAttribute("kind")
        if kind == "src":
            src_paths.append(entry.getAttribute("path"))
    return src_paths
            

def _create_missing_directories(dom):
    src_dirs = _grep_src_dirs(dom)    
    for src_dir in src_dirs:
        if DEBUG: print src_dir
        if not os.path.exists(src_dir):
            print "mkdir ", src_dir
            os.makedirs(src_dir)

class JarFile:
    def __init__(self, path=None, source_path=None, version=None):
        self.path = path
        self.source_path = source_path
        self.version = None

def _is_greater_version(v1, v2):
    parts1 = v1.split(".")
    parts2 = v2.split(".")
    if len(parts1) != len(parts2):
        if DEBUG: print "WARN: part length doesn't match", v1, v2
        if v1 == "development" and v2 != "development":
            return True
        return False # undecidable
    for i, p1 in enumerate(parts1):
        p2 = parts2[i]
        if int(p1) > int(p2):
            return True
        if int(p2) > int(p1):
            return False
    return False        
    
def _find_unique_jars():
    # TODO: make this elegant, total sprawl right now
    seen_source_jars = {}
    jars_by_version = {}
    for root, dirs, files in os.walk(IVY_LIB):
        for file in files:
            if file.endswith(".jar") and file.find("-src-") == -1:
                m = RE_JARNAME.match(file)
                if m:
                    basename = m.group(1)
                    version = m.group(2)
                    if DEBUG: print version, basename
                    if basename in jars_by_version:
                        latest_max_version = jars_by_version[basename]
                        if _is_greater_version(version, latest_max_version):
                            if DEBUG: print "greater version of ", basename
                            jars_by_version[basename] = version
                    else:
                        jars_by_version[basename] = version
    
    for root, dirs, files in os.walk(IVY_LIB):
        for file in files:
            if file.endswith(".jar") and file.find("-src-") > -1:
                basefile = file.replace("-src-", "-")
                if DEBUG: print "basefile", basefile
                if basefile not in seen_source_jars:
                    seen_source_jars[basefile] = file
                
    seen_jars = []
    jars = []
    for root, dirs, files in os.walk(IVY_LIB):
        for file in files:
            if file.endswith(".jar") and file.find("-src-") == -1:
                m = RE_JARNAME.match(file)
                if m:
                    basename = m.group(1)
                    version = m.group(2)
                    if jars_by_version[basename] != version:
                        continue
                if file not in seen_jars:
                    if DEBUG: print root, file
                    source_file = None
                    if file in seen_source_jars:
                        source_file = seen_source_jars[file]                    
                        if DEBUG: print "source: ", source_file
                    seen_jars.append(file)
                    jar = JarFile(path= root + "/" + file)
                    if source_file:
                        jar.source_path = root + "/" + source_file
                    jars.append(jar)
    return jars
    
def _write_classpathfile(dom):    
    if DEBUG:
        print "writing to .classpath"        
    classpathfile = open(".classpath", "w")
    classpathfile.write(dom.toprettyxml())
    classpathfile.close()
    
if __name__ == '__main__':
    import optparse
    p = optparse.OptionParser(__doc__)
    p.add_option("-d", "--debug", action="store_true", dest="debug", help="enable debug output")
    
    (opts, args) = p.parse_args()
    
    header = DEFAULT_HEADER
    # Optional second parameter is a file to use for the header (project-specific source
    # directories, etc., starting from "<?xml...")
    if len(args) == 1:
        if os.path.exists(args[0]):
            header = args[0]
    DEBUG = opts.debug
    if DEBUG:
        print "rebuilding eclipse classpath using header ", header
    header_str = open(header).read()
    header_str += "</classpath>"
    dom = minidom.parseString(header_str)
    _create_missing_directories(dom)
    jars = _find_unique_jars()
    cpNode= dom.getElementsByTagName("classpath")[0]
    for jar in jars:
        cpEntry = dom.createElement("classpathentry")
        cpEntry.setAttribute("kind", "lib")
        cpEntry.setAttribute("path", jar.path)
        if jar.source_path != None:
            cpEntry.setAttribute("sourcepath", jar.source_path)
        cpNode.appendChild(cpEntry)
    _write_classpathfile(dom)


