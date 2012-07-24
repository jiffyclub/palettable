brewer2mpl
==========

brewer2mpl is a pure Python package for accessing
`colorbrewer2.org <http://colorbrewer2.org>`_ color maps from Python.
With brewer2mpl you can get the raw RGB colors of all 165
`colorbrewer2.org <http://colorbrewer2.org>`_ color maps. The color map data
ships with brewer2mpl so no internet connection is required.

For more information and to view some of the color maps see the wiki at
https://github.com/jiffyclub/brewer2mpl/wiki.

Color Maps
----------

colorbrewer2.org has 3 map types: sequential, diverging, and qualitative.
Each color map has between 3 and 12 defined colors.

Examples
--------

Listing Color Maps
~~~~~~~~~~~~~~~~~~

List all of the available color maps::

    brewer2mpl.print_maps()

List maps by type::

    brewer2mpl.print_maps('sequential')

Filter by number of colors defined::

    brewer2mpl.print_maps('qualitative', 6)

Get a Color Map
~~~~~~~~~~~~~~~

Color maps are accessed by name, type, and number::

    bmap = brewer2mpl.get_map('Paired', 'Qualitative', 5)

If you want a color map reversed from how it is given by colorbrewer2.org
set the `reverse` keyword to `True`::

    bmap = brewer2mpl.get_map('Paired', 'Qualitative', 5, reverse=True)

`BrewerMap` Objects
~~~~~~~~~~~~~~~~~~~

Color maps are represented by `BrewerMap` objects. They have a few useful
attributes::

    # colorbrewer2.org url.
    # Copy this into your browser to see the map at colorbrewer2.org.
    bmap.colorbrewer2_url

    # colorbrewer2.org name
    bmap.name

    # number of defined colors
    bmap.number

    # colors as a list of RGB 0-255 triplets
    bmap.colors

    # colors as a list of hex strings
    bmap.hex_colors

    # colors as a list of RGB 0-1 triplets (as used by matplotlib)
    bmap.mpl_colors

    # matplotlib color map
    bmap.mpl_colormap

The matplotlib color maps are created using
`matplotlib.colors.LinearSegmentedColormap.from_list`. If you want to pass
options to that method use the `BrewerMap.get_mpl_colormap` method::

    cmap = bmap.get_mpl_colormap(N=1000, gamma=2.0)
