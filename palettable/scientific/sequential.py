"""
Sequential colormaps from Scientific Colour-Maps:
http://www.fabiocrameri.ch/colourmaps.php

"""
from __future__ import absolute_import

from . import scientific
from . import colordata
from .. import utils

_PALETTE_TYPE = 'sequential'
_MAP_NAMES = (
    'Batlow',
    'BatlowW',
    'BatlowK',
    'Glasgow',
    'Lipari',
    'Navia',
    'Hawaii',
    'Buda',
    'Imola',
    'Oslo',
    'GrayC',
    'Nuuk',
    'Devon',
    'LaJolla',
    'Bamako',
    'Davos',
    'Bilbao',
    'LaPaz',
    'Acton',
    'Turku',
    'Tokyo',    # Sequential gradients
    'Oleron',
    'Bukavu',
    'Fes',      # Multi-sequential gradients
    'RomaO',
    'BamO',
    'BrocO',
    'CorkO',
    'VikO',     # Cyclic gradients
)
_NAMES_TO_DATA = {
    name: getattr(colordata, name.upper()) for name in _MAP_NAMES
}
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(_MAP_NAMES)

print_maps = utils.print_maps_factory(
    'sequential scientific', _NAMES_AND_LENGTHS, _PALETTE_TYPE)
get_map = utils.get_map_factory(
    'sequential scientific', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    scientific.ScientificMap, is_evenly_spaced=True)

globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
