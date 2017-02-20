from __future__ import absolute_import, print_function
"""
Mycarta palettes as described at https://mycarta.wordpress.com/color-palettes/

"""

import itertools

from . import colordata
from .. import utils
from ..palette import Palette

_PALETTE_TYPE = 'sequential'
_NAMES_TO_DATA = {
    'Cube1': colordata.CUBE1,
    'CubeYF': colordata.CUBEYF,
    'LinearL': colordata.LINEARL,
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    sorted(_NAMES_TO_DATA.keys()))


class MycartaMap(Palette):
    """
    Representation of a color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str
    palette_type : str
    colors : list
        Colors as list of 0-255 RGB triplets.

    Attributes
    ----------
    name : str
    type : str
    number : int
        Number of colors in color map.
    colors : list
        Colors as list of 0-255 RGB triplets.
    hex_colors : list
    mpl_colors : list
    mpl_colormap : matplotlib LinearSegmentedColormap
    url : str
        Website with related info.

    """
    url = 'https://mycarta.wordpress.com/color-palettes/'

    def __init__(self, name, palette_type, colors):
        super(MycartaMap, self).__init__(name, palette_type, colors)


print_maps = utils.print_maps_factory(
    'mycarta', _NAMES_AND_LENGTHS, _PALETTE_TYPE)
get_map = utils.get_map_factory(
    'mycarta', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    MycartaMap)
