from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='brewer2mpl',
    version='1.4.1',
    description=(
        'Connect colorbrewer2.org color maps to Python and matplotlib'),
    long_description=long_description,
    author='Matt Davis',
    author_email='jiffyclub@gmail.com',
    url='https://github.com/jiffyclub/brewer2mpl/wiki',
    packages=['brewer2mpl', 'brewer2mpl.wesanderson'],
    package_data={'brewer2mpl': ['data/colorbrewer*']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization'])
