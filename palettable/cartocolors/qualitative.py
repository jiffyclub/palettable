from __future__ import absolute_import

from .cartocolors import _load_maps_by_type

globals().update(_load_maps_by_type('qualitative'))
