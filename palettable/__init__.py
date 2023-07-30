"""
Palettable is a pure Python package for accessing
a variety of color maps from Python, including colorbrewer2,
Tableau, and whimsical Wes Anderson maps.

"""
from __future__ import absolute_import

from . import cmocean
from . import cartocolors
from . import colorbrewer
from . import cubehelix
from . import lightbartlein
from . import matplotlib
from . import mycarta
from . import plotly
from . import scientific
from . import tableau
from . import wesanderson

VERSION = version = __version__ = '3.4.0.dev.0'
