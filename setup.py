#!/usr/bin/env python
from distutils.core import setup

with open('README.rst', 'r') as f:
      long_description = f.read()

setup(name='brewer2mpl',
      version='1.3.2',
      description='Connect colorbrewer2.org color maps to Python and matplotlib',
      long_description=long_description,
      author='Matt Davis',
      author_email='jiffyclub@gmail.com',
      url='https://github.com/jiffyclub/brewer2mpl/wiki',
      packages=['brewer2mpl'],
      package_data={'brewer2mpl': ['data/colorbrewer*']},
      classifiers=['License :: OSI Approved :: MIT License',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering :: Visualization'])
