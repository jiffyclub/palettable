from __future__ import absolute_import, print_function
"""
Diverging Light & Bartlein palettes as described at
http://geog.uoregon.edu/datagraphics/color_scales.htm

"""
import itertools as it

from . import colordata
from . import lightbartlein
from .. import utils

_PALETTE_TYPE = 'diverging'
_NAMES_TO_DATA = {
    'BlueDarkOrange12': colordata._BLUE_TO_DARK_ORANGE_12,
    'BlueDarkOrange18': colordata._BLUE_TO_DARK_ORANGE_18,
    'BlueDarkRed12': colordata._BLUE_TO_DARK_RED_12,
    'BlueDarkRed18': colordata._BLUE_TO_DARK_RED_18,
    'BlueGreen': colordata._BLUE_TO_GREEN,
    'BlueGrey': colordata._BLUE_TO_GREY,
    'BlueGray': colordata._BLUE_TO_GREY,
    'BlueOrange8': colordata._BLUE_TO_ORANGE_8,
    'BlueOrange10': colordata._BLUE_TO_ORANGE_10,
    'BlueOrange12': colordata._BLUE_TO_ORANGE_12,
    'BlueOrangeRed': colordata._BLUE_ORANGE_RED,
    'BrownBlue10': colordata._BROWN_TO_BLUE_10,
    'BrownBlue12': colordata._BROWN_TO_BLUE_12,
    'GreenMagenta': colordata._GREEN_TO_MAGENTA,
    'RedYellowBlue': colordata._RED_YELLOW_BLUE,
}
_MAX_LENS = {
    'BlueDarkOrange12': 12,
    'BlueDarkOrange18': 18,
    'BlueDarkRed12': 12,
    'BlueDarkRed18': 18,
    'BlueGreen': 14,
    'BlueGrey': 8,
    'BlueGray': 8,
    'BlueOrange8': 8,
    'BlueOrange10': 10,
    'BlueOrange12': 12,
    'BlueOrangeRed': 14,
    'BrownBlue10': 10,
    'BrownBlue12': 12,
    'GreenMagenta': 16,
    'RedYellowBlue': 11,
}
_NAMES_AND_LENGTHS = list(
    it.chain.from_iterable(
        utils.make_names_and_lengths([name], range(2, _MAX_LENS[name] + 1))
        for name in sorted(_NAMES_TO_DATA)
    )
)

print_maps = utils.print_maps_factory('diverging Light & Bartlein',
                                      _NAMES_AND_LENGTHS,
                                      _PALETTE_TYPE)

get_map = utils.get_map_factory('diverging Light & Bartlein',
                                __name__,
                                _NAMES_TO_DATA,
                                _PALETTE_TYPE,
                                lightbartlein.LightBartleinMap,
                                is_evenly_spaced=True)

globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
