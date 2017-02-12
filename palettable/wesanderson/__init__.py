from __future__ import absolute_import

from .wesanderson import __doc__, _palettes, print_maps, get_map, _get_all_maps


globals().update(_get_all_maps())
