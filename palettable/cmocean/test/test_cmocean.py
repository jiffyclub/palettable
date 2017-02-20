from __future__ import absolute_import

import pytest

from ... import cmocean
from ... import utils


def test_print_maps_diverging(capsys):
    cmocean.diverging.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'Balance_3     diverging       3'


def test_print_maps_sequential(capsys):
    cmocean.sequential.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'Algae_3       sequential      3'


def test_get_map_diverging():
    palette = cmocean.diverging.get_map('BALANCE_5')
    assert isinstance(palette, cmocean.cmoceanpalette.CmoceanMap)
    assert palette.name == 'Balance_5'
    assert palette.type == 'diverging'
    assert len(palette.colors) == 5
    assert palette.url == 'http://matplotlib.org/cmocean/'


def test_get_map_sequential():
    palette = cmocean.sequential.get_map('AMP_5')
    assert isinstance(palette, cmocean.cmoceanpalette.CmoceanMap)
    assert palette.name == 'Amp_5'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 5
    assert palette.url == 'http://matplotlib.org/cmocean/'


def test_get_map_diverging_reversed():
    palette = cmocean.diverging.get_map('BALANCE_5', reverse=True)
    assert isinstance(palette, cmocean.cmoceanpalette.CmoceanMap)
    assert palette.name == 'Balance_5_r'
    assert palette.type == 'diverging'
    assert len(palette.colors) == 5
    assert palette.url == 'http://matplotlib.org/cmocean/'


def test_get_map_sequential_reversed():
    palette = cmocean.sequential.get_map('AMP_5', reverse=True)
    assert isinstance(palette, cmocean.cmoceanpalette.CmoceanMap)
    assert palette.name == 'Amp_5_r'
    assert palette.type == 'sequential'
    assert len(palette.colors) == 5
    assert palette.url == 'http://matplotlib.org/cmocean/'


def test_palettes_loaded():
    assert isinstance(
        cmocean.diverging.Balance_8, cmocean.cmoceanpalette.CmoceanMap)
    assert isinstance(
        cmocean.diverging.Balance_8_r, cmocean.cmoceanpalette.CmoceanMap)
    assert cmocean.diverging.Balance_8.type == 'diverging'

    assert isinstance(
        cmocean.sequential.Amp_8, cmocean.cmoceanpalette.CmoceanMap)
    assert isinstance(
        cmocean.sequential.Amp_8_r, cmocean.cmoceanpalette.CmoceanMap)
    assert cmocean.sequential.Amp_8.type == 'sequential'


def test_get_all_maps():
    # Smoke tests.
    assert isinstance(
        utils.load_all_palettes(
            cmocean.diverging._NAMES_AND_LENGTHS, cmocean.diverging.get_map),
        dict)
    assert isinstance(
        utils.load_all_palettes(
            cmocean.sequential._NAMES_AND_LENGTHS, cmocean.sequential.get_map),
        dict)
