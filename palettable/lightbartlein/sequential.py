from __future__ import absolute_import, print_function
"""
Sequential Light & Bartlein palettes as described at
http://geog.uoregon.edu/datagraphics/color_scales.htm

"""
import itertools as it

from . import colordata
from . import lightbartlein
from .. import utils

_PALETTE_TYPE = 'sequential'
_NAMES_TO_DATA = {
    'Blues7': colordata._BLUE_7,
    'Blues10': colordata._BLUE_10,
}
_MAX_LENS = {
    'Blues7': 7,
    'Blues10': 10,
}
_NAMES_AND_LENGTHS = list(
    it.chain.from_iterable(
        utils.make_names_and_lengths([name], range(2, _MAX_LENS[name] + 1))
        for name in sorted(_NAMES_TO_DATA)
    )
)

print_maps = utils.print_maps_factory('sequential Light & Bartlein',
                                      _NAMES_AND_LENGTHS,
                                      _PALETTE_TYPE)

get_map = utils.get_map_factory('sequential Light & Bartlein',
                                __name__,
                                _NAMES_TO_DATA,
                                _PALETTE_TYPE,
                                lightbartlein.LightBartleinMap,
                                is_evenly_spaced=True)

globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
