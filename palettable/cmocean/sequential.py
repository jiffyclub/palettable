"""
Sequential color maps from the cmocean package:
https://github.com/matplotlib/cmocean.

"""
from __future__ import absolute_import

import itertools

from . import cmoceanpalette
from . import colormaps
from .. import utils

_PALETTE_TYPE = 'sequential'
_NAMES_TO_DATA = {
    'Algae': colormaps._ALGAE,
    'Amp': colormaps._AMP,
    'Deep': colormaps._DEEP,
    'Dense': colormaps._DENSE,
    'Gray': colormaps._GRAY,
    'Haline': colormaps._HALINE,
    'Ice': colormaps._ICE,
    'Matter': colormaps._MATTER,
    'Oxy': colormaps._OXY,
    'Phase': colormaps._PHASE,
    'Solar': colormaps._SOLAR,
    'Speed': colormaps._SPEED,
    'Tempo': colormaps._TEMPO,
    'Thermal': colormaps._THERMAL,
    'Turbid': colormaps._TURBID,
}
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    sorted(_NAMES_TO_DATA.keys()))


print_maps = utils.print_maps_factory(
    'sequential cmocean', _NAMES_AND_LENGTHS, _PALETTE_TYPE)
get_map = utils.get_map_factory(
    'sequential cmocean', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    cmoceanpalette.CmoceanMap)


globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
