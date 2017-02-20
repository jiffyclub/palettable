from __future__ import absolute_import

from .. import utils
from .mycarta import __doc__, print_maps, get_map, _NAMES_AND_LENGTHS


globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
