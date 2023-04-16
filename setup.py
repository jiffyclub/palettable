from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='palettable',
    version='3.4.0.dev.0',
    description=(
        'Color palettes for Python'),
    long_description=long_description,
    author='Matt Davis',
    author_email='jiffyclub@gmail.com',
    url='https://jiffyclub.github.io/palettable/',
    packages=find_packages(exclude=["*.test"]),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Visualization'],
    python_requires=">=3.7",
    )
