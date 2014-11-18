
try:
    import pytest
except ImportError:
    raise ImportError('Tests require pytest >= 2.2.')

from brewer2mpl import tableau

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
    tableau.get_map('Tableau 10')
    tableau.get_map('Tableau 10', reverse=True)

def test_get_all_maps():
    # Smoke tests.
    tableau.get_all_maps()
