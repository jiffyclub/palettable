"""
Qualitative colormaps from Scientific Colour-Maps:
http://www.fabiocrameri.ch/colourmaps.php

"""
from __future__ import absolute_import

from . import scientific
from . import colordata_qualitative
from .. import utils

_PALETTE_TYPE = 'qualitative'
_NAMES_TO_DATA = {
    'Acton': colordata_qualitative.ACTON,
    'Bamako': colordata_qualitative.BAMAKO,
    'Batlow': colordata_qualitative.BATLOW,
    'BatlowK': colordata_qualitative.BATLOWK,
    'BatlowW': colordata_qualitative.BATLOWW,
    'Bilbao': colordata_qualitative.BILBAO,
    'Buda': colordata_qualitative.BUDA,
    'Davos': colordata_qualitative.DAVOS,
    'Devon': colordata_qualitative.DEVON,
    'Glasgow': colordata_qualitative.GLASGOW,
    'GrayC': colordata_qualitative.GRAYC,
    'Hawaii': colordata_qualitative.HAWAII,
    'Imola': colordata_qualitative.IMOLA,
    'Lajolla': colordata_qualitative.LAJOLLA,
    'Lapaz': colordata_qualitative.LAPAZ,
    'Lipari': colordata_qualitative.LIPARI,
    'Navia': colordata_qualitative.NAVIA,
    'Nuuk': colordata_qualitative.NUUK,
    'Oslo': colordata_qualitative.OSLO,
    'Tokyo': colordata_qualitative.TOKYO,
    'Turku': colordata_qualitative.TURKU,
}
_NAME_MAP = utils.make_name_map(_NAMES_TO_DATA.keys())
_NAMES_AND_LENGTHS = utils.make_names_and_lengths(
    sorted(_NAMES_TO_DATA.keys()), range(2, 11)
)

print_maps = utils.print_maps_factory(
    'qualitative scientific', _NAMES_AND_LENGTHS, _PALETTE_TYPE)

get_map = utils.get_map_factory(
    'qualitative scientific', __name__, _NAMES_TO_DATA, _PALETTE_TYPE,
    scientific.ScientificMap, is_evenly_spaced=False)

globals().update(utils.load_all_palettes(_NAMES_AND_LENGTHS, get_map))
