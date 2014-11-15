"""
Miscellaneous tests of colorbrewer functionality.

"""
try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

from .. import colorbrewer

@pytest.mark.parametrize('map_type', ['Sequential', 'Diverging', 'Qualitative'])
def test_load_maps_by_type(map_type):
    maps = colorbrewer._load_maps_by_type(map_type)

    assert len(maps) == len(colorbrewer.COLOR_MAPS[map_type])
    assert sorted(maps.keys()) == sorted(colorbrewer.COLOR_MAPS[map_type].keys())
