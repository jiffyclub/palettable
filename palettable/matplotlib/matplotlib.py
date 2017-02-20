from __future__ import absolute_import, print_function
"""
New matplotlib color palettes as described at https://bids.github.io/colormap

"""

import itertools

from . import colormaps
from .. import utils
from ..palette import Palette

_PALETTE_TYPE = 'sequential'
_NAMES_TO_DATA = {
    'Magma': colormaps._MAGMA_DATA,
    'Inferno': colormaps._INFERNO_DATA,
    'Plasma': colormaps._PLASMA_DATA,
    'Viridis': colormaps._VIRIDIS_DATA
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    sorted(_NAMES_TO_DATA.keys()))


class MatplotlibMap(Palette):
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
    url = 'https://bids.github.io/colormap'

    def __init__(self, name, palette_type, colors):
        super(MatplotlibMap, self).__init__(name, palette_type, colors)


print_maps = utils.print_maps_factory(
    'matplotlib', _NAMES_AND_LENGTHS, _PALETTE_TYPE)
get_map = utils.get_map_factory(
    'matplotlib', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    MatplotlibMap)
