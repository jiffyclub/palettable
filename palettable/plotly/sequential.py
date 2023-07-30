"""
Color maps from Plotly package
Learn more at https://github.com/plotly/plotly.py and view the MIT license at
https://github.com/plotly/plotly.py/blob/master/LICENSE.txt

"""

from __future__ import absolute_import

from . import plotly
from . import colordata
from .. import utils

_PALETTE_TYPE = "sequential"
_NAMES_TO_DATA = {
    "Blackbody": colordata.BLACKBODY,
    "Bluered": colordata.BLUERED,
    "Electric": colordata.ELECTRIC,
    "Hot": colordata.HOT,
    "Jet": colordata.JET,
    "Rainbow": colordata.RAINBOW,
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = (
    utils.make_names_and_lengths(["Blackbody"], range(2, 6))
    + utils.make_names_and_lengths(["Bluered"], range(2, 3))
    + utils.make_names_and_lengths(["Electric"], range(2, 7))
    + utils.make_names_and_lengths(["Hot"], range(2, 5))
    + utils.make_names_and_lengths(["Jet"], range(2, 7))
    + utils.make_names_and_lengths(["Rainbow"], range(2, 10))
)

print_maps = utils.print_maps_factory(
    "sequential plotly", _NAMES_AND_LENGTHS, _PALETTE_TYPE
)

get_map = utils.get_map_factory(
    "sequential plotly",
    __name__,
    _NAMES_TO_DATA,
    _PALETTE_TYPE,
    plotly.PlotlyColorMap,
    is_evenly_spaced=False,
)

globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
