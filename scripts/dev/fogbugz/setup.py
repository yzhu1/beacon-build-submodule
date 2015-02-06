try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(
      name='FogbugzCLI',
      version='1.0.0',
      author='Ankit Goswami',
      author_email='ankit.goswami@gmail.com',
      scripts=['fbcli.py'],
      url='https://dmc270.mc.wgenhq.net/index.php/3-12_Platform/Development/Fogbugz_CLI#Fogbugz_Command_line_interface',
      license='amplify',
      description='Command line interface for FogBugz',
      long_description=open('README.txt').read(),
      license='MIT',

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: FogBugz :: Command line tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7'
      ],
      
      keywords='Command line interface FogBugz',
      
      install_requires=[
                        "requests",
                        "fogbugz",
                        ],
      packages=['fbcli'],
      entry_points={
          'console_scripts': [
              'fbcli=fbcli:main',
          ],
      },
)