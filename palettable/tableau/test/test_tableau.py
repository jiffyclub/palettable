from __future__ import absolute_import

try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

from ... import tableau


def test_print_maps(capsys):
    # just make sure there are no errors
    tableau.print_maps()
    out, err = capsys.readouterr()
    assert out


def test_get_map_bad_name():
    with pytest.raises(KeyError):
        tableau.get_map('bad name')


def test_get_map():
    # Smoke tests.
    assert isinstance(
        tableau.get_map('Tableau_10'), tableau.tableau.TableauMap)
    assert isinstance(
        tableau.get_map(
            'Tableau_10', reverse=True), tableau.tableau.TableauMap)


def test_get_all_maps():
    # Smoke tests.
    maps = tableau.tableau._get_all_maps()
    assert isinstance(maps, dict)
    assert 'Tableau_10' in maps
    assert 'Tableau_10_r' in maps


def test_maps_loaded():
    assert hasattr(tableau, 'ColorBlind_10')
    assert hasattr(tableau, 'ColorBlind_10_r')
    assert tableau.ColorBlind_10.type == 'qualitative'
