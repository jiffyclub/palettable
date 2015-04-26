# coding: utf-8
"""
Cubehelix color maps and palettes.

The Cubehelix algorithm makes color scales with monotonic changes in percieved
brightness. This means that a cubehelix color map automatically transforms to
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

import numpy as np

from ..palette import Palette


url = 'http://adsabs.harvard.edu/abs/2011arXiv1108.5083G'
palette_type = 'sequential'


class Cubehelix(Palette):
    """
    Representation of a Cubehelix color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str, optional
        Name of the color map (defaults to ``'custom_cubehelix'``).
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
        The gamma correction for intensity. Values of ``gamma < 1`` emphasize
        low intensities while ``gamma > 1`` emphasises high intensities.
        Default is ``1.0``.
    sat : scalar, optional
        The uniform saturation intensity factor. ``sat=0`` produces grayscale,
        while ``sat=1`` retains the full saturation. Setting ``sat>1``
        oversaturates the color map, at the risk of clipping the color scale.
        Note that ``sat`` overrides both ``min_stat`` and ``max_sat`` if set.
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

    """
    url = url

    def __init__(self, name="custom_cubehelix", **kwargs):
        colors = Cubehelix._cubehelix(**kwargs)
        super(Cubehelix, self).__init__(name, palette_type, colors)

    @staticmethod
    def _cubehelix(start=0.5, rotation=-1.5, gamma=1.0,
                   start_hue=None, end_hue=None,
                   sat=None, min_sat=1.2, max_sat=1.2,
                   min_light=0., max_light=1.,
                   n=256., reverse=False):
        """
        Create a sequence of RGB colours given cubehelix algorithm parameters.

        See http://adsabs.harvard.edu/abs/2011arXiv1108.5083G for a technical
        explanation of the algorithm.

        Returns a (n, 3) array of colour values, scaled from 0 to 255.

        """
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

        return rgb
