"""
Miscellaneous tests of brewer2mpl functionality.

"""
try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

from brewer2mpl import brewer2mpl

@pytest.mark.parametrize('map_type', ['Sequential', 'Diverging', 'Qualitative'])
def test_load_maps_by_type(map_type):
    maps = brewer2mpl._load_maps_by_type(map_type)

    assert len(maps) == len(brewer2mpl.COLOR_MAPS[map_type])
    assert sorted(maps.keys()) == sorted(brewer2mpl.COLOR_MAPS[map_type].keys())
