#!/usr/bin/python

import sys, os
import asset_processing_settings as settings

app_static_dir = sys.argv[1]
rpm_version = sys.argv[2]
build_web_assets_dir = sys.argv[3]
manifest_dir = app_static_dir + settings.MANIFEST_DIR

asset_map = {}

for manifest_file_name in os.listdir(manifest_dir):
    if manifest_file_name.endswith(settings.MANIFEST_EXT):
        manifest_file = open(manifest_dir + manifest_file_name)
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
            settings.PROCESSORS[extension](asset_map[extension], app_static_dir, build_web_assets_dir, rpm_version, os.path.splitext(manifest_file_name)[0])

