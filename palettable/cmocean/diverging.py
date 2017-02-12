"""
Diverging color maps from the cmocean package:
https://github.com/matplotlib/cmocean.

"""
from __future__ import absolute_import

import itertools

from . import cmoceanpalette
from . import colormaps
from .. import utils

_PALETTE_TYPE = 'diverging'
_NAME_MAP = {
    'balance': 'Balance',
    'curl': 'Curl',
    'delta': 'Delta',
}
_NAMES_TO_DATA = {
    'Balance': colormaps._BALANCE,
    'Curl': colormaps._CURL,
    'Delta': colormaps._DELTA,
}
_PALETTE_LENGTHS = range(3, 21)
_NAMES_AND_LENGTHS = list(itertools.product(
    sorted(_NAMES_TO_DATA.keys()), _PALETTE_LENGTHS))


def print_maps():
    """Print a list of diverging cmocean palettes"""
    namelen = max(
        len(cmoceanpalette.palette_name(name, length))
        for name, length in _NAMES_AND_LENGTHS)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for name, length in _NAMES_AND_LENGTHS:
        print(fmt.format(
            cmoceanpalette.palette_name(name, length), _PALETTE_TYPE, length))


def get_map(name, reverse=False):
    """
    Get a diverging cmocean palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use palettable.cmocean.diverging.print_maps
        to see available names.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : CmoceanMap

    """
    # name will be something like Viridis_8
    name, length = cmoceanpalette.split_name_length(name)

    if name.lower() not in _NAME_MAP:
        raise KeyError('Unknown palette name: {0}'.format(name))
    name = _NAME_MAP[name.lower()]

    colors = utils.evenly_spaced_values(length, _NAMES_TO_DATA[name])

    # add number back to name
    name = '{0}_{1}'.format(name, length)

    if reverse:
        name += '_r'
        colors = list(reversed(colors))

    return cmoceanpalette.CmoceanMap(name, _PALETTE_TYPE, colors)


def _get_all_maps():
    """
    Returns a dictionary of all diverging cmocean palettes,
    including reversed ones.

    """
    fmt = '{0}_{1}'.format
    maps = {}
    for name, length in _NAMES_AND_LENGTHS:
        map_name = fmt(name, length)
        maps[map_name] = get_map(map_name)
        maps[map_name + '_r'] = get_map(map_name, reverse=True)
    return maps


globals().update(_get_all_maps())
