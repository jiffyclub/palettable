from __future__ import absolute_import, division

import itertools
import math
import sys
import textwrap


def round_as_py3(value):
    """
    Implement round behaviour consistent with Python 3 for use in Python 2.
    (Such that halves are rounded toward the even side.
    Only for positive numbers.)
    Adapted from https://github.com/python/cpython/blob/6b678aea1ca5c3c3728cd5a7a6eb112b2dad8553/Python/pytime.c#L71

    """
    if math.fmod(value, 1) == 0.5:
        return 2 * round(value / 2)
    else:
        return round(value)

if sys.version_info[0] >= 3:
    round_ = round
else:
    round_ = round_as_py3


def n_to_indices(num, length):
    """
    Calculate `num` evenly spaced indices for a sequence of length `length`.

    Should be used with num >= 2, result will always include first and last.

    Parameters
    ----------
    num : int
    length : int

    Returns
    -------
    list of int

    """
    if num < 2:
        raise ValueError('num must be 2 or larger, got {0}'.format(num))
    elif num > length:
        raise ValueError('num cannot be greater than length')

    # subtract 1 from length to make it equivalent to the last index,
    # subtract 1 from num to make the calculation include the last index
    step = (length - 1) / (num - 1)

    return (int(round_(step * i)) for i in range(num))


def evenly_spaced_values(num, data):
    """
    Returns `num` evenly spaced values from sequence `data`.

    Parameters
    ----------
    num : int
    data : sequence

    Returns
    -------
    values : list

    """
    return [data[i] for i in n_to_indices(num, len(data))]


def make_name_map(names):
    """
    Create a dictionary mapping lowercase names to capitalized names.

    Parameters
    ----------
    names : sequence

    Returns
    -------
    dict

    """
    return dict((name.lower(), name) for name in names)


def make_names_and_lengths(names, lengths=None):
    """
    Create a list pairing palette names with lengths. (Mostly used to define
    the set of palettes that are automatically built.)

    Parameters
    ----------
    names : sequence of str
    lengths : sequence of int, optional

    Returns
    -------
    list of tuple
        Pairs of names and lengths.

    """
    lengths = lengths or range(3, 21)
    return list(itertools.product(names, lengths))


def palette_name(name, length):
    """Create a palette name like CubeYF_8"""
    return '{0}_{1}'.format(name, length)


def split_name_length(name):
    """Split name and length from a name like CubeYF_8"""
    split = name.split('_')
    return split[0], int(split[1])


def print_maps_factory(desc, names_and_lengths, palette_type):
    """
    Create a function that will print the names and lengths of palettes.

    Parameters
    ----------
    desc : str
        Short description of palettes, for example "sequential cmocean".
        Used to populate the print_maps docstring.
    names_and_lengths : sequence of tuple
        Pairs of names and lengths.
    palette_type : str
        Palette type to include in printed messages.

    Returns
    -------
    function
        Takes no arguments.

    """
    def print_maps():
        namelen = max(
            len(palette_name(name, length))
            for name, length in names_and_lengths)
        fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

        for name, length in names_and_lengths:
            print(fmt.format(
                palette_name(name, length), palette_type, length))
    print_maps.__doc__ = 'Print a list of {0} palettes'.format(desc)
    return print_maps


def get_map_factory(desc, mod_path, names_to_data, palette_type, palette_class,
                    is_evenly_spaced=True):
    """
    Create a function that builds a Palette instance from available data
    and the given Palette sub-class.

    Parameters
    ----------
    desc : str
        Short description of palettes, for example "sequential cmocean".
        Used to populate the get_map docstring.
    mod_path : str
        Path to module where get_map will be used. Use to point users to
        the print_maps function. E.g. 'palettable.cmocean.sequential'.
    names_to_data : dict
        Dictionary mapping string palette names to color data.
        (Lists of 0-255 integer RGB tuples.)
    palette_type : str
        Palette type to pass into Palette subclass, e.g. 'diverging'.
    palette_class : Palette subclass
        Subclass of Palette to use when creating new Palettes.
        Must have __init__ signature (name, palette_type, colors).
    is_evenly_spaced : bool
        Sets sampling of palette. If True, then choose values evenly spaced
        in palette array, otherwise choose colors from the beginning of the
        array.

    Returns
    -------
    function
        The function will have the definition:

            def get_map(name, reverse=False):

    """
    name_map = make_name_map(names_to_data.keys())

    def get_map(name, reverse=False):
        # name will be something like Viridis_8
        name, length = split_name_length(name)
        name_lower = name.lower()

        if name_lower not in name_map:
            raise KeyError('Unknown palette name: {0}'.format(name))

        name = name_map[name_lower]

        if len(names_to_data[name]) < length:
            raise ValueError('Number of requested colors larger than '
                             'the number available in {0}'.format(name))
        if is_evenly_spaced:
            colors = evenly_spaced_values(length, names_to_data[name])
        else:
            colors = names_to_data[name][:length]

        # add number back to name
        name = palette_name(name, length)

        if reverse:
            name += '_r'
            colors = list(reversed(colors))

        return palette_class(name, palette_type, colors)

    get_map.__doc__ = textwrap.dedent("""\
        Get a {0} palette by name.

        Parameters
        ----------
        name : str
            Name of map. Use {1}.print_maps
            to see available names.
        reverse : bool, optional
            If True reverse colors from their default order.

        Returns
        -------
        {2}

        """).format(desc, mod_path, palette_class.__class__.__name__)

    return get_map


def load_all_palettes(names_and_lengths, get_map_func):
    """
    Load all palettes (including reversed ones) into a dictionary,
    given a dictionary of names and lengths, plus a get_map function.

    Parameters
    ----------
    names_and_lengths : dict
        names_and_lengths : sequence of tuple
        Pairs of names and lengths.
    get_map_func : function
        Function with signature get_map(name, reverse=False) that returns
        a Palette subclass instance.

    Returns
    -------
    dict
        Maps Name_Length strings to instances of a Palette subclass.

    """
    maps = {}
    for name, length in names_and_lengths:
        map_name = palette_name(name, length)
        maps[map_name] = get_map_func(map_name)
        maps[map_name + '_r'] = get_map_func(map_name, reverse=True)
    return maps
