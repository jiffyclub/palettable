import pytest

from .. import utils


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
