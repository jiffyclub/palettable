"""
Test the BrewerMap class.

"""

try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

try:
    from matplotlib.colors import LinearSegmentedColormap
except ImportError:
    HAVE_MPL = False
else:
    HAVE_MPL = True

import brewer2mpl


class TestBrewerMap(object):
    @classmethod
    def setup_class(cls):
        name = 'TestMap'
        map_type = 'TestType'
        colors = [(0, 0, 0), (12, 134, 245), (255, 255, 255)]

        cls.bmap = brewer2mpl.BrewerMap(name, map_type, colors)

        cls.name = name
        cls.map_type = map_type
        cls.colors = colors

    def test_init(self):
        assert self.bmap.name == self.name
        assert self.bmap.type == self.map_type
        assert self.bmap.colors == self.colors
        assert self.bmap.number == len(self.colors)

    def test_colorbrewer2_url(self):
        url = 'http://colorbrewer2.org/index.php?type=testtype&scheme=TestMap&n=3'
        assert self.bmap.colorbrewer2_url == url

    def test_hex_colors(self):
        hex_colors = ['#000000', '#0C86F5', '#FFFFFF']
        assert self.bmap.hex_colors == hex_colors

    def test_mpl_colors(self):
        mpl_colors = [(0, 0, 0), (12/255., 134/255., 245/255.), (1, 1, 1)]
        assert self.bmap.mpl_colors == mpl_colors

    @pytest.mark.skipif('not HAVE_MPL')
    def test_mpl_colormap(self):
        mpl_colormap = self.bmap.mpl_colormap
        assert isinstance(mpl_colormap, LinearSegmentedColormap)
