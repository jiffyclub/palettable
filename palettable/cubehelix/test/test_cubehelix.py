# coding: utf-8

# import numpy as np

from ... import cubehelix


def test_get_map():
    palette = cubehelix.get_map('CLASSIC')
    assert palette.name == 'classic'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 256
    assert palette.url == 'http://adsabs.harvard.edu/abs/2011arXiv1108.5083G'


def test_get_map_reversed():
    palette = cubehelix.get_map('classic', reverse=False)
    palette_r = cubehelix.get_map('classic', reverse=True)
    assert palette.hex_colors[0] == palette_r.hex_colors[-1]


def test_palettes_loaded():
    assert isinstance(cubehelix.classic, cubehelix.Cubehelix)
    assert isinstance(cubehelix.classic_r, cubehelix.Cubehelix)


def test_default_is_classic():
    classic_palette = cubehelix.get_map('classic')
    default_palette = cubehelix.Cubehelix(n=256)
    assert classic_palette.hex_colors[0] == default_palette.hex_colors[0]
    assert classic_palette.hex_colors[128] == default_palette.hex_colors[128]
    assert classic_palette.hex_colors[255] == default_palette.hex_colors[255]
    # Test consistency
    known_colors = ['#000000', '#237433', '#DB8ACB', '#FFFFFF']
    palette = cubehelix.Cubehelix(n=4)
    for c1, c2 in zip(palette.hex_colors, known_colors):
        assert c1 == c2


def test_start_end_hue():
    # Test to make sure result is consistent
    palette = cubehelix.Cubehelix(start_hue=240., end_hue=-300.,
                                  min_sat=1., max_sat=2.5,
                                  min_light=0.3, max_light=0.8, gamma=.9, n=4)
    known_colors = ['#873B61', '#677BDC', '#47DF91', '#E9D575']
    for c1, c2 in zip(palette.hex_colors, known_colors):
        assert c1 == c2
