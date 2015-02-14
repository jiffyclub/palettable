from ... import wesanderson as wap


def test_print_maps(capsys):
    wap.print_maps()
    out, err = capsys.readouterr()
    lines = out.split('\n')
    assert lines[0] == 'Cavalcanti        Qualitative     5'


def test_get_map():
    palette = wap.get_map('cavalcanTi')
    assert isinstance(palette, wap.wesanderson.WesAndersonMap)
    assert palette.name == 'Cavalcanti'
    assert len(palette.colors) == 5
    assert palette.wap_url == \
        ('http://wesandersonpalettes.tumblr.com/post/'
         '79348553036/castello-cavalcanti-how-can-i-help')


def test_get_map_reversed():
    palette = wap.get_map('cavalcanTi', reverse=True)
    assert isinstance(palette, wap.wesanderson.WesAndersonMap)
    assert palette.name == 'Cavalcanti_r'
    assert len(palette.colors) == 5
    assert palette.wap_url == \
        ('http://wesandersonpalettes.tumblr.com/post/'
         '79348553036/castello-cavalcanti-how-can-i-help')


def test_palettes_loaded():
    assert isinstance(wap.Cavalcanti, wap.wesanderson.WesAndersonMap)
    assert isinstance(wap.Cavalcanti_r, wap.wesanderson.WesAndersonMap)


def test_get_all_maps():
    # Smoke tests.
    wap._get_all_maps()
