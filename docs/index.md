---
title: Palettable
layout: home
content: []
tagline:
    Color palettes for Python
---

Palettable (formerly brewer2mpl) is a library of color palettes for Python.
It's written in pure Python with no dependencies,
but it can supply color maps for [matplotlib](http://matplotlib.org/).
You can use Palettable to customize matplotlib plots or
supply colors for a web application.

Palettable has color palettes from:

- [CartoColors][cartocolors]
- [cmocean][cmocean]
- [Colorbrewer2][colorbrewer]
- [Cubehelix][cubehelix]
- [Light & Bartlein][lightbartlein]
- [matplotlib][matplotlib]
- [MyCarta][mycarta]
- [Plotly][plotly]
- [Scientific][scientific]
- [Tableau][tableau]
- The [Wes Anderson Palettes][wesanderson] blog

# Documentation

## Installation

Palettable is available on PyPI for installation via pip:
`pip install palettable`.
Palettable is compatible with Python 2.6, 2.7, and Python 3.

## Finding Palettes

Palettes are pre-built and loaded at import time.
They have a naming convention of `<Name>_<number of colors>`.
For example, the Colorbrewer2 palette Dark2 with seven colors is
named `Dark2_7`.
Every palette also has a reversed version with the same name plus
the suffix `_r` (e.g. `Dark2_7_r`).

The modules with palettes are:

- [`palettable.cartocolors.diverging`][cartocolors/diverging]
- [`palettable.cartocolors.qualitative`][cartocolors/qualitative]
- [`palettable.cartocolors.sequential`][cartocolors/sequential]
- [`palettable.cmocean.diverging`][cmocean/diverging]
- [`palettable.cmocean.sequential`][cmocean/sequential]
- [`palettable.colorbrewer.diverging`][colorbrewer/diverging]
- [`palettable.colorbrewer.qualitative`][colorbrewer/qualitative]
- [`palettable.colorbrewer.sequential`][colorbrewer/sequential]
- [`palettable.lightbartlein.diverging`][lightbartlein/diverging]
- [`palettable.lightbartlein.sequential`][lightbartlein/sequential]
- [`palettable.matplotlib`][matplotlib]
- [`palettable.mycarta`][mycarta]
- [`palettable.plotly.diverging`][plotly/diverging]
- [`palettable.plotly.qualitative`][plotly/qualitative]
- [`palettable.plotly.sequential`][plotly/sequential]
- [`palettable.scientific.diverging`][scientific/diverging]
- [`palettable.scientific.sequential`][scientific/sequential]
- [`palettable.tableau`][tableau]
- [`palettable.wesanderson`][wesanderson]

The `Dark2_7` palette could be imported via:

```python
from palettable.colorbrewer.qualitative import Dark2_7
```

## Palette Interface

All the palette instances have a common interface including these attributes:

`name`
:   The name of the palette.

`type`
:   One of `'diverging'`, `'qualitative'`, or `'sequential`'.

`number`
:   The number of defined colors in the palette.

`colors`
:   The defined colors in the palette as a list of RGB tuples
    in the range 0-255.

`hex_colors`
:   Colors as a list of hex strings (e.g. '#A912F4').

`mpl_colors`
:   Colors as a list of RGB tuples in the range 0-1 as used by matplotlib.

`mpl_colormap`
:   A continuous, interpolated matplotlib
    [`LinearSegmentedColormap`](http://matplotlib.org/api/colors_api.html#matplotlib.colors.LinearSegmentedColormap).

Palettes also have these methods:

`get_mpl_colormap`
:   Use this method to get a matplotlib color map and pass custom keyword
    arguments to
    [`LinearSegmentedColormap.from_list`](http://matplotlib.org/api/colors_api.html#matplotlib.colors.LinearSegmentedColormap.from_list).

`show_as_blocks`
:   Show the defined colors of the palette in the IPython Notebook.
    Requires [ipythonblocks][] to be installed.

`show_discrete_image`
:   Show the defined colors of the palette in the IPython Notebook.
    Requires [matplotlib][] to be installed.

`show_continuous_image`
:   Show the continuous, interpolated palette in the IPython Notebook.
    Requires [matplotlib][] to be installed.

`save_discrete_image`
:   Save an image of the defined colors of palette to a file.
    Requires [matplotlib][] to be installed.

`save_continuous_image`
:   Save an image of the continuous, interpolated palette to a file.
    Requires [matplotlib][] to be installed.

## Cookbook

### matplotlib Color Cycle

matplotlib follows a default color cycle when drawing a plot.
This can be modified as described
[in this example](http://matplotlib.org/examples/color/color_cycle_demo.html).
To substitute a Palettable palette use the `.mpl_colors` attribute:

```python
ax.set_prop_cycle('color', palettable.colorbrewer.qualitative.Dark2_8.mpl_colors)
```

### matplotlib Colormap

Many matplotlib functions and methods take a `cmap` argument.
You can use the `.mpl_colormap` attribute with this:

```python
from palettable.colorbrewer.sequential import Blues_8
ax.imshow(data, cmap=Blues_8.mpl_colormap)
```

Note that the colorbrewer2 color palettes are all available in [matplotlib][]
already.
See the full list of available color maps in matplotlib here:
[http://matplotlib.org/examples/color/colormaps_reference.html](http://matplotlib.org/examples/color/colormaps_reference.html).

### matplotlib Discrete Colormap

The `.mpl_colormap` attribute is a continuous, interpolated map.
If you want to make discrete color map you can use matplotlib's
[`ListedColormap`](http://matplotlib.org/api/colors_api.html#matplotlib.colors.ListedColormap):

```python
cmap = ListedColormap(palettable.colorbrewer.qualitative.Dark2_7.mpl_colors)
```

# Contact

Palettable is on GitHub at
[https://github.com/jiffyclub/palettable](https://github.com/jiffyclub/palettable).
Please report issues there.
