import css_processor

CSS_DIR = 'css'
ASSET_MANIFEST_EXT = '.assets'
STATIC_DIR = 'static'
FILENAME_SEPARATOR = '_'
PROCESSORS = {'.scss':css_processor.create_combined_sass_file
                }
