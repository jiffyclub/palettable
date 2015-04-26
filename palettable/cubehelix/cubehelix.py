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
    start : scalar, optional
        Sets the starting position in the color space. 0=blue, 1=red,
        2=green. Defaults to 0.5.
    rot : scalar, optional
        The number of rotations through the rainbow. Can be positive
        or negative, indicating direction of rainbow. Negative values
        correspond to Blue->Red direction. Defaults to -1.5
    gamma : scalar, optional
        The gamma correction for intensity. Defaults to 1.0
    reverse : boolean, optional
        Set to True to reverse the color map. Will go from black to
        white. Good for density plots where shade~density. Defaults to False
    nlev : scalar, optional
        Defines the number of discrete levels to render colors at.
        Defaults to 256.
    sat : scalar, optional
        The saturation intensity factor. Defaults to 1.2
        NOTE: this was formerly known as "hue" parameter
    minSat : scalar, optional
        Sets the minimum-level saturation. Defaults to 1.2
    maxSat : scalar, optional
        Sets the maximum-level saturation. Defaults to 1.2
    startHue : scalar, optional
        Sets the starting color, ranging from [0, 360], as in
        D3 version by @mbostock
        NOTE: overrides values in start parameter
    endHue : scalar, optional
        Sets the ending color, ranging from [0, 360], as in
        D3 version by @mbostock
        NOTE: overrides values in rot parameter
    minLight : scalar, optional
        Sets the minimum lightness value. Defaults to 0.
    maxLight : scalar, optional
        Sets the maximum lightness value. Defaults to 1.
    """
    url = url

    def __init__(self, name="custom_cubehelix", **kwargs):
        colors = Cubehelix._cubehelix(**kwargs)
        super(Cubehelix, self).__init__(name, palette_type, colors)

    @staticmethod
    def _cubehelix(start=0.5, rot=-1.5, gamma=1.0, reverse=False, nlev=256.,
                   minSat=1.2, maxSat=1.2, minLight=0., maxLight=1., **kwargs):
        """
        Create a sequence of RGB colours given cubehelix algorithm parameters.

        """
        # override start and rot if startHue and endHue are set
        if kwargs is not None:
            if 'startHue' in kwargs:
                start = (kwargs.get('startHue') / 360. - 1.) * 3.
            if 'endHue' in kwargs:
                rot = kwargs.get('endHue') / 360. - start / 3. - 1.
            if 'sat' in kwargs:
                minSat = kwargs.get('sat')
                maxSat = kwargs.get('sat')

        # set up the parameters
        fract = np.linspace(minLight, maxLight, nlev)
        angle = 2.0 * np.pi * (start / 3.0 + rot * fract + 1.)
        fract = fract**gamma

        satar = np.linspace(minSat, maxSat, nlev)
        amp = satar * fract * (1. - fract) / 2.

        # compute the RGB vectors according to main equations
        cos_angle = np.cos(angle)
        sin_angle = np.sin(angle)
        red = fract + amp * (-0.14861 * cos_angle + 1.78277 * sin_angle)
        grn = fract + amp * (-0.29227 * cos_angle - 0.90649 * sin_angle)
        blu = fract + amp * (1.97294 * cos_angle)

        # find where RBB are outside the range [0,1], clip
        red[np.where((red > 1.))] = 1.
        grn[np.where((grn > 1.))] = 1.
        blu[np.where((blu > 1.))] = 1.

        red[np.where((red < 0.))] = 0.
        grn[np.where((grn < 0.))] = 0.
        blu[np.where((blu < 0.))] = 0.

        # optional color reverse
        if reverse is True:
            red = red[::-1]
            blu = blu[::-1]
            grn = grn[::-1]

        colors = zip(red * 255., grn * 255., blu * 255.)
        return colors
