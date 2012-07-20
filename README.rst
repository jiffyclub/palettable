brewer2mpl
==========

Connect `colorbrewer2.org <http://colorbrewer2.org>`_ color maps to
Python and matplotlib.

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

`BrewerMap` Objects
~~~~~~~~~~~~~~~~~~~

Color maps are represented by `BrewerMap` objects. The have a few useful
attributes::

    # colorbrewer2.org url
    bmap.colorbrewer2_url

    # colorbrewer2.org name
    bmap.name

    # number of defined colors
    bmap.number

    # colors as a list of RGB 0-255 triplets
    bmap.colors

    # colors as a list of RGB 0-1 triplets (as used by matplotlib)
    bmap.mpl_colors
