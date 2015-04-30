# coding: utf-8
"""
Cubehelix color maps and palettes.

The Cubehelix algorithm makes color scales with monotonic changes in perceived
brightness. This means that a cubehelix color map gracefully degrades into
a monotonic grayscale color map when rendered without color.

Cubehelix maps are generated algorithmically, giving the user flexibility
in desiging a color map that is also safe for grayscale printers. This
module provides several cubehelix realizations, while also exposing the
algorithm directly through the :class:`Cubehelix` class.

Cubehelix was developed by `D.A Green, 2011, BASI, 39, 289
<http://adsabs.harvard.edu/abs/2011arXiv1108.5083G>`_. The original Python
port was done by James R. A. Davenport (see License).

Original License
----------------

Copyright (c) 2014, James R. A. Davenport and contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
from __future__ import absolute_import, print_function

try:
    import numpy as np
except ImportError:  # pragma: no cover
    HAVE_NPY = False
else:
    HAVE_NPY = True

from ..palette import Palette


url = 'http://adsabs.harvard.edu/abs/2011arXiv1108.5083G'
palette_type = 'sequential'


palette_names = [
    'classic_16',
    'perceptual_rainbow_16',
    'purple_16',
    'jim_special_16',
    'red_16',
    'cubehelix1_16',
    'cubehelix2_16',
    'cubehelix3_16'
]


palette_rgb = dict((
    ('classic_16',
     # dict(start=0.5, rotation=-1.5, gamma=1.0, sat=1.2,
     #      min_light=0., max_light=1., n=16)
     [[0, 0, 0],
      [22, 10, 34],
      [24, 32, 68],
      [16, 62, 83],
      [14, 94, 74],
      [35, 116, 51],
      [80, 125, 35],
      [138, 122, 45],
      [190, 117, 85],
      [218, 121, 145],
      [219, 138, 203],
      [204, 167, 240],
      [191, 201, 251],
      [195, 229, 244],
      [220, 246, 239],
      [255, 255, 255]]),
    ('perceptual_rainbow_16',
     # Similar to Matteo Niccoli's Perceptual Rainbow:
     # http://mycarta.wordpress.com/2013/02/21/perceptual-rainbow-palette-the-method/
     # https://github.com/jradavenport/cubehelix
     # dict(start_hue=240., end_hue=-300., min_sat=1., max_sat=2.5,
     #      min_light=0.3, max_light=0.8, gamma=.9, n=16)
     [[135, 59, 97],
      [143, 64, 127],
      [143, 72, 157],
      [135, 85, 185],
      [121, 102, 207],
      [103, 123, 220],
      [84, 146, 223],
      [69, 170, 215],
      [59, 192, 197],
      [60, 210, 172],
      [71, 223, 145],
      [93, 229, 120],
      [124, 231, 103],
      [161, 227, 95],
      [198, 220, 100],
      [233, 213, 117]]),
    ('purple_16',
     # dict(start=0., rotation=0.0, n=16)
     [[0, 0, 0],
      [15, 14, 35],
      [31, 28, 68],
      [47, 43, 99],
      [63, 59, 127],
      [79, 75, 152],
      [96, 91, 174],
      [113, 107, 194],
      [130, 124, 211],
      [147, 142, 225],
      [164, 160, 237],
      [182, 178, 246],
      [200, 196, 252],
      [218, 215, 255],
      [236, 235, 255],
      [255, 255, 255]]),
    ('jim_special_16',
     # http://www.ifweassume.com/2014/04/cubehelix-colormap-for-python.html
     # dict(start=0.3, rotation=-0.5, n=16)
     [[0, 0, 0],
      [22, 10, 34],
      [37, 25, 68],
      [47, 43, 99],
      [52, 65, 125],
      [55, 88, 146],
      [59, 112, 160],
      [64, 137, 169],
      [74, 160, 173],
      [89, 181, 175],
      [109, 199, 177],
      [134, 214, 180],
      [163, 227, 189],
      [195, 237, 203],
      [226, 246, 225],
      [255, 255, 255]]),
    ('red_16',
     # http://www.ifweassume.com/2014/04/cubehelix-colormap-for-python.html
     # dict(start=0., rotation=0.5, n=16)
     [[0, 0, 0],
      [19, 12, 35],
      [44, 22, 65],
      [73, 32, 90],
      [104, 41, 107],
      [134, 53, 118],
      [162, 67, 124],
      [185, 83, 126],
      [204, 102, 128],
      [216, 124, 130],
      [225, 148, 136],
      [229, 172, 147],
      [232, 196, 164],
      [236, 219, 189],
      [242, 238, 219],
      [255, 255, 255]]),
    ('cubehelix1_16',
     # http://nbviewer.ipython.org/gist/anonymous/a4fa0adb08f9e9ea4f94
     # dict(gamma=1.0, start=1.5, rotation=-1.0, sat=1.5, n=16)
     [[0, 0, 0],
      [27, 15, 0],
      [65, 23, 4],
      [104, 27, 32],
      [133, 33, 75],
      [147, 45, 126],
      [144, 66, 175],
      [129, 96, 210],
      [111, 131, 227],
      [99, 166, 226],
      [101, 197, 211],
      [120, 219, 194],
      [153, 233, 185],
      [193, 240, 191],
      [230, 245, 216],
      [255, 255, 255]]),
    ('cubehelix2_16',
     # http://nbviewer.ipython.org/gist/anonymous/a4fa0adb08f9e9ea4f94
     # dict(gamma=1.0, start=2.0, rotation=1.0, sat=1.5, n=16)
     [[0, 0, 0],
      [0, 28, 14],
      [0, 51, 47],
      [7, 65, 91],
      [35, 71, 135],
      [78, 72, 168],
      [129, 72, 184],
      [177, 77, 181],
      [214, 90, 165],
      [235, 113, 143],
      [238, 142, 128],
      [230, 175, 127],
      [219, 206, 144],
      [216, 231, 178],
      [226, 247, 219],
      [255, 255, 255]]),
    ('cubehelix3_16',
     # http://nbviewer.ipython.org/gist/anonymous/a4fa0adb08f9e9ea4f94
     # dict(gamma=1.0, start=2.0, rotation=1.0, sat=3, n=16)
     [[0, 0, 0],
      [0, 39, 12],
      [0, 68, 60],
      [0, 80, 131],
      [3, 75, 202],
      [72, 60, 252],
      [156, 43, 255],
      [235, 36, 244],
      [255, 45, 194],
      [255, 73, 134],
      [255, 115, 86],
      [255, 164, 67],
      [235, 209, 85],
      [211, 241, 135],
      [215, 255, 200],
      [255, 255, 255]]),
))


class Cubehelix(Palette):
    """
    Representation of a Cubehelix color map with matplotlib compatible
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

    """
    url = url

    def __init__(self, name, colors):
        super(Cubehelix, self).__init__(name, palette_type, colors)

    @classmethod
    def make(cls, start=0.5, rotation=-1.5, gamma=1.0,
             start_hue=None, end_hue=None,
             sat=None, min_sat=1.2, max_sat=1.2,
             min_light=0., max_light=1.,
             n=256., reverse=False, name='custom_cubehelix'):
        """
        Create an arbitrary Cubehelix color palette from the algorithm.

        See http://adsabs.harvard.edu/abs/2011arXiv1108.5083G for a technical
        explanation of the algorithm.

        Parameters
        ----------
        start : scalar, optional
            Sets the starting position in the RGB color space. 0=blue, 1=red,
            2=green. Default is ``0.5`` (purple).
        rotation : scalar, optional
            The number of rotations through the rainbow. Can be positive
            or negative, indicating direction of rainbow. Negative values
            correspond to Blue->Red direction. Default is ``-1.5``.
        start_hue : scalar, optional
            Sets the starting color, ranging from [-360, 360]. Combined with
            `end_hue`, this parameter overrides ``start`` and ``rotation``.
            This parameter is based on the D3 implementation by @mbostock.
            Default is ``None``.
        end_hue : scalar, optional
            Sets the ending color, ranging from [-360, 360]. Combined with
            `start_hue`, this parameter overrides ``start`` and ``rotation``.
            This parameter is based on the D3 implementation by @mbostock.
            Default is ``None``.
        gamma : scalar, optional
            The gamma correction for intensity. Values of ``gamma < 1``
            emphasize low intensities while ``gamma > 1`` emphasises high
            intensities. Default is ``1.0``.
        sat : scalar, optional
            The uniform saturation intensity factor. ``sat=0`` produces
            grayscale, while ``sat=1`` retains the full saturation. Setting
            ``sat>1`` oversaturates the color map, at the risk of clipping
            the color scale. Note that ``sat`` overrides both ``min_stat``
            and ``max_sat`` if set.
        min_sat : scalar, optional
            Saturation at the minimum level. Default is ``1.2``.
        max_sat : scalar, optional
            Satuation at the maximum level. Default is ``1.2``.
        min_light : scalar, optional
            Minimum lightness value. Default is ``0``.
        max_light : scalar, optional
            Maximum lightness value. Default is ``1``.
        n : scalar, optional
            Number of discrete rendered colors. Default is ``256``.
        reverse : bool, optional
            Set to ``True`` to reverse the color map. Will go from black to
            white. Good for density plots where shade -> density.
            Default is ``False``.
        name : str, optional
            Name of the color map (defaults to ``'custom_cubehelix'``).

        Returns
        -------
        palette : `Cubehelix`
            A Cubehelix color palette.
        """
        if not HAVE_NPY:  # pragma: no cover
            raise RuntimeError('numpy not available.')
        # start_hue/end_hue were popularized by D3's implementation
        # and will override start/rotation if set
        if start_hue is not None and end_hue is not None:
            start = (start_hue / 360. - 1.) * 3.
            rotation = end_hue / 360. - start / 3. - 1.

        # lambd is effectively the color map grid
        lambd = np.linspace(min_light, max_light, n)

        # apply the gamma correction
        lambd_gamma = lambd ** gamma

        # Rotation angle
        # NOTE the equation for phi in Green 2011 does not have an extra `+1`
        # but the Fortran code does, as does the original cubehelix.py
        # I'm leaving out the +1 to keep to the original equation, but
        # worth investigating. In practice I see no difference!
        phi = 2.0 * np.pi * (start / 3.0 + rotation * lambd)

        if sat is None:
            sat = np.linspace(min_sat, max_sat, n)

        # Amplitude of helix from grayscale map
        amp = sat * lambd_gamma * (1. - lambd_gamma) / 2.

        # Compute the RGB vectors according to Green 2011 Eq 2
        rot_matrix = np.array([[-0.14861, +1.78277],
                               [-0.29227, -0.90649],
                               [+1.97294, 0.0]])
        sin_cos = np.array([np.cos(phi), np.sin(phi)])
        rgb = (lambd_gamma + amp * np.dot(rot_matrix, sin_cos)).T * 255.

        # Clipping is necessary in some cases when sat > 1
        np.clip(rgb, 0., 255., out=rgb)

        if reverse:
            rgb = rgb[::-1, :]

        colors = rgb.astype(int).tolist()
        return cls(name, colors)


def print_maps():
    """
    Print a list of pre-made Cubehelix palettes.

    """
    namelen = max(len(name) for name in palette_names)
    fmt = '{0:' + str(namelen + 4) + '}{1:16}'

    for name in palette_names:
        print(fmt.format(name, palette_type))


def get_map(name, reverse=False):
    """
    Get a pre-made Cubehelix palette by name.

    Parameters
    ----------
    name : str
        Name of map. Use `print_maps()` to see available names.
    reverse : bool, optional
        If True reverse colors from their default order.

    Returns
    -------
    palette : Cubehelix

    """
    try:
        # Make everthing lower case for matching
        index = [s.lower() for s in palette_names].index(name.lower())
    except ValueError:
        msg = "{0!r} is an unknown Cubehelix palette."
        raise KeyError(msg.format(name))

    real_name = palette_names[index]
    colors = palette_rgb[real_name]

    if reverse:
        real_name = real_name + '_r'
        colors = list(reversed(colors))

    return Cubehelix(real_name, colors)


def _get_all_maps():
    """
    Returns a dictionary of all Cubehelix palettes, including reversed ones.

    These default palettes are rendered with 16 colours.

    """
    d = {}
    for name in palette_names:
        d[name] = get_map(name)
        d[name + '_r'] = get_map(name, reverse=True)
    return d
