Building Palettable Docs
~~~~~~~~~~~~~~~~~~~~~~~~

The Palettable documentation is a mixture of hand curated and generated
content because it contains a large number of palettes and images that
would be painful to list manually.
Files that contain generated content have a suffix ``.md.tpl``,
the ``gendocs.py`` uses Jinja to compile them into Markdown files
that can be turned into HTML by `Urubu <http://thegrovesf.com/>`__.

Palettable sub-modules are mapped to a directory in the docs in the
``MODULES`` dictionary of the ``gendocs.py`` script.
Each of those directories must contain an ``index.md.tpl`` file that
contains Jinja templating for building out a Palettable doc page with
palette preview images.
(See for example `matplotlib/index.md.tpl <./matplotlib/index.md.tpl>`__.)

Building the docs requires
--------------------------

- Palettable
- Matplotlib
- Jinja
- Urubu
- `tservice <https://pypi.python.org/pypi/tservice>`__

Steps to build the docs
-----------------------

1. Generate images and compile ``index.md.tpl`` files

   - ``make images``
   - If all images are up-to-date, then you can compile ``index.md.tpl``
     files only with ``make compile``

2. Have Urubu build HTML

   - Urube configuration lives in ``_site.yml``
   - Run the build with ``make build``

3. Preview the docs with ``make serve``

Adding new Palettable modules
-----------------------------

1. Create a new directory for the module's docs
2. Create an ``index.md.tpl`` file in the new directory and document
   the module therein. Include Jinja templating to create a table-of-contents
   and include preview images.
   (See for example `matplotlib/index.md.tpl <./matplotlib/index.md.tpl>`__.)
3. Update the ``MODULES`` dict in ``gendocs.py`` to map
   the new module to its directory location
4. Build docs as above to preview
