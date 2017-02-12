from __future__ import absolute_import

import pytest

from .. import utils


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
