"""
Color maps from Plotly package
Learn more at https://github.com/plotly/plotly.py and view the MIT license at
https://github.com/plotly/plotly.py/blob/master/LICENSE.txt

"""

from __future__ import absolute_import

from . import plotly
from . import colordata
from .. import utils

_PALETTE_TYPE = "diverging"
_NAMES_TO_DATA = {
    "Picnic": colordata.PICNIC,
    "Portland": colordata.PORTLAND,
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    ["Picnic"], range(2, 12)
) + utils.make_names_and_lengths(["Portland"], range(2, 6))


print_maps = utils.print_maps_factory(
    "diverging plotly", _NAMES_AND_LENGTHS, _PALETTE_TYPE
)

get_map = utils.get_map_factory(
    "diverging plotly",
    __name__,
    _NAMES_TO_DATA,
    _PALETTE_TYPE,
    plotly.PlotlyColorMap,
    is_evenly_spaced=False,
)

globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
