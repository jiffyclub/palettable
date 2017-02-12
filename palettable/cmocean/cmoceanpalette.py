"""
Palette class and utilities for cmocean palettes.

"""
from __future__ import absolute_import

from ..palette import Palette


class CmoceanMap(Palette):
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
    url = 'http://matplotlib.org/cmocean/'

    def __init__(self, name, palette_type, colors):
        super(CmoceanMap, self).__init__(name, palette_type, colors)


def palette_name(name, length):
    """Create a palette name like Viridis_8"""
    return '{0}_{1}'.format(name, length)


def split_name_length(name):
    """Split name and length from a name like Viridis_8"""
    split = name.split('_')
    return split[0], int(split[1])
