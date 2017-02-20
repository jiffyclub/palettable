"""
Diverging color maps from the cmocean package:
https://github.com/matplotlib/cmocean.

"""
from __future__ import absolute_import

import itertools

from . import cmoceanpalette
from . import colormaps
from .. import utils

_PALETTE_TYPE = 'diverging'
_NAMES_TO_DATA = {
    'Balance': colormaps._BALANCE,
    'Curl': colormaps._CURL,
    'Delta': colormaps._DELTA,
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    sorted(_NAMES_TO_DATA.keys()))


print_maps = utils.print_maps_factory(
    'diverging cmocean', _NAMES_AND_LENGTHS, _PALETTE_TYPE)
get_map = utils.get_map_factory(
    'divergine cmocean', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    cmoceanpalette.CmoceanMap)


globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
