from __future__ import absolute_import

from ... import matplotlib as mpl
from ... import utils


def test_print_maps(capsys):
    mpl.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'Inferno_3     sequential      3'


def test_get_map():
    palette = mpl.get_map('VIRIDIS_5')
    assert isinstance(palette, mpl.matplotlib.MatplotlibMap)
    assert palette.name == 'Viridis_5'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 5
    assert palette.url == 'https://bids.github.io/colormap'


def test_get_map_reversed():
    palette = mpl.get_map('VIRIDIS_5', reverse=True)
    assert isinstance(palette, mpl.matplotlib.MatplotlibMap)
    assert palette.name == 'Viridis_5_r'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 5
    assert palette.url == 'https://bids.github.io/colormap'


def test_palettes_loaded():
    assert isinstance(mpl.Viridis_8, mpl.matplotlib.MatplotlibMap)
    assert isinstance(mpl.Viridis_8_r, mpl.matplotlib.MatplotlibMap)
    assert mpl.Viridis_8.type == 'sequential'


def test_get_all_maps():
    # Smoke tests.
    assert isinstance(
        utils.load_all_palettes(mpl._NAMES_AND_LENGTHS, mpl.get_map), dict)
