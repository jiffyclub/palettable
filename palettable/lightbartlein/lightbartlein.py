from __future__ import absolute_import, print_function
"""
Light & Bartlein palettes as described at
http://geog.uoregon.edu/datagraphics/color_scales.htm

"""

from ..palette import Palette


class LightBartleinMap(Palette):
    """
    Representation of a Light & Bartlein color map with matplotlib compatible
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
        super(LightBartleinMap, self).__init__(name, palette_type, colors)
