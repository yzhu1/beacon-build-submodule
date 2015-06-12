try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(
      name='FogbugzCLI',
      version='0.1.0',
      author='Ankit Goswami',
      author_email='agoswami@amplify.com',
      scripts=['fbcli.py'],
      url='https://dmc270.mc.wgenhq.net/index.php/3-12_Platform/Development/Fogbugz_CLI#Fogbugz_Command_line_interface',
      license='amplify',
      description='Command line interface for FogBugz',
      long_description=open('README.txt').read(),
      install_requires=[
                        "requests",
                        "fogbugz",
                        ],
      )