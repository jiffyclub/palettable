"""
brewer2mpl is a pure Python package for accessing
colorbrewer2.org color maps from Python. With brewer2mpl you can get the
raw RGB colors of all 165 colorbrewer2.org color maps.

"""
from .colorbrewer import *
from . import wesanderson
from . import tableau

version = __version__ = '1.5dev'
