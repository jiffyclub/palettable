from __future__ import absolute_import

from ... import mycarta
from ... import utils


def test_print_maps(capsys):
    mycarta.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'Cube1_3       sequential      3'


def test_get_map():
    palette = mycarta.get_map('LINEARL_5')
    assert isinstance(palette, mycarta.mycarta.MycartaMap)
    assert palette.name == 'LinearL_5'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 5
    assert palette.url == 'https://mycarta.wordpress.com/color-palettes/'


def test_get_map_reversed():
    palette = mycarta.get_map('LINEARL_5', reverse=True)
    assert isinstance(palette, mycarta.mycarta.MycartaMap)
    assert palette.name == 'LinearL_5_r'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 5
    assert palette.url == 'https://mycarta.wordpress.com/color-palettes/'


def test_palettes_loaded():
    assert isinstance(mycarta.CubeYF_8, mycarta.mycarta.MycartaMap)
    assert isinstance(mycarta.CubeYF_8_r, mycarta.mycarta.MycartaMap)
    assert mycarta.CubeYF_8.type == 'sequential'


def test_get_all_maps():
    # Smoke tests.
    assert isinstance(
        utils.load_all_palettes(mycarta._NAMES_AND_LENGTHS, mycarta.get_map),
        dict)
