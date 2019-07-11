from __future__ import absolute_import

from ... import lightbartlein
from ... import utils


def test_print_maps_diverging(capsys):
    lightbartlein.diverging.print_maps()
    out, err = capsys.readouterr()
    lines = out.split("\n")
    assert lines[0] == "BlueDarkOrange12_2     diverging       2"


def test_print_maps_sequential(capsys):
    lightbartlein.sequential.print_maps()
    out, err = capsys.readouterr()
    lines = out.split("\n")
    assert lines[0] == "Blues10_2     sequential      2"


def test_get_map_diverging():
    palette = lightbartlein.diverging.get_map("GreenMagenta_5")
    assert isinstance(palette, lightbartlein.lightbartlein.LightBartleinMap)
    assert palette.name == "GreenMagenta_5"
    assert palette.type == "diverging"
    assert len(palette.colors) == 5
    assert (
        palette.url == "http://geog.uoregon.edu/datagraphics/color_scales.htm"
    )


def test_get_map_sequential():
    palette = lightbartlein.sequential.get_map("Blues7_5")
    assert isinstance(palette, lightbartlein.lightbartlein.LightBartleinMap)
    assert palette.name == "Blues7_5"
    assert palette.type == "sequential"
    assert len(palette.colors) == 5
    assert (
        palette.url == "http://geog.uoregon.edu/datagraphics/color_scales.htm"
    )


def test_get_map_diverging_reversed():
    palette = lightbartlein.diverging.get_map("GreenMagenta_5", reverse=True)
    assert isinstance(palette, lightbartlein.lightbartlein.LightBartleinMap)
    assert palette.name == "GreenMagenta_5_r"
    assert palette.type == "diverging"
    assert len(palette.colors) == 5
    assert (
        palette.url == "http://geog.uoregon.edu/datagraphics/color_scales.htm"
    )


def test_get_map_sequential_reversed():
    palette = lightbartlein.sequential.get_map("Blues7_5", reverse=True)
    assert isinstance(palette, lightbartlein.lightbartlein.LightBartleinMap)
    assert palette.name == "Blues7_5_r"
    assert palette.type == "sequential"
    assert len(palette.colors) == 5
    assert (
        palette.url == "http://geog.uoregon.edu/datagraphics/color_scales.htm"
    )


def test_palettes_loaded():
    assert isinstance(
        lightbartlein.diverging.GreenMagenta_10,
        lightbartlein.lightbartlein.LightBartleinMap,
    )
    assert isinstance(
        lightbartlein.diverging.GreenMagenta_10_r,
        lightbartlein.lightbartlein.LightBartleinMap,
    )
    assert lightbartlein.diverging.GreenMagenta_10.type == 'diverging'

    assert isinstance(
        lightbartlein.sequential.Blues10_4,
        lightbartlein.lightbartlein.LightBartleinMap,
    )
    assert isinstance(
        lightbartlein.sequential.Blues10_4_r,
        lightbartlein.lightbartlein.LightBartleinMap,
    )
    assert lightbartlein.sequential.Blues10_4.type == 'sequential'


def test_get_all_maps():
    # Smoke tests.
    assert isinstance(
        utils.load_all_palettes(lightbartlein.diverging._NAMES_AND_LENGTHS,
                                lightbartlein.diverging.get_map),
        dict)
    assert isinstance(
        utils.load_all_palettes(lightbartlein.sequential._NAMES_AND_LENGTHS,
                                lightbartlein.sequential.get_map),
        dict)
