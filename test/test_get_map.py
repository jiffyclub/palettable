"""
Test the get_map function.

"""
try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

import brewer2mpl


def reverse(sequence):
    return [x for x in reversed(sequence)]


def test_get_map_reverse():
    bmap = brewer2mpl.get_map('Greens', 'Sequential', 8)
    bmap_r = brewer2mpl.get_map('Greens', 'Sequential', 8, reverse=True)

    assert bmap.type == bmap_r.type
    assert bmap.name + '_r' == bmap_r.name
    assert bmap.number == bmap_r.number
    assert bmap.colors == reverse(bmap_r.colors)


def test_get_map_raises():
    with pytest.raises(ValueError):
        brewer2mpl.get_map('FakeName', 'FakeType', 8)
