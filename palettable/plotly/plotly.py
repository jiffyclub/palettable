"""
Color maps from Plotly package
Learn more at https://github.com/plotly/plotly.py and view the MIT license at
https://github.com/plotly/plotly.py/blob/master/LICENSE.txt

"""
from ..palette import Palette


class PlotlyColorMap(Palette):
    """
    Representation of a Scientific color map with matplotlib compatible
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

    url = "https://plotly.com/python/"

    def __init__(self, name, palette_type, colors):
        super(PlotlyColorMap, self).__init__(name, palette_type, colors)
