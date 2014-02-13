#!/usr/bin/python

import sys, os
import asset_processing_settings as settings

app_web_dir = sys.argv[1]
app_static_dir = os.path.join(app_web_dir, settings.STATIC_DIR)
rpm_version = sys.argv[2]
build_web_assets_dir = sys.argv[3]
manifest_dir = os.path.join(app_web_dir, sys.argv[4])


for manifest_file_name in os.listdir(manifest_dir):
    print('Reading asset file: ' + manifest_file_name)
    if not manifest_file_name.endswith(settings.ASSET_MANIFEST_EXT):
        continue
    manifest_file = open(os.path.join(manifest_dir, manifest_file_name))
    asset_map = {}
    for asset in manifest_file:
        asset = asset.strip()
        filename, file_extension = os.path.splitext(asset)
        # move to separate method for validating manifest file
        if '.css' in file_extension:
            raise Exception("CSS files are not supported, please change to SCSS")
        if file_extension not in asset_map:
	        asset_map[file_extension] = []
        asset_map[file_extension].append(filename)
    manifest_file.close()
    for extension in settings.PROCESSORS:
        settings.PROCESSORS[extension](asset_map[extension], app_static_dir, build_web_assets_dir, rpm_version, manifest_file_name)

