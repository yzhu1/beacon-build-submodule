import css_processor

CSS_DIR = 'css'
STATIC_DIR = 'static'
SASS_EXT = ".scss"
ASSET_MANIFEST_EXT = '.assets'
FILENAME_SEPARATOR = '_'
PROCESSORS = {SASS_EXT:css_processor.create_combined_sass_file
                }
