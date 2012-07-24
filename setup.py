#!/usr/bin/env python
from distutils.core import setup

setup(name='brewer2mpl',
      version='1.0dev',
      description='Connect colorbrewer2.org color maps to Python and matplotlib',
      author='Matt Davis',
      url='https://github.com/jiffyclub/brewer2mpl/wiki',
      packages=['brewer2mpl'],
      package_data={'brewer2mpl': ['data/colorbrewer*']},
      classifiers=['License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Visualization'])
