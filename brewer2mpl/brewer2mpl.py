from __future__ import print_function

import os.path
import json

try:
    from matplotlib.colors import LinearSegmentedColormap
except ImportError:
    HAVE_MPL = False
else:
    HAVE_MPL = True


__all__ = ('COLOR_MAPS', 'print_maps', 'print_all_maps', 'print_maps_by_type',
           'get_map')

_DATADIR = os.path.join(os.path.dirname(__file__), 'data')
_DATAFILE = os.path.join(_DATADIR, 'colorbrewer_all_schemes.json')

with open(_DATAFILE, 'r') as f:
    COLOR_MAPS = json.load(f)


def print_maps(map_type=None, number=None):
    """
    Print maps by type and/or number of defined colors.

    """
    if not map_type and not number:
        print_all_maps()

    elif map_type:
        print_maps_by_type(map_type, number)

    else:
        s = ('Invalid parameter combination. '
             'number without map_type is not supported.')
        raise ValueError(s)


def print_all_maps():
    """
    Print the name and number of defined colors of all available color maps.

    """
    for t in ('Sequential', 'Diverging', 'Qualitative'):
        print_maps_by_type(t)


def print_maps_by_type(map_type, number=None):
    """
    Print all available maps of a given type.

    """
    map_type = map_type.capitalize()
    print(map_type)

    map_keys = sorted(COLOR_MAPS[map_type].keys())

    format_str = '{0:8}  :  {1}'

    for mk in map_keys:
        num_keys = sorted(COLOR_MAPS[map_type][mk].keys(), key=int)

        if not number or str(number) in num_keys:
            num_str = '{' + ', '.join(num_keys) + '}'
            print(format_str.format(mk, num_str))


class BrewerMap(object):
    """
    Representation of a colorbrewer2 color map with matplotlib compatible
    views of the map.

    """
    def __init__(self, name, map_type, number, colors):
        self.name = name
        self.type = map_type
        self.number = int(number)
        self.colors = colors

    @property
    def colorbrewer2_url(self):
        """
        URL that can be used to view the color map at colorbrewer2.org.

        """
        url = 'http://colorbrewer2.org/index.php?type={0}&scheme={1}&n={2}'
        return url.format(self.type.lower(), self.name, self.number)

    @property
    def mpl_colors(self):
        """
        Colors expressed on the range 0-1 as used by matplotlib.

        """
        mc = []

        for color in self.colors:
            mc.append(tuple([x/255. for x in color]))

        return mc

    @property
    def mpl_colormap(self):
        """
        A basic matplotlib color map. If you want to specify keyword arguments
        use the `get_mpl_colormap` method.

        """
        return self.get_mpl_colormap()

    def get_mpl_colormap(self, **kwargs):
        """
        A color map that can be used in matplotlib plots. Requires matplotlib
        to be importable. Keyword arguments are passed to
        `matplotlib.colors.LinearSegmentedColormap.from_list`.

        """
        if not HAVE_MPL:
            raise RuntimeError('matplotlib not available.')

        cmap = LinearSegmentedColormap.from_list(self.name,
                                                 self.mpl_colors, **kwargs)

        return cmap


def get_map(name, map_type, number):
    """
    Return a `BrewerMap` representation of the specified color map.

    """
    number = str(number)
    map_type = map_type.capitalize()

    colors = COLOR_MAPS[map_type][name][number]['Colors']

    return BrewerMap(name, map_type, int(number), colors)
