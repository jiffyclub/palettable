from __future__ import absolute_import

import pytest

from ... import cartocolors
from ... import utils


def test_print_maps_diverging(capsys):
    cartocolors.diverging.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'ArmyRose_2    diverging       2'


def test_print_maps_qualitative(capsys):
    cartocolors.qualitative.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'Antique_2     qualitative     2'


def test_print_maps_sequential(capsys):
    cartocolors.sequential.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'BluGrn_2        sequential      2'


def test_get_map_diverging():
    palette = cartocolors.diverging.get_map('Geyser_5')
    assert isinstance(palette, cartocolors.cartocolorspalette.CartoColorsMap)
    assert palette.name == 'Geyser_5'
    assert palette.type == 'diverging'
    assert len(palette.colors) == 5
    assert palette.url == 'https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names'


def test_get_map_qualitative():
    palette = cartocolors.qualitative.get_map('Bold_5')
    assert isinstance(palette, cartocolors.cartocolorspalette.CartoColorsMap)
    assert palette.name == 'Bold_5'
    assert palette.type == 'qualitative'
    assert len(palette.colors) == 5
    assert palette.url == 'https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names'


def test_get_map_sequential():
    palette = cartocolors.sequential.get_map('agGrnYl_3')
    assert isinstance(palette, cartocolors.cartocolorspalette.CartoColorsMap)
    assert palette.name == 'agGrnYl_3'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 3
    assert palette.url == 'https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names'


def test_get_map_diverging_reversed():
    palette = cartocolors.diverging.get_map('Earth_3_r', reverse=True)
    assert isinstance(palette, cartocolors.cartocolorspalette.CartoColorsMap)
    assert palette.name == 'Earth_3_r'
    assert palette.type == 'diverging'
    assert len(palette.colors) == 3
    assert palette.url == 'https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names'


def test_get_map_qualitative_reversed():
    palette = cartocolors.qualitative.get_map('Safe_3_r', reverse=True)
    assert isinstance(palette, cartocolors.cartocolorspalette.CartoColorsMap)
    assert palette.name == 'Safe_3_r'
    assert palette.type == 'qualitative'
    assert len(palette.colors) == 3
    assert palette.url == 'https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names'


def test_get_map_sequential_reversed():
    palette = cartocolors.sequential.get_map('Mint_5', reverse=True)
    assert isinstance(palette, cartocolors.cartocolorspalette.CartoColorsMap)
    assert palette.name == 'Mint_5_r'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 5
    assert palette.url == 'https://github.com/CartoDB/CartoColor/wiki/CARTOColor-Scheme-Names'


def test_palettes_loaded():
    assert isinstance(cartocolors.diverging.Earth_7,
                      cartocolors.cartocolorspalette.CartoColorsMap)
    assert isinstance(cartocolors.diverging.Earth_7_r,
                      cartocolors.cartocolorspalette.CartoColorsMap)
    assert cartocolors.diverging.Earth_7.type == 'diverging'

    assert isinstance(cartocolors.qualitative.Vivid_4,
                      cartocolors.cartocolorspalette.CartoColorsMap)
    assert isinstance(cartocolors.qualitative.Vivid_4_r,
                      cartocolors.cartocolorspalette.CartoColorsMap)
    assert cartocolors.qualitative.Vivid_4.type == 'qualitative'

    assert isinstance(cartocolors.sequential.BluGrn_7,
                      cartocolors.cartocolorspalette.CartoColorsMap)
    assert isinstance(cartocolors.sequential.BluGrn_7_r,
                      cartocolors.cartocolorspalette.CartoColorsMap)
    assert cartocolors.sequential.BluGrn_7.type == 'sequential'


def test_get_all_maps():
    # Smoke tests.
    assert isinstance(
        utils.load_all_palettes(cartocolors.diverging._NAMES_AND_LENGTHS,
                                cartocolors.diverging.get_map),
        dict)
    assert isinstance(
        utils.load_all_palettes(cartocolors.qualitative._NAMES_AND_LENGTHS,
                                cartocolors.qualitative.get_map),
        dict)
    assert isinstance(
        utils.load_all_palettes(cartocolors.sequential._NAMES_AND_LENGTHS,
                                cartocolors.sequential.get_map),
        dict)
