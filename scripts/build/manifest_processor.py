#!/usr/bin/python

import sys, os
import asset_processing_settings as settings

app_web_dir = sys.argv[1]
rpm_version = sys.argv[2]
build_web_assets_dir = sys.argv[3]
manifest_dir = os.path.join(app_web_dir, sys.argv[4])
build_number = sys.argv[5]

app_static_dir = os.path.join(app_web_dir, settings.STATIC_DIR)
file_version = rpm_version + settings.FILENAME_SEPARATOR + build_number

for manifest_file_name in os.listdir(manifest_dir):
    if not manifest_file_name.endswith(settings.ASSET_MANIFEST_EXT):
        continue
    print('Reading asset file: ' + manifest_file_name)
    manifest_file = open(os.path.join(manifest_dir, manifest_file_name))
    asset_map = {}
    for asset in manifest_file:
        asset = asset.strip()
        if len(asset) == 0 or asset.startswith('#'):
            continue
        filename, file_extension = os.path.splitext(asset)
        if file_extension not in settings.PROCESSORS.keys():
            raise Exception(file_extension + " files are not supported!")
        if file_extension not in asset_map:
	        asset_map[file_extension] = []
        asset_map[file_extension].append(filename)
    manifest_file.close()
    for extension in asset_map.keys():
        settings.PROCESSORS[extension](asset_map[extension], app_static_dir, build_web_assets_dir, file_version, manifest_file_name)
print ("""                         __
               _.--\"\"  |
.----.     _.-'   |/\| |.--.
|    |__.-'   _________|  |_)  _______________  
|  .-\"\"-.\"\"\"\"\" ___,    `----'\"))   __   .-\"\"-.\"\"\"\"--._  
'-' ,--. `    Beacon  .---.       |:.| ' ,--. `      _`.
 ( (    ) ) __Assess__ \\|// _..--  \/ ( (    ) )--._\".-.
  . `--' ;\__________________..--------. `--' ;--------'
   `-..-'                               `-..-'
""")
