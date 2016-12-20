from __future__ import absolute_import, division

import math
import sys


def round_as_py3(value):
    """
    Implement round behaviour consistent with Python 3 for use in Python 2.
    (Such that halves are rounded toward the even side.
    Only for positive numbers.)
    Adapted from https://github.com/python/cpython/blob/6b678aea1ca5c3c3728cd5a7a6eb112b2dad8553/Python/pytime.c#L71

    """
    if math.fmod(value, 1) == 0.5:
        return 2 * round(value / 2)
    else:
        return round(value)

if sys.version_info[0] >= 3:
    round_ = round
else:
    round_ = round_as_py3


def n_to_indices(num, length):
    """
    Calculate `num` evenly spaced indices for a sequence of length `length`.

    Should be used with num >= 2, result will always include first and last.

    Parameters
    ----------
    num : int
    length : int

    Returns
    -------
    list of int

    """
    if num < 2:
        raise ValueError('num must be 2 or larger, got {}'.format(num))
    elif num > length:
        raise ValueError('num cannot be greater than length')

    # subtract 1 from length to make it equivalent to the last index,
    # subtract 1 from num to make the calculation include the last index
    step = (length - 1) / (num - 1)

    return (int(round_(step * i)) for i in range(num))


def evenly_spaced_values(num, data):
    """
    Returns `num` evenly spaced values from sequence `data`.

    Parameters
    ----------
    num : int
    data : sequence

    Returns
    -------
    values : list

    """
    return [data[i] for i in n_to_indices(num, len(data))]
