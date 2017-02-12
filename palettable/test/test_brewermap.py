"""
Test the BrewerMap class.

"""
from __future__ import absolute_import

import os
import sys
import tempfile

try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

# figure out which URL lib to import
if sys.version_info[0] == 2:
    import urllib2 as urllib
else:
    import urllib.request as urllib

try:
    from matplotlib.colors import LinearSegmentedColormap
except ImportError:
    HAVE_MPL = False
else:
    HAVE_MPL = True

import mock
from ipythonblocks import BlockGrid

from .. import colorbrewer


@pytest.fixture
def img_filename(request):
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        fname = f.name

    def delete():
        if os.path.exists(fname):
            os.remove(fname)
    request.addfinalizer(delete)

    return fname


class TestBrewerMap(object):
    @classmethod
    def setup_class(cls):
        name = 'TestMap'
        map_type = 'TestType'
        colors = [(0, 0, 0), (12, 134, 245), (255, 255, 255)]

        cls.bmap = colorbrewer.BrewerMap(name, map_type, colors)

        cls.name = name
        cls.map_type = map_type
        cls.colors = colors

    def test_init(self):
        assert self.bmap.name == self.name
        assert self.bmap.type == self.map_type
        assert self.bmap.colors == self.colors
        assert self.bmap.number == len(self.colors)

    def test_colorbrewer2_url(self):
        url = 'http://colorbrewer2.org/index.html?type=testtype&scheme=TestMap&n=3'
        assert self.bmap.colorbrewer2_url == url

    def test_colorbrewer2_url_exists(self):
        '''Simple check to ensure a URL is valid. Thanks to
        http://stackoverflow.com/questions/4041443'''
        try:
            urllib.urlopen(self.bmap.colorbrewer2_url)
            assert True
        except:
            assert False

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

    @mock.patch.object(BlockGrid, 'show')
    def test_show_as_blocks(self, mock_show):
        self.bmap.show_as_blocks()
        mock_show.assert_called_with()

    @pytest.mark.skipif('not HAVE_MPL')
    def test_save_discrete_image(self, img_filename):
        self.bmap.save_discrete_image(img_filename)
        assert os.path.isfile(img_filename)

    @pytest.mark.skipif('not HAVE_MPL')
    def test_save_continuous_image(self, img_filename):
        self.bmap.save_continuous_image(img_filename)
        assert os.path.isfile(img_filename)
