"""
Palettable is a pure Python package for accessing
a variety of color maps from Python, including colorbrewer2,
Tableau, and whimsical Wes Anderson maps.

"""
from __future__ import absolute_import

from . import cmocean
from . import colorbrewer
from . import cubehelix
from . import matplotlib
from . import mycarta
from . import wesanderson
from . import tableau

version = __version__ = '3.1.0.dev.0'
