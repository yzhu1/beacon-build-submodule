import css_processor
import js_processor

CSS_DIR = 'css'
STATIC_DIR = 'static'
SASS_EXT = '.scss'
JS_DIR = 'js'
JS_EXT = '.js'
ASSET_MANIFEST_EXT = '.assets'
FILENAME_SEPARATOR = '_'
PROCESSORS = {SASS_EXT:css_processor.create_combined_sass_file,
              JS_EXT:js_processor.create_combined_js_file
             }
