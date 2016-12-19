from __future__ import absolute_import, division

import math


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

    # subtract 1 from length to make it equivalent to the last index,
    # subtract 1 from num to make the calculation include the last index
    step = float(length - 1) / float(num - 1)

    return (int(round(step * i)) for i in range(num))


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
