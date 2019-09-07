from __future__ import absolute_import

from ... import scientific
from ... import utils


def test_print_maps_diverging(capsys):
    scientific.diverging.print_maps()
    out, err = capsys.readouterr()
    lines = out.split("\n")
    assert lines[0] == "Broc_3       diverging       3"


def test_print_maps_sequential(capsys):
    scientific.sequential.print_maps()
    out, err = capsys.readouterr()
    lines = out.split("\n")
    assert lines[0] == "Devon_3       sequential      3"


def test_get_map_diverging():
    palette = scientific.diverging.get_map("Lisbon_19")
    assert isinstance(palette, scientific.scientific.ScientificMap)
    assert palette.name == "Lisbon_19"
    assert palette.type == "diverging"
    assert len(palette.colors) == 19
    assert (
        palette.url == "http://www.fabiocrameri.ch/colourmaps.php"
    )


def test_get_map_sequential():
    palette = scientific.sequential.get_map("Buda_6")
    assert isinstance(palette, scientific.scientific.ScientificMap)
    assert palette.name == "Buda_6"
    assert palette.type == "sequential"
    assert len(palette.colors) == 6
    assert (
        palette.url == "http://www.fabiocrameri.ch/colourmaps.php"
    )


def test_get_map_diverging_reversed():
    palette = scientific.diverging.get_map("Lisbon_19", reverse=True)
    assert isinstance(palette, scientific.scientific.ScientificMap)
    assert palette.name == "Lisbon_19_r"
    assert palette.type == "diverging"
    assert len(palette.colors) == 19
    assert (
        palette.url == "http://www.fabiocrameri.ch/colourmaps.php"
    )


def test_get_map_sequential_reversed():
    palette = scientific.sequential.get_map("Buda_6", reverse=True)
    assert isinstance(palette, scientific.scientific.ScientificMap)
    assert palette.name == "Buda_6_r"
    assert palette.type == "sequential"
    assert len(palette.colors) == 6
    assert (
        palette.url == "http://www.fabiocrameri.ch/colourmaps.php"
    )


def test_palettes_loaded():
    assert isinstance(
        scientific.diverging.Tofino_10,
        scientific.scientific.ScientificMap,
    )
    assert isinstance(
        scientific.diverging.Tofino_10_r,
        scientific.scientific.ScientificMap,
    )
    assert scientific.diverging.Tofino_10.type == 'diverging'

    assert isinstance(
        scientific.sequential.Nuuk_9,
        scientific.scientific.ScientificMap,
    )
    assert isinstance(
        scientific.sequential.Nuuk_9_r,
        scientific.scientific.ScientificMap,
    )
    assert scientific.sequential.Nuuk_9.type == 'sequential'


def test_get_all_maps():
    # Smoke tests.
    assert isinstance(
        utils.load_all_palettes(scientific.diverging._NAMES_AND_LENGTHS,
                                scientific.diverging.get_map),
        dict)
    assert isinstance(
        utils.load_all_palettes(scientific.sequential._NAMES_AND_LENGTHS,
                                scientific.sequential.get_map),
        dict)
