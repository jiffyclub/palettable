from __future__ import absolute_import

import inspect

import pytest

from .. import utils
from ..mycarta import mycarta


def test_round_as_py3():
    assert utils.round_as_py3(2.2) == 2.0
    assert utils.round_as_py3(2.5) == 2.0
    assert utils.round_as_py3(2.6) == 3.0
    assert utils.round_as_py3(3.5) == 4.0


@pytest.mark.parametrize('num, length, expected', [
    (2, 5, [0, 4]),
    (3, 5, [0, 2, 4]),
    (4, 5, [0, 1, 3, 4]),
    (5, 5, [0, 1, 2, 3, 4]),
    (2, 10, [0, 9]),
    (3, 10, [0, 4, 9]),
    (4, 10, [0, 3, 6, 9]),
    (5, 10, [0, 2, 4, 7, 9]),
    (6, 10, [0, 2, 4, 5, 7, 9]),
    (10, 10, list(range(10)))
])
def test_n_to_indices(num, length, expected):
    assert list(utils.n_to_indices(num, length)) == expected
    assert utils.evenly_spaced_values(num, list(range(length))) == expected


def test_n_to_indices_raises():
    with pytest.raises(ValueError):
        utils.n_to_indices(1, 5)

    with pytest.raises(ValueError):
        utils.n_to_indices(10, 5)


def test_make_name_map():
    assert utils.make_name_map(('A', 'b', 'CdEf')) == \
        {'a': 'A', 'b': 'b', 'cdef': 'CdEf'}


def test_make_names_and_lengths():
    assert utils.make_names_and_lengths(('a', 'b'), (1, 2)) == \
        [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

    sample = utils.make_names_and_lengths(('a', 'b'))
    assert sample[0] == ('a', 3)
    assert sample[-1] == ('b', 20)


def test_palette_name():
    assert utils.palette_name('Pants', 8) == 'Pants_8'


def test_split_name_length():
    assert utils.split_name_length('Pants_8') == ('Pants', 8)


def test_print_maps_factory(capsys):
    func = utils.print_maps_factory(
        'sample', [('a', 1), ('a', 2), ('b', 1), ('b', 2)], 'sequential')
    assert inspect.isfunction(func)
    assert 'sample' in inspect.getdoc(func)

    func()
    out, _ = capsys.readouterr()

    assert 'a_1    sequential      1' in out


@pytest.mark.parametrize('reverse', [(True,), (False,)])
def test_get_map_factory(reverse):
    name = 'sample_3'
    expected_name = 'Sample_3'
    colors = [1, 2, 3]
    if reverse:
        expected_name += '_r'
        expected_colors = colors[::-1]
    else:
        expected_colors = colors

    def test_func(name, type_, colors):
        assert name == expected_name
        assert type_ == 'diverging'
        assert colors == expected_colors
        return True

    get_map = utils.get_map_factory(
        'sample desc', 'sample.test', {'Sample': colors}, 'diverging', test_func)

    assert get_map(name, reverse=reverse)

    doc = inspect.getdoc(get_map)
    assert doc.startswith('Get a sample desc palette by name')
    assert 'sample.test' in doc
    assert doc.endswith('function')


def test_load_all_palettes():
    palettes = utils.load_all_palettes(
        mycarta._NAMES_AND_LENGTHS, mycarta.get_map)

    for suffix in ('', '_r'):
        assert ('LinearL_13' + suffix) in palettes
        assert isinstance(palettes['LinearL_13' + suffix], mycarta.MycartaMap)
