Version 1.2
-----------

* The `print_maps_by_type` and `get_map` functions are now insensitive
  to the case of the `map_type` parameter.
* The `get_map` function is now insensitive to the case of the name parameter.
* Fixed a bug in `get_map` that caused color maps not to get reversed
  when they should have been.
* Added a test suite.

Version 1.1
-----------

* Removed the `number` parameter from `BrewerMap` construction. This attribute
  is now set from the length of the `colors` input.
* Added the `BrewerMap` class to the list of names imported in the brewer2mpl
  namespace. This will make it easier for users to make their own color maps
  by mixing and matching existing ones.
