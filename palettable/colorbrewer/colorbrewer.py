from __future__ import absolute_import
from __future__ import print_function

import webbrowser

from ..palette import Palette
from .colorbrewer_all_schemes import COLOR_MAPS

__all__ = ('COLOR_MAPS', 'print_maps', 'print_all_maps', 'print_maps_by_type',
           'get_map', 'MAP_TYPES', 'BrewerMap')


MAP_TYPES = ('sequential', 'diverging', 'qualitative')


def print_maps(map_type=None, number=None):
    """
    Print maps by type and/or number of defined colors.

    Parameters
    ----------
    map_type : {'sequential', 'diverging', 'qualitative'}, optional
        Filter output by map type. By default all maps are printed.
    number : int, optional
        Filter output by number of defined colors. By default there is
        no numeric filtering.

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
    for t in MAP_TYPES:
        print_maps_by_type(t)


def print_maps_by_type(map_type, number=None):
    """
    Print all available maps of a given type.

    Parameters
    ----------
    map_type : {'sequential', 'diverging', 'qualitative'}
        Select map type to print.
    number : int, optional
        Filter output by number of defined colors. By default there is
        no numeric filtering.

    """
    if map_type.lower() not in MAP_TYPES:
        s = 'Invalid map type, must be one of {0}'.format(MAP_TYPES)
        raise ValueError(s)

    print(map_type)

    # maps are keyed by capitalized types in COLOR_MAPS
    map_type = map_type.capitalize()
    map_keys = sorted(COLOR_MAPS[map_type].keys())

    format_str = '{0:8}  :  {1}'

    for mk in map_keys:
        num_keys = sorted(COLOR_MAPS[map_type][mk].keys(), key=int)

        if not number or str(number) in num_keys:
            num_str = '{' + ', '.join(num_keys) + '}'
            print(format_str.format(mk, num_str))


class BrewerMap(Palette):
    """
    Representation of a colorbrewer2 color map with matplotlib compatible
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
    colorbrewer2_url : str
    hex_colors : list
    mpl_colors : list
    mpl_colormap : matplotlib LinearSegmentedColormap

    """
    @property
    def colorbrewer2_url(self):
        """
        URL that can be used to view the color map at colorbrewer2.org.

        """
        url = 'http://colorbrewer2.org/index.html?type={0}&scheme={1}&n={2}'
        return url.format(self.type.lower(), self.name, self.number)

    def colorbrewer2(self):
        """
        View this color map at colorbrewer2.org. This will open
        colorbrewer2.org in your default web browser.

        """
        webbrowser.open_new_tab(self.colorbrewer2_url)  # pragma: no cover


def get_map(name, map_type, number, reverse=False):
    """
    Return a `BrewerMap` representation of the specified color map.

    Parameters
    ----------
    name : str
        Name of color map. Use `print_maps` to see available color maps.
    map_type : {'sequential', 'diverging', 'qualitative'}
        Select color map type.
    number : int
        Number of defined colors in color map.
    reverse : bool, optional
        Set to True to get the reversed color map.

    """
    number = str(number)

    # check for valid type
    if map_type.lower() not in MAP_TYPES:
        s = 'Invalid map type, must be one of {0}'.format(MAP_TYPES)
        raise ValueError(s)

    # maps are keyed by capitalized types in COLOR_MAPS
    map_type = map_type.capitalize()

    # make a dict of lower case map name to map name so this can be
    # insensitive to case.
    # this would be a perfect spot for a dict comprehension but going to
    # wait on that to preserve 2.6 compatibility.
    # map_names = {k.lower(): k for k in COLOR_MAPS[map_type].iterkeys()}
    map_names = dict((k.lower(), k) for k in COLOR_MAPS[map_type].keys())

    # check for valid name
    if name.lower() not in map_names:
        s = 'Invalid color map name {0!r} for type {1!r}.\n'
        s = s.format(name, map_type)
        valid_names = [str(k) for k in COLOR_MAPS[map_type].keys()]
        valid_names.sort()
        s += 'Valid names are: {0}'.format(valid_names)
        raise ValueError(s)

    name = map_names[name.lower()]

    # check for valid number
    if number not in COLOR_MAPS[map_type][name]:
        s = 'Invalid number for map type {0!r} and name {1!r}.\n'
        s = s.format(map_type, str(name))
        valid_numbers = [int(k) for k in COLOR_MAPS[map_type][name].keys()]
        valid_numbers.sort()
        s += 'Valid numbers are : {0}'.format(valid_numbers)
        raise ValueError(s)

    colors = COLOR_MAPS[map_type][name][number]['Colors']

    if reverse:
        name += '_r'
        colors = [x for x in reversed(colors)]

    return BrewerMap(name, map_type.lower(), colors)


def _load_maps_by_type(map_type):
    """
    Load all maps of a given type into a dictionary.

    Color maps are loaded as BrewerMap objects. Dictionary is
    keyed by map name and then integer numbers of defined
    colors. There is an additional 'max' key that points to the
    color map with the largest number of defined colors.

    Parameters
    ----------
    map_type : {'sequential', 'diverging', 'qualitative'}

    Returns
    -------
    maps : dict of BrewerMap

    """
    map_type = map_type.capitalize()
    seq_maps = COLOR_MAPS[map_type]

    loaded_maps = {}

    for map_name in seq_maps:
        for num in seq_maps[map_name]:
            inum = int(num)
            name = '{0}_{1}'.format(map_name, num)
            loaded_maps[name] = get_map(map_name, map_type, inum)
            loaded_maps[name + '_r'] = get_map(
                map_name, map_type, inum, reverse=True)

    return loaded_maps
