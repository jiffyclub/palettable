"""
Color maps from Plotly package
Learn more at https://github.com/plotly/plotly.py and view the MIT license at
https://github.com/plotly/plotly.py/blob/master/LICENSE.txt

"""

from __future__ import absolute_import

from . import plotly
from . import colordata
from .. import utils

_PALETTE_TYPE = "qualitative"
_NAMES_TO_DATA = {
    "Plotly": colordata.PLOTLY,
    "D3": colordata.D3,
    "G10": colordata.G10,
    "T10": colordata.T10,
    "Alphabet": colordata.ALPHABET,
    "Dark24": colordata.DARK24,
    "Light24": colordata.LIGHT24,
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = (
    utils.make_names_and_lengths(["Plotly", "D3", "G10", "T10"], range(2, 11))
    + utils.make_names_and_lengths(["Alphabet"], range(2, 27))
    + utils.make_names_and_lengths(["Dark24", "Light24"], range(2, 25))
)

print_maps = utils.print_maps_factory(
    "qualitative plotly", _NAMES_AND_LENGTHS, _PALETTE_TYPE
)

get_map = utils.get_map_factory(
    "qualitative plotly",
    __name__,
    _NAMES_TO_DATA,
    _PALETTE_TYPE,
    plotly.PlotlyColorMap,
    is_evenly_spaced=False,
)

globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
