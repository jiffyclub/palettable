from __future__ import absolute_import

from ... import wesanderson as wap


def test_print_maps(capsys):
    wap.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'Aquatic1          qualitative     5'


def test_get_map():
    palette = wap.get_map('cavalcanTi')
    assert isinstance(palette, wap.wesanderson.WesAndersonMap)
    assert palette.name == 'Cavalcanti'
    assert palette.type == 'qualitative'
    assert len(palette.colors) == 5
    assert palette.url == \
        ('http://wesandersonpalettes.tumblr.com/post/'
         '79348553036/castello-cavalcanti-how-can-i-help')


def test_get_map_reversed():
    palette = wap.get_map('cavalcanTi', reverse=True)
    assert isinstance(palette, wap.wesanderson.WesAndersonMap)
    assert palette.name == 'Cavalcanti_r'
    assert palette.type == 'qualitative'
    assert len(palette.colors) == 5
    assert palette.url == \
        ('http://wesandersonpalettes.tumblr.com/post/'
         '79348553036/castello-cavalcanti-how-can-i-help')


def test_palettes_loaded():
    assert isinstance(wap.Cavalcanti_5, wap.wesanderson.WesAndersonMap)
    assert isinstance(wap.Cavalcanti_5_r, wap.wesanderson.WesAndersonMap)
    assert wap.Cavalcanti_5.type == 'qualitative'


def test_get_all_maps():
    # Smoke tests.
    wap._get_all_maps()
