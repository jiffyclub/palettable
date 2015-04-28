# coding: utf-8

# import numpy as np

from ... import cubehelix


def test_get_map():
    palette = cubehelix.get_map('CLASSIC')
    assert palette.name == 'classic'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 16
    assert palette.url == 'http://adsabs.harvard.edu/abs/2011arXiv1108.5083G'


def test_get_map_reversed():
    palette = cubehelix.get_map('classic', reverse=False)
    palette_r = cubehelix.get_map('classic', reverse=True)
    assert palette.colors == palette_r.colors[::-1]


def test_palettes_loaded():
    assert isinstance(cubehelix.classic, cubehelix.Cubehelix)
    assert isinstance(cubehelix.classic_r, cubehelix.Cubehelix)


def test_default_is_classic():
    classic_palette = cubehelix.get_map('classic')
    default_palette = cubehelix.Cubehelix.make(n=16)
    assert classic_palette.colors == default_palette.colors


def test_classic():
    palette = cubehelix.Cubehelix.make(start=0.5, rotation=-1.5, gamma=1.0,
                                       sat=1.2, min_light=0., max_light=1.,
                                       n=16)
    assert palette.colors == cubehelix.get_map('classic').colors


def test_perceptual_rainbow():
    palette = cubehelix.Cubehelix.make(start_hue=240., end_hue=-300.,
                                       min_sat=1., max_sat=2.5,
                                       min_light=0.3, max_light=0.8, gamma=.9,
                                       n=16)
    assert palette.colors == cubehelix.get_map('perceptual_rainbow').colors


def test_purple():
    palette = cubehelix.Cubehelix.make(start=0., rotation=0.0, n=16)
    assert palette.colors == cubehelix.get_map('purple').colors


def test_jim_special():
    palette = cubehelix.Cubehelix.make(start=0.3, rotation=-0.5, n=16)
    assert palette.colors == cubehelix.get_map('jim_special').colors


def test_red():
    palette = cubehelix.Cubehelix.make(start=0., rotation=0.5, n=16)
    assert palette.colors == cubehelix.get_map('red').colors


def test_cubehelix1():
    palette = cubehelix.Cubehelix.make(gamma=1.0, start=1.5,
                                       rotation=-1.0, sat=1.5, n=16)
    assert palette.colors == cubehelix.get_map('cubehelix1').colors


def test_cubehelix2():
    palette = cubehelix.Cubehelix.make(gamma=1.0, start=2.0, rotation=1.0,
                                       sat=1.5, n=16)
    assert palette.colors == cubehelix.get_map('cubehelix2').colors


def test_cubehelix3():
    palette = cubehelix.Cubehelix.make(gamma=1.0, start=2.0, rotation=1.0,
                                       sat=3, n=16)
    assert palette.colors == cubehelix.get_map('cubehelix3').colors
