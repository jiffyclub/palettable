"""
Sequential color maps from the CartoColors schemes:
https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names
"""
from __future__ import absolute_import

from . import cartocolorspalette
from . import colormaps
from .. import utils

_PALETTE_TYPE = 'sequential'
_NAMES_TO_DATA = {
    'Burg': colormaps._BURG,
    'BurgYl': colormaps._BURGYL,
    'RedOr': colormaps._REDOR,
    'OrYel': colormaps._ORYEL,
    'Peach': colormaps._PEACH,
    'PinkYl': colormaps._PINKYL,
    'Mint': colormaps._MINT,
    'BluGrn': colormaps._BLUGRN,
    'DarkMint': colormaps._DARKMINT,
    'Emrld': colormaps._EMRLD,
    'agGrnYl': colormaps._AGGRNYL,
    'BluYl': colormaps._BLUYL,
    'Teal': colormaps._TEAL,
    'TealGrn': colormaps._TEALGRN,
    'Purp': colormaps._PURP,
    'PurpOr': colormaps._PURPOR,
    'Sunset': colormaps._SUNSET,
    'Magenta': colormaps._MAGENTA,
    'SunsetDark': colormaps._SUNSETDARK,
    'agSunset': colormaps._AGSUNSET,
    'BrwnYl': colormaps._BRWNYL,
}
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    sorted(_NAMES_TO_DATA.keys()),
    range(2, 8))


print_maps = utils.print_maps_factory(
    'sequential cartocolors', _NAMES_AND_LENGTHS, _PALETTE_TYPE)
get_map = utils.get_map_factory(
    'sequential cartocolors', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    cartocolorspalette.CartoColorsMap)


globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
