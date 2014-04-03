from .wesanderson import __doc__, _palettes, print_maps, get_map
from .wesanderson import WesAndersonMap as _WesAndersonMap


def _load_maps():
    maps = {}

    for k, v in _palettes.items():
        maps[k] = _WesAndersonMap(k, v['type'], v['colors'], v['url'])

    return maps
globals().update(_load_maps())
