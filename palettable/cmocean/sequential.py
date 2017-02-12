"""
Sequential color maps from the cmocean package:
https://github.com/matplotlib/cmocean.

"""
from __future__ import absolute_import

import itertools

from . import cmoceanpalette
from . import colormaps
from .. import utils

_PALETTE_TYPE = 'sequential'
_NAME_MAP = {
    'algae': 'Algae',
    'amp': 'Amp',
    'deep': 'Deep',
    'dense': 'Dense',
    'gray': 'Gray',
    'haline': 'Haline',
    'ice': 'Ice',
    'matter': 'Matter',
    'oxy': 'Oxy',
    'phase': 'Phase',
    'solar': 'Solar',
    'speed': 'Speed',
    'tempo': 'Tempo',
    'thermal': 'Thermal',
    'turbid': 'Turbid',
}
_NAMES_TO_DATA = {
    'Algae': colormaps._ALGAE,
    'Amp': colormaps._AMP,
    'Deep': colormaps._DEEP,
    'Dense': colormaps._DENSE,
    'Gray': colormaps._GRAY,
    'Haline': colormaps._HALINE,
    'Ice': colormaps._ICE,
    'Matter': colormaps._MATTER,
    'Oxy': colormaps._OXY,
    'Phase': colormaps._PHASE,
    'Solar': colormaps._SOLAR,
    'Speed': colormaps._SPEED,
    'Tempo': colormaps._TEMPO,
    'Thermal': colormaps._THERMAL,
    'Turbid': colormaps._TURBID,
}
_PALETTE_LENGTHS = range(3, 21)
_NAMES_AND_LENGTHS = list(itertools.product(
    sorted(_NAMES_TO_DATA.keys()), _PALETTE_LENGTHS))


def print_maps():
    """Print a list of sequential cmocean palettes"""
    namelen = max(
        len(cmoceanpalette.palette_name(name, length))
        for name, length in _NAMES_AND_LENGTHS)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for name, length in _NAMES_AND_LENGTHS:
        print(fmt.format(
            cmoceanpalette.palette_name(name, length), _PALETTE_TYPE, length))


def get_map(name, reverse=False):
    """
    Get a sequential cmocean palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use palettable.cmocean.sequential.print_maps
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
    Returns a dictionary of all sequential cmocean palettes,
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
