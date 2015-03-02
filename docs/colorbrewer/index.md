---
title: 'Colorbrewer'
layout: simple_page
content: ['']
---

Colorbrewer palettes are taken from
[http://colorbrewer2.org/](http://colorbrewer2.org/).
They come in three sub-modules grouped by their use:

- [palettable.colorbrewer.diverging][diverging]
- [palettable.colorbrewer.qualitative][qualitative]
- [palettable.colorbrewer.sequential][sequential]

Colorbrewer maps have an additional attribute and method related to viewing
the palettes online.
The `.colorbrewer2_url` attribute is the URL at
[http://colorbrewer2.org/](http://colorbrewer2.org/)
at which to view the palette online,
and the `.colorbrewer2()` method will open your
browser pointed to that URL.
