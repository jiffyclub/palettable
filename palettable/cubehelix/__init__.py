from __future__ import absolute_import

from .cubehelix import __doc__, Cubehelix, print_maps, get_map, _get_all_maps

globals().update(_get_all_maps())
