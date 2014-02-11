import css_processor

CSS_DIR = '/css/'
MANIFEST_DIR = '/manifest/'
MANIFEST_EXT = '.manifest'
COMBINED_STYLESHEET_PREFIX = '_compressed_'
PROCESSORS = {'.scss':css_processor.create_combined_sass_file
                }
