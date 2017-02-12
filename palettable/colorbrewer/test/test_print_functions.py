"""
Test the colorbrewer print functions. The output is not actually tested,
but the functions are fully exercised to catch errors.

"""
from __future__ import absolute_import

try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

from .. import colorbrewer


def test_print_maps1(capsys):
    # just make sure there are no errors
    colorbrewer.print_maps()
    out, err = capsys.readouterr()
    assert out


def test_print_maps2(capsys):
    # just make sure there are no errors
    colorbrewer.print_maps('sequential')
    out, err = capsys.readouterr()
    assert out


def test_print_maps3(capsys):
    # just make sure there are no errors
    colorbrewer.print_maps('sequential', 6)
    out, err = capsys.readouterr()
    assert out


def test_print_maps_raises():
    with pytest.raises(ValueError):
        colorbrewer.print_maps(number=6)


def test_print_all_maps(capsys):
    # just make sure there are no errors
    colorbrewer.print_all_maps()
    out, err = capsys.readouterr()
    assert out


def test_print_maps_by_type1(capsys):
    # just make sure there are no errors
    colorbrewer.print_maps_by_type('qualitative')
    out, err = capsys.readouterr()
    assert out


def test_print_maps_by_type2(capsys):
    # just make sure there are no errors
    colorbrewer.print_maps_by_type('qualitative', number=6)
    out, err = capsys.readouterr()
    assert out


def test_print_maps_by_type_raises():
    with pytest.raises(ValueError):
        colorbrewer.print_maps_by_type('notarealtype')
