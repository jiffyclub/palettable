Version 3.2.0
-------------

* Light & Bartlein palettes (thanks @dcherian in #30!)
* Drop official support for Python 2.6 and 3.3

Version 3.1.0
-------------

* CartoColors palettes (thanks @andy-esch in #21!)

Version 3.0.0
-------------

* Added new Wes Anderson palettes
* Changed WesAndersonMap.wap_url attribute to .url to match the rest
  of the API
* Added modules for cmocean, matplotlib, and mycarta palettes

Version 2.1
-----------

* Add cubehelix palettes (thanks @jonathansick and @jradavenport!)
* Add two new Wes Anderson palettes

Version 2.0
-----------

* Change name of library to Palettable
* Add Tableau palettes
* Additional Wes Anderson palettes
* Pre-make all palettes so they are available at import time
* Change naming scheme to <name>_<number of colors>

Version 1.4
-----------

* Fix colorbrewer2 URLs, thanks @mbforbes!
* Add ``.show_as_blocks()`` method for displaying color maps
  in an IPython Notebook using `ipythonblocks <http://ipythonblocks.org>`_.
* Add ``brewer2mpl.wesanderson`` module with color maps from
  `Wes Anderson Palettes <http://wesandersonpalettes.tumblr.com/>`_

Version 1.3.2
-------------

* Fixes for Python 3, thanks @astrofrog!

Version 1.3.1
-------------

* Bugfix release for a Python 2.6 incompatible format string.

Version 1.3
-----------

* Add a ``colorbrewer2`` method to ``BrewerMap`` objects that launches
  colorbrewer2.org in the user's browser.
* Added ``sequential``, ``diverging``, and ``qualitative`` modules to provide
  direct access to ``BrewerMap`` objects.

Version 1.2
-----------

* The ``print_maps_by_type`` and ``get_map`` functions are now insensitive
  to the case of the ``map_type`` parameter.
* The ``get_map`` function is now insensitive to the case of the name parameter.
* Fixed a bug in ``get_map`` that caused color maps not to get reversed
  when they should have been.
* Added a test suite.

Version 1.1
-----------

* Removed the ``number`` parameter from ``BrewerMap`` construction. This attribute
  is now set from the length of the ``colors`` input.
* Added the ``BrewerMap`` class to the list of names imported in the brewer2mpl
  namespace. This will make it easier for users to make their own color maps
  by mixing and matching existing ones.
