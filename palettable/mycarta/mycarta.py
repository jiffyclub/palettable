from __future__ import absolute_import, print_function
"""
Mycarta palettes as described at https://mycarta.wordpress.com/color-palettes/

"""

import itertools

from . import colordata
from .. import utils
from ..palette import Palette

_PALETTE_TYPE = 'sequential'
_NAME_MAP = {
    'cube1': 'Cube1',
    'cubeyf': 'CubeYF',
    'linearl': 'LinearL',
}
_NAMES_TO_DATA = {
    'Cube1': colordata.CUBE1,
    'CubeYF': colordata.CUBEYF,
    'LinearL': colordata.LINEARL,
}
_PALETTE_LENGTHS = range(3, 21)
_NAMES_AND_LENGTHS = list(itertools.product(
    sorted(_NAMES_TO_DATA.keys()), _PALETTE_LENGTHS))


class MycartaMap(Palette):
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
    url = 'https://mycarta.wordpress.com/color-palettes/'

    def __init__(self, name, colors):
        super(MycartaMap, self).__init__(name, _PALETTE_TYPE, colors)


def palette_name(name, length):
    """Create a palette name like CubeYF_8"""
    return '{0}_{1}'.format(name, length)


def split_name_length(name):
    """Split name and length from a name like CubeYF_8"""
    split = name.split('_')
    return split[0], int(split[1])


def print_maps():
    """Print a list of mycarta palettes"""
    namelen = max(
        len(palette_name(name, length)) for name, length in _NAMES_AND_LENGTHS)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for name, length in _NAMES_AND_LENGTHS:
        print(fmt.format(palette_name(name, length), _PALETTE_TYPE, length))


def get_map(name, reverse=False):
    """
    Get a mycarta palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use palettable.mycarta.print_maps
        to see available names.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : MycartaMap

    """
    # name will be something like CubeYF_8
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

    return MycartaMap(name, colors)


def _get_all_maps():
    """
    Returns a dictionary of all mycarta palettes,
    including reversed ones.

    """
    fmt = '{0}_{1}'.format
    maps = {}
    for name, length in _NAMES_AND_LENGTHS:
        map_name = fmt(name, length)
        maps[map_name] = get_map(map_name)
        maps[map_name + '_r'] = get_map(map_name, reverse=True)
    return maps
