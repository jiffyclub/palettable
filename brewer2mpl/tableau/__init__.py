from __future__ import absolute_import

from .tableau import __doc__, print_maps, get_map, _get_all_maps

globals().update(_get_all_maps())
