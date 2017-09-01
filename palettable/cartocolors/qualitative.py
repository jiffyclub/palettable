"""
Qualitative color maps from the CartoColors schemes:
https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names
"""
from __future__ import absolute_import

import itertools

from . import cartocolorspalette
from . import colormaps
from .. import utils

_PALETTE_TYPE = 'qualitative'
_NAMES_TO_DATA = {
    'Antique': colormaps._ANTIQUE,
    'Bold': colormaps._BOLD,
    'Pastel': colormaps._PASTEL,
    'Prism': colormaps._PRISM,
    'Safe': colormaps._SAFE,
    'Vivid': colormaps._VIVID,
}

_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(sorted(_NAMES_TO_DATA.keys()),
                                                  range(2, 11))


print_maps = utils.print_maps_factory('qualitative cartocolors',
                                      _NAMES_AND_LENGTHS,
                                      _PALETTE_TYPE)

get_map = utils.get_map_factory('qualitative cartocolors',
                                __name__,
                                _NAMES_TO_DATA,
                                _PALETTE_TYPE,
                                cartocolorspalette.CartoColorsMap,
                                is_evenly_spaced=False)


globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
