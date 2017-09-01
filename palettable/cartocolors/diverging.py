"""
Diverging color maps from the CartoColors schemes:
https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names
"""
from __future__ import absolute_import

import itertools

from . import cartocolorspalette
from . import colormaps
from .. import utils

_PALETTE_TYPE = 'diverging'
_NAMES_TO_DATA = {
        'ArmyRose': colormaps._ARMYROSE,
        'Fall': colormaps._FALL,
        'Geyser': colormaps._GEYSER,
        'Temps': colormaps._TEMPS,
        'TealRose': colormaps._TEALROSE,
        'Tropic': colormaps._TROPIC,
        'Earth': colormaps._EARTH,
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    sorted(_NAMES_TO_DATA.keys()),
    range(2, 8))


print_maps = utils.print_maps_factory(
    'diverging cartocolors', _NAMES_AND_LENGTHS, _PALETTE_TYPE)
get_map = utils.get_map_factory(
    'diverging cartocolors', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    cartocolorspalette.CartoColorsMap)


globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
