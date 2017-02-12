"""
Test the get_map function.

"""
from __future__ import absolute_import

try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

from .. import colorbrewer


def reverse(sequence):
    return [x for x in reversed(sequence)]


def test_get_map_reverse():
    bmap = colorbrewer.get_map('Greens', 'sequential', 8)
    bmap_r = colorbrewer.get_map('Greens', 'sequential', 8, reverse=True)

    assert bmap.type == bmap_r.type
    assert bmap.name + '_r' == bmap_r.name
    assert bmap.number == bmap_r.number
    assert bmap.colors == reverse(bmap_r.colors)


def test_get_map_raises_bad_type():
    with pytest.raises(ValueError):
        colorbrewer.get_map('Greens', 'FakeType', 8)


def test_get_map_raises_bad_name():
    with pytest.raises(ValueError):
        colorbrewer.get_map('FakeName', 'sequential', 8)


def test_get_map_raises_bad_number():
    with pytest.raises(ValueError):
        colorbrewer.get_map('Greens', 'sequential', 99)


class TestCaseSensitivity(object):
    def test_type1(self):
        bmap = colorbrewer.get_map('Greens', 'SEQUENTIAL', 8)
        assert bmap.name == 'Greens'
        assert bmap.type == 'sequential'
        assert bmap.number == 8

    def test_type2(self):
        bmap = colorbrewer.get_map('Greens', 'sequential', 8)
        assert bmap.name == 'Greens'
        assert bmap.type == 'sequential'
        assert bmap.number == 8

    def test_type3(self):
        bmap = colorbrewer.get_map('Greens', 'SeQuEnTiAl', 8)
        assert bmap.name == 'Greens'
        assert bmap.type == 'sequential'
        assert bmap.number == 8

    def test_name1(self):
        bmap = colorbrewer.get_map('GREENS', 'Sequential', 8)
        assert bmap.name == 'Greens'
        assert bmap.type == 'sequential'
        assert bmap.number == 8

    def test_name2(self):
        bmap = colorbrewer.get_map('greens', 'Sequential', 8)
        assert bmap.name == 'Greens'
        assert bmap.type == 'sequential'
        assert bmap.number == 8

    def test_name3(self):
        bmap = colorbrewer.get_map('GrEeNs', 'Sequential', 8)
        assert bmap.name == 'Greens'
        assert bmap.type == 'sequential'
        assert bmap.number == 8

    def test_name4(self):
        bmap = colorbrewer.get_map('piyg', 'Diverging', 8)
        assert bmap.name == 'PiYG'
        assert bmap.type == 'diverging'
        assert bmap.number == 8
