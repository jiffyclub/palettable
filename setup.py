from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='palettable',
    version='2.0.0',
    description=(
        'Color palettes for Python'),
    long_description=long_description,
    author='Matt Davis',
    author_email='jiffyclub@gmail.com',
    url='https://jiffyclub.github.io/palettable/',
    packages=find_packages(exclude=["*.test"]),
    package_data={'palettable.colorbrewer': ['data/colorbrewer*']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization'])
