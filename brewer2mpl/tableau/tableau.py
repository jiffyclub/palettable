# coding: utf-8
"""
Color palettes derived from Tableau: http://www.tableausoftware.com/

See also:

http://kb.tableausoftware.com/articles/knowledgebase/creating-custom-color-palettes
http://tableaufriction.blogspot.ro/2012/11/finally-you-can-use-tableau-data-colors.html

"""
from __future__ import absolute_import

from ..colormap import ColorMap

# There is no documentation page that lists the color palettes.
url = 'http://www.tableausoftware.com'
palette_type = 'Qualitative'

palettes = [
    # Long name, short name
    ('Tableau 10', 'T 10'),
    ('Tableau 10 Light', 'T 10 L'),
    ('Tableau 10 Medium', 'T 10 M'),
    ('Tableau 20', 'T 20'),
    ('Gray 5', 'Gra 5'),
    ('Color Blind 10', 'CB 10'),
    ('Traffic Light', 'TL'),
    ('Purple-Gray 6', 'P-G 6'),
    ('Purple-Gray 12', 'P-G 12'),
    ('Blue-Red 6', 'B-R 6'),
    ('Blue-Red 12', 'B-R 12'),
    ('Green-Orange 6', 'G-O 6'),
    ('Green-Orange 12', 'G-O 12')
]

# Dictionary from name or short name to index.
lookup = dict([(name, i) for i, names in enumerate(palettes)
                         for name in names])

colors_rgb = [
    # Tableau 10
    [[ 31, 119, 180],
     [255, 127,  14],
     [ 44, 160,  44],
     [214,  39,  40],
     [148, 103, 189],
     [140,  86,  75],
     [227, 119, 194],
     [127, 127, 127],
     [188, 189,  34],
     [ 23, 190, 207]],
    # Tableau 10 Light
    [[174, 199, 232],
     [255, 187, 120],
     [152, 223, 138],
     [255, 152, 150],
     [197, 176, 213],
     [196, 156, 148],
     [247, 182, 210],
     [199, 199, 199],
     [219, 219, 141],
     [158, 218, 229]],
    # Tableau 10 Medium
    [[114, 158, 206],
     [255, 158,  74],
     [103, 191,  92],
     [237, 102,  93],
     [173, 139, 201],
     [168, 120, 110],
     [237, 151, 202],
     [162, 162, 162],
     [205, 204,  93],
     [109, 204, 218]],
    # Tableau 20
    [[ 31, 119, 180],
     [174, 199, 232],
     [255, 127,  14],
     [255, 187, 120],
     [ 44, 160,  44],
     [152, 223, 138],
     [214,  39,  40],
     [255, 152, 150],
     [148, 103, 189],
     [197, 176, 213],
     [140,  86,  75],
     [196, 156, 148],
     [227, 119, 194],
     [247, 182, 210],
     [127, 127, 127],
     [199, 199, 199],
     [188, 189,  34],
     [219, 219, 141],
     [ 23, 190, 207],
     [158, 218, 229]],
    # Gray 5
    [[ 96,  99, 106],
     [165, 172, 175],
     [ 65,  68,  81],
     [143, 135, 130],
     [207, 207, 207]],
    # Color Blind 10
    [[  0, 107, 164],
     [255, 128,  14],
     [171, 171, 171],
     [ 89,  89,  89],
     [ 95, 158, 209],
     [200,  82,   0],
     [137, 137, 137],
     [162, 200, 236],
     [255, 188, 121],
     [207, 207, 207]],
    # Traffic Light
    [[177,   3,  24],
     [219, 161,  58],
     [ 48, 147,  67],
     [216,  37,  38],
     [255, 193,  86],
     [105, 183, 100],
     [242, 108, 100],
     [255, 221, 113],
     [159, 205, 153]],
    # Purple-Gray 6
    [[123, 102, 210],
     [220,  95, 189],
     [148, 145, 123],
     [153,  86, 136],
     [208, 152, 238],
     [215, 213, 197]],
    # Purple-Gray 12
    [[123, 102, 210],
     [166, 153, 232],
     [220,  95, 189],
     [255, 192, 218],
     [ 95,  90,  65],
     [180, 177, 155],
     [153,  86, 136],
     [216, 152, 186],
     [171, 106, 213],
     [208, 152, 238],
     [139, 124, 110],
     [219, 212, 197]],
    # Blue-Red 6
    [[ 44, 105, 176],
     [240,  39,  32],
     [172,  97,  60],
     [107, 163, 214],
     [234, 107, 115],
     [233, 195, 155]],
    # Blue-Red 12
    [[ 44, 105, 176],
     [181, 200, 226],
     [240,  39,  32],
     [255, 182, 176],
     [172,  97,  60],
     [233, 195, 155],
     [107, 163, 214],
     [181, 223, 253],
     [172, 135,  99],
     [221, 201, 180],
     [189,  10,  54],
     [244, 115, 122]],
    # Green-Orange 6
    [[ 50, 162,  81],
     [255, 127,  15],
     [ 60, 183, 204],
     [255, 217,  74],
     [ 57, 115, 124],
     [184,  90,  13]],
    # Green-Orange 12
    [[ 50, 162,  81],
     [172, 217, 141],
     [255, 127,  15],
     [255, 185, 119],
     [ 60, 183, 204],
     [152, 217, 228],
     [184,  90,  13],
     [255, 217,  74],
     [ 57, 115, 124],
     [134, 180, 169],
     [130, 133,  59],
     [204, 201,  77]]
]

class TableauMap(ColorMap):
    """
    Representation of a color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str
    map_type : str
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

    """
    url = url

    def __init__(self, name, short_name, colors):
        super(TableauMap, self).__init__(name, palette_type, colors)
        self.short_name = short_name


def print_maps():
    """
    Print a list of Tableau palettes.

    """
    namelen = max(len(name) for name, _ in palettes)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for i, names in enumerate(palettes):
        print(fmt.format(names[0], palette_type, len(colors_rgb[i])))


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
    palette : TableauMap

    """
    try:
        index = lookup[name]
    except KeyError:
        msg = "{0!r} is an unknown Tableau palette."
        raise KeyError(msg.format(name))

    name, short_name = palettes[index]
    colors = colors_rgb[index]
    if reverse:
        name = name + '_r'
        short_name = short_name + '_r'
        colors = list(reversed(colors))

    return TableauMap(name, short_name, colors)

def get_all_maps():
    """
    Returns a dictionary of all Tableau palettes.

    """
    return dict([(name, get_map(name)) for name, short_name in palettes])
