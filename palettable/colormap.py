# coding: utf-8

from __future__ import absolute_import

try:
    from matplotlib.colors import LinearSegmentedColormap
except ImportError:     # pragma: no cover
    HAVE_MPL = False
else:
    HAVE_MPL = True


class ColorMap(object):
    """
    Representation of a color map with matplotlib compatible
    views of the map.

    Parameters
    ----------
    name : str
    map_type : str
    colors : list
        Colors as list of 0-255 RGB triplets.

    Attributes
    ----------
    name : str
    type : str
    number : int
        Number of colors in color map.
    colors : list
        Colors as list of 0-255 RGB triplets.
    hex_colors : list
    mpl_colors : list
    mpl_colormap : matplotlib LinearSegmentedColormap

    """
    def __init__(self, name, map_type, colors):
        self.name = name
        self.type = map_type
        self.number = len(colors)
        self.colors = colors

    @property
    def hex_colors(self):
        """
        Colors as a tuple of hex strings. (e.g. '#A912F4')

        """
        hc = []

        for color in self.colors:
            h = '#' + ''.join('{0:>02}'.format(hex(c)[2:].upper())
                              for c in color)
            hc.append(h)

        return hc

    @property
    def mpl_colors(self):
        """
        Colors expressed on the range 0-1 as used by matplotlib.

        """
        mc = []

        for color in self.colors:
            mc.append(tuple([x / 255. for x in color]))

        return mc

    @property
    def mpl_colormap(self):
        """
        A basic matplotlib color map. If you want to specify keyword arguments
        use the `get_mpl_colormap` method.

        """
        return self.get_mpl_colormap()

    def get_mpl_colormap(self, **kwargs):
        """
        A color map that can be used in matplotlib plots. Requires matplotlib
        to be importable. Keyword arguments are passed to
        `matplotlib.colors.LinearSegmentedColormap.from_list`.

        """
        if not HAVE_MPL:    # pragma: no cover
            raise RuntimeError('matplotlib not available.')

        cmap = LinearSegmentedColormap.from_list(self.name,
                                                 self.mpl_colors, **kwargs)

        return cmap

    def show_as_blocks(self, block_size=100):
        """
        Show colors in the IPython Notebook using ipythonblocks.

        Parameters
        ----------
        block_size : int, optional
            Size of displayed blocks.

        """
        from ipythonblocks import BlockGrid

        grid = BlockGrid(self.number, 1, block_size=block_size)

        for block, color in zip(grid, self.colors):
            block.rgb = color

        grid.show()
