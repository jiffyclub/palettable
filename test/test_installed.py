"""
Test installed palettable to make sure everything is accessible.

"""

import palettable
from palettable.palette import Palette


def test_colorbrewer():
    assert isinstance(palettable.colorbrewer.diverging.PuOr_6, Palette)
    assert isinstance(palettable.colorbrewer.qualitative.Pastel1_9, Palette)
    assert isinstance(palettable.colorbrewer.sequential.PuBuGn_9, Palette)


def test_cubehelix():
    assert isinstance(palettable.cubehelix.classic_16, Palette)


def test_tableau():
    assert isinstance(palettable.tableau.ColorBlind_10, Palette)


def test_wes_anderson():
    assert isinstance(palettable.wesanderson.Aquatic1_5, Palette)
