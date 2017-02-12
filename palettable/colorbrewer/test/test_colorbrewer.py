"""
Miscellaneous tests of colorbrewer functionality.

"""
from __future__ import absolute_import

try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

from .. import colorbrewer
from .. import diverging
from .. import qualitative
from .. import sequential


@pytest.mark.parametrize(
    'map_type', ['sequential', 'diverging', 'qualitative'])
def test_load_maps_by_type(map_type):
    maps = colorbrewer._load_maps_by_type(map_type)

    m = list(maps.values())[0]

    assert isinstance(m, colorbrewer.BrewerMap)
    assert m.type == map_type


def test_diverging():
    assert hasattr(diverging, 'BrBG_11_r')
    assert isinstance(diverging.BrBG_11_r, colorbrewer.BrewerMap)
    assert diverging.BrBG_11_r.type == 'diverging'


def test_qualitative():
    assert hasattr(qualitative, 'Set3_12')
    assert isinstance(qualitative.Set3_12, colorbrewer.BrewerMap)
    assert qualitative.Set3_12.type == 'qualitative'


def test_sequential():
    assert hasattr(sequential, 'Blues_6_r')
    assert isinstance(sequential.Blues_6_r, colorbrewer.BrewerMap)
    assert sequential.Blues_6_r.type == 'sequential'
