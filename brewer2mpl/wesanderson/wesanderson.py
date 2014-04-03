from __future__ import print_function
"""
Color palettes derived from http://wesandersonpalettes.tumblr.com/.

"""

import webbrowser

from ..brewer2mpl import _ColorMap


_tumblr_template = 'http://wesandersonpalettes.tumblr.com/post/{0}'

# Tumblr palettes in chronological order
_palettes = {
    'Chevalier': {
        'colors': [
            (53, 82, 67), (254, 202, 73), (201, 213, 213), (187, 162, 137)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format('79263620764/hotel-chevalier')
    },
    'Moonrise1': {
        'colors': [
            (114, 202, 221), (240, 165, 176), (140, 133, 54), (195, 180, 119),
            (250, 208, 99)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '79263667140/sam-i-love-you-but-you-dont-know-what-youre')
    },
    'Mendl': {
        'colors': [
            (222, 141, 185), (184, 192, 246), (207, 147, 135), (92, 128, 204)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format('79348206200/mendls-heaven')
    },
    'Margot1': {
        'colors': [
            (137, 119, 18), (243, 194, 164), (246, 159, 151), (254, 214, 140),
            (98, 144, 117)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format('79348364517/margot-takes-a-bath')
    },
    'Cavalcanti': {
        'colors': [
            (209, 170, 0), (8, 50, 19), (146, 148, 96), (111, 152, 121),
            (132, 33, 17)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '79348553036/castello-cavalcanti-how-can-i-help')
    },
    'Moonrise2': {
        'colors': [
            (102, 124, 116), (181, 106, 39), (194, 186, 124), (31, 25, 23)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '79641731527/sam-why-do-you-always-use-binoculars-suzy-it')
    },
    'Margot2': {
        'colors': [
            (118, 139, 147), (188, 36, 15), (249, 236, 197), (212, 115, 41)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format('79641785036/margot-takes-a-break')
    },
    'Moonrise3': {
        'colors': [
            (242, 218, 82), (197, 157, 0), (203, 203, 201), (27, 30, 20)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '79783357790/suzy-ive-always-wanted-to-be-an-orphan-most-of')
    },
    'GrandBudapest1': {
        'colors': [
            (238, 174, 101), (251, 79, 85), (72, 19, 19), (204, 95, 39)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format('79784389334/the-grand-budapest-hotel')
    },
    'Moonrise4': {
        'colors': [
            (123, 135, 97), (193, 166, 46), (79, 143, 107), (59, 69, 60),
            (159, 50, 8)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format('79956897654/coming-soon')
    },
    'Zissou': {
        'colors': [
            (0, 153, 230), (18, 37, 90), (242, 56, 20), (223, 183, 139),
            (182, 195, 197)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '79956949771/steve-zissou-dont-point-that-gun-at-him-hes-an')
    },
    'Royal1': {
        'colors': [
            (121, 164, 58), (242, 214, 175), (94, 72, 41), (24, 20, 1)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '79957796915/royal-o-reilly-tenenbaum-1932-2001')
    },
    'Darjeeling1': {
        'colors': [
            (158, 151, 151), (194, 142, 0), (131, 102, 89), (156, 90, 51)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '80149649946/jack-i-wonder-if-the-three-of-us-wouldve-been')
    },
    'FantasticFox1': {
        'colors': [
            (249, 219, 32), (147, 75, 78), (66, 23, 13), (194, 121, 34),
            (226, 200, 167)
        ],
        'type': 'Qualitative',
        'url': _tumblr_template.format(
            '80149872170/mrs-fox-you-know-you-really-are-fantastic-mr')
    }
}

_map_names = {}
for k in _palettes:
    _map_names[k.lower()] = k


class WesAndersonMap(_ColorMap):
    """
    Representation of a color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str
    map_type : str
    colors : list
        Colors as list of 0-255 RGB triplets.
    url : str
        URL on the web where this color map can be viewed.

    Attributes
    ----------
    name : str
    map_type : str
    number : int
        Number of colors in color map.
    colors : list
        Colors as list of 0-255 RGB triplets.
    hex_colors : list
    mpl_colors : list
    mpl_colormap : matplotlib LinearSegmentedColormap
    wap_url : str
        URL on the web where this color map can be viewed.

    """
    def __init__(self, name, map_type, colors, url):
        super(WesAndersonMap, self).__init__(name, map_type, colors)
        self.wap_url = url

    def wap(self):
        """
        View this color palette on the web.
        Will open a new tab in your web browser.

        """
        webbrowser.open_new_tab(self.wap_url)  # pragma: no cover


def print_maps():
    """
    Print a list of Wes Anderson palettes.

    """
    namelen = max(len(k) for k in _palettes)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}{2:}'

    for k in sorted(_palettes.keys()):
        print(fmt.format(k, _palettes[k]['type'], len(_palettes[k]['colors'])))


def get_map(name, reverse=False):
    """
    Get a Wes Anderson palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use brewer2mpl.wap.print_maps to see available names.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : WesAndersonMap

    """
    name = _map_names[name.lower()]
    palette = _palettes[name]

    if reverse:
        name += '_r'
        palette['colors'] = list(reversed(palette['colors']))

    return WesAndersonMap(
        name, palette['type'], palette['colors'], palette['url'])
