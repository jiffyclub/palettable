from __future__ import print_function

import os.path
import json

from collections import OrderedDict


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
    max_mp_len = max(map(len, map_keys))

    format_str = '{:8}  :  {}'

    for mk in map_keys:
        num_keys = sorted(COLOR_MAPS[map_type][mk].keys(), key=int)
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


def get_map(name, map_type, number):
    """
    Return a `BrewerMap` representation of the specified color map.

    """
    number = str(number)
    map_type = map_type.capitalize()

    colors = COLOR_MAPS[map_type][name][number]['Colors']

    return BrewerMap(name, map_type, int(number), colors)
