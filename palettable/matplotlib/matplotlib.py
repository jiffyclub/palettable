from __future__ import absolute_import, print_function
"""
New matplotlib color palettes as described at https://bids.github.io/colormap

"""

import itertools

from . import colormaps
from .. import utils
from ..palette import Palette

_PALETTE_TYPE = 'sequential'
_NAME_MAP = {
    'magma': 'Magma',
    'inferno': 'Inferno',
    'plasma': 'Plasma',
    'viridis': 'Viridis'
}
_NAMES_TO_DATA = {
    'Magma': colormaps._MAGMA_DATA,
    'Inferno': colormaps._INFERNO_DATA,
    'Plasma': colormaps._PLASMA_DATA,
    'Viridis': colormaps._VIRIDIS_DATA
}
_PALETTE_LENGTHS = range(3, 21)
_NAMES_AND_LENGTHS = list(itertools.product(
    sorted(_NAMES_TO_DATA.keys()), _PALETTE_LENGTHS))


class MatplotlibMap(Palette):
    """
    Representation of a color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str
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

    def __init__(self, name, colors):
        super(MatplotlibMap, self).__init__(name, _PALETTE_TYPE, colors)


def palette_name(name, length):
    """Create a palette name like Viridis_8"""
    return '{0}_{1}'.format(name, length)


def split_name_length(name):
    """Split name and length from a name like Viridis_8"""
    split = name.split('_')
    return split[0], int(split[1])


def print_maps():
    """Print a list of matplotlib palettes"""
    namelen = max(
        len(palette_name(name, length)) for name, length in _NAMES_AND_LENGTHS)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for name, length in _NAMES_AND_LENGTHS:
        print(fmt.format(palette_name(name, length), _PALETTE_TYPE, length))


def get_map(name, reverse=False):
    """
    Get a matplotlib palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use palettable.matplotlib.print_maps
        to see available names.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : MatplotlibMap

    """
    # name will be something like Viridis_8
    name, length = split_name_length(name)

    if name.lower() not in _NAME_MAP:
        raise KeyError('Unknown palette name: {0}'.format(name))
    name = _NAME_MAP[name.lower()]

    colors = utils.evenly_spaced_values(length, _NAMES_TO_DATA[name])

    # add number back to name
    name = '{0}_{1}'.format(name, length)

    if reverse:
        name += '_r'
        colors = list(reversed(colors))

    return MatplotlibMap(name, colors)


def _get_all_maps():
    """
    Returns a dictionary of all matplotlib palettes,
    including reversed ones.

    """
    fmt = '{0}_{1}'.format
    maps = {}
    for name, length in _NAMES_AND_LENGTHS:
        map_name = fmt(name, length)
        maps[map_name] = get_map(map_name)
        maps[map_name + '_r'] = get_map(map_name, reverse=True)
    return maps
