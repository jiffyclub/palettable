from __future__ import absolute_import, print_function
"""

Light & Bartlein palettes as described at http://geog.uoregon.edu/datagraphics/color_scales.htm

"""

from . import colordata
from ..palette import Palette

_NAMES_TO_DATA = {
    'GreenMagenta': [colordata._GRMG, 'diverging', 16],
    'BlueDarkRed12': [colordata._BUDR_12, 'diverging', 12],
    'BlueDarkRed18': [colordata._BUDR_18, 'diverging', 18],
    'BlueDarkOrange12': [colordata._BUDOR_12, 'diverging', 12],
    'BlueDarkOrange18': [colordata._BUDOR_18, 'diverging', 18],
    'BlueGreen': [colordata._BUGN, 'diverging', 14],
    'BrownBlue10': [colordata._BRBU_10, 'diverging', 10],
    'BrownBlue12': [colordata._BRBU_12, 'diverging', 12],
    'BlueGrey8': [colordata._BUGR, 'diverging', 8],
    'BlueGray8': [colordata._BUGR, 'diverging', 8],
    'BlueOrange8': [colordata._BUOR_8, 'diverging', 8],
    'BlueOrange10': [colordata._BUOR_10, 'diverging', 10],
    'BlueOrange12': [colordata._BUOR_12, 'diverging', 12],
    'BlueOrangeRed': [colordata._BUORRD, 'diverging', 14],
    'RedYellowBlue': [colordata._RDYLBU, 'diverging', 11],
    'Blues7': [colordata._BU7, 'sequential', 7],
    'Blues10': [colordata._BU10, 'sequential', 10],
}
palette_names = list(_NAMES_TO_DATA.keys())


class LBMap(Palette):
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
    url = 'http://geog.uoregon.edu/datagraphics/color_scales.htm'

    def __init__(self, name, palette_type, colors):
        super(LBMap, self).__init__(name, palette_type, colors)


def print_maps():
    """
    Print a list of Light-Bartlein palettes.

    """
    namelen = max(len(name) for name in palette_names)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for i, name in enumerate(palette_names):
        print(fmt.format(name,
                         _NAMES_TO_DATA[name][1],
                         _NAMES_TO_DATA[name][2]))


def get_map(name, reverse=False):
    """
    Get a Tableau palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use `print_maps` to see available names. If `None`, then
        return a list of all colormaps.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : LBMap

    """

    if name not in _NAMES_TO_DATA:
        raise ValueError(name + ' not in Light-Bartlein colormaps.')

    colors = _NAMES_TO_DATA[name][0]
    paltype = _NAMES_TO_DATA[name][1]

    if reverse:
        name = name + '_r'
        colors = list(reversed(colors))

    return LBMap(name, paltype, colors)


def _get_all_maps():
    """
    Returns a dictionary of all Light-Bartlein palettes,
    including reversed ones.
    """
    d = dict((name, get_map(name)) for name in palette_names)
    d.update(dict(
        (name + '_r', get_map(name, reverse=True)) for name in palette_names))
    return d
