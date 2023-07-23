from __future__ import absolute_import

from ... import plotly
from ... import utils


def test_print_maps_diverging(capsys):
    plotly.diverging.print_maps()
    out, err = capsys.readouterr()
    lines = out.split("\n")
    assert lines[0] == "Picnic_2      diverging       2"


def test_print_maps_sequential(capsys):
    plotly.sequential.print_maps()
    out, err = capsys.readouterr()
    lines = out.split("\n")
    assert lines[0] == "Blackbody_2    sequential      2"


def test_print_maps_qualitative(capsys):
    plotly.qualitative.print_maps()
    out, err = capsys.readouterr()
    lines = out.split("\n")
    assert lines[0] == "Plotly_2       qualitative     2"


def test_get_map_diverging():
    palette = plotly.diverging.get_map("Picnic_9")
    assert isinstance(palette, plotly.plotly.PlotlyColorMap)
    assert palette.name == "Picnic_9"
    assert palette.type == "diverging"
    assert len(palette.colors) == 9
    assert palette.url == "https://plotly.com/python/"


def test_get_map_sequential():
    palette = plotly.sequential.get_map("Jet_6")
    assert isinstance(palette, plotly.plotly.PlotlyColorMap)
    assert palette.name == "Jet_6"
    assert palette.type == "sequential"
    assert len(palette.colors) == 6
    assert palette.url == "https://plotly.com/python/"


def test_get_map_qualitative():
    palette = plotly.qualitative.get_map("D3_10")
    assert isinstance(palette, plotly.plotly.PlotlyColorMap)
    assert palette.name == "D3_10"
    assert palette.type == "qualitative"
    assert len(palette.colors) == 10
    assert palette.url == "https://plotly.com/python/"


def test_get_map_diverging_reversed():
    palette = plotly.diverging.get_map("Picnic_9", reverse=True)
    assert isinstance(palette, plotly.plotly.PlotlyColorMap)
    assert palette.name == "Picnic_9_r"
    assert palette.type == "diverging"
    assert len(palette.colors) == 9
    assert palette.url == "https://plotly.com/python/"


def test_get_map_sequential_reversed():
    palette = plotly.sequential.get_map("Jet_6", reverse=True)
    assert isinstance(palette, plotly.plotly.PlotlyColorMap)
    assert palette.name == "Jet_6_r"
    assert palette.type == "sequential"
    assert len(palette.colors) == 6
    assert palette.url == "https://plotly.com/python/"


def test_get_map_qualitative_reversed():
    palette = plotly.qualitative.get_map("D3_10", reverse=True)
    assert isinstance(palette, plotly.plotly.PlotlyColorMap)
    assert palette.name == "D3_10_r"
    assert palette.type == "qualitative"
    assert len(palette.colors) == 10
    assert palette.url == "https://plotly.com/python/"


def test_palettes_loaded():
    assert isinstance(
        plotly.diverging.Picnic_5,
        plotly.plotly.PlotlyColorMap,
    )
    assert isinstance(
        plotly.diverging.Picnic_5_r,
        plotly.plotly.PlotlyColorMap,
    )
    assert plotly.diverging.Picnic_5.type == "diverging"

    assert isinstance(
        plotly.sequential.Electric_4,
        plotly.plotly.PlotlyColorMap,
    )
    assert isinstance(
        plotly.sequential.Electric_4_r,
        plotly.plotly.PlotlyColorMap,
    )
    assert plotly.sequential.Electric_4.type == "sequential"

    assert isinstance(
        plotly.qualitative.Alphabet_14,
        plotly.plotly.PlotlyColorMap,
    )
    assert isinstance(
        plotly.qualitative.Alphabet_14_r,
        plotly.plotly.PlotlyColorMap,
    )
    assert plotly.qualitative.Alphabet_10.type == "qualitative"


def test_get_all_maps():
    # Smoke tests.
    assert isinstance(
        utils.load_all_palettes(
            plotly.diverging._NAMES_AND_LENGTHS, plotly.diverging.get_map
        ),
        dict,
    )
    assert isinstance(
        utils.load_all_palettes(
            plotly.sequential._NAMES_AND_LENGTHS,
            plotly.sequential.get_map,
        ),
        dict,
    )
    assert isinstance(
        utils.load_all_palettes(
            plotly.qualitative._NAMES_AND_LENGTHS,
            plotly.qualitative.get_map,
        ),
        dict,
    )
