# coding: utf-8

from __future__ import absolute_import

import sys

try:
    import matplotlib.pyplot as plt
    from matplotlib.colors import (
        ListedColormap, BoundaryNorm, Normalize, LinearSegmentedColormap)
    from matplotlib.colorbar import ColorbarBase
except ImportError:     # pragma: no cover
    HAVE_MPL = False
else:
    HAVE_MPL = True


class Palette(object):
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

    def _write_image(self, fp, style, format='png', size=(6, 1)):
        """
        Write the color map as an image to a file-like object.

        Parameters
        ----------
        fp : file-like
            A file-like object such as an open file pointer or
            a StringIO/BytesIO instance.
        style : {'discrete', 'continuous'}
            Whether to make the color map image as a discrete map
            or a continuous map.
        format : str, optional
            An image format that will be understood by matplotlib.
        size : tuple of int, optional
            (width, height) of image to make in units of inches.

        """
        if not HAVE_MPL:    # pragma: no cover
            raise RuntimeError('matplotlib not available.')

        fig = plt.figure(figsize=size, frameon=False)
        ax = fig.add_axes([0, 0, 1, 1], frameon=False)
        ax.set_axis_off()

        if style == 'discrete':
            # make a bounded color map showing only the defined colors
            ncolors = self.number
            norm = BoundaryNorm(range(ncolors + 1), ncolors=ncolors)
            cmap = ListedColormap(self.mpl_colors)

        elif style == 'continuous':
            # make the smooth, interpolated color map
            cmap = self.mpl_colormap
            norm = Normalize(vmin=0, vmax=1)

        ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal')
        fig.savefig(fp, format=format)
        plt.close(fig)

    def show_discrete_image(self, size=(6, 1)):
        """
        Embed an image of this discrete color map in the IPython Notebook.

        Parameters
        ----------
        size : tuple of int, optional
            (width, height) of image to make in units of inches.

        """
        if sys.version_info[0] == 2:
            from StringIO import StringIO as BytesIO
        elif sys.version_info[0] == 3:
            from io import BytesIO

        from IPython.display import display
        from IPython.display import Image as ipyImage

        im = BytesIO()
        self._write_image(im, 'discrete', format='png', size=size)
        display(ipyImage(data=im.getvalue(), format='png'))

    def save_discrete_image(self, filename, size=(6, 1), format=None):
        """
        Save an image of this discrete color map to a file.

        Parameters
        ----------
        filename : str
            If `format` is None the format will be inferred from the
            `filename` extension.
        size : tuple of int, optional
            (width, height) of image to make in units of inches.
        format : str, optional
            An image format that will be understood by matplotlib.

        """
        with open(filename, 'wb') as f:
            self._write_image(
                f, 'discrete', format=filename.split('.')[-1], size=size)

    def show_continuous_image(self, size=(6, 1)):
        """
        Embed an image of this continuous color map in the IPython Notebook.

        Parameters
        ----------
        size : tuple of int, optional
            (width, height) of image to make in units of inches.

        """
        if sys.version_info[0] == 2:
            from StringIO import StringIO as BytesIO
        elif sys.version_info[0] == 3:
            from io import BytesIO

        from IPython.display import display
        from IPython.display import Image as ipyImage

        im = BytesIO()
        self._write_image(im, 'continuous', format='png', size=size)
        display(ipyImage(data=im.getvalue(), format='png'))

    def save_continuous_image(self, filename, size=(6, 1), format=None):
        """
        Save an image of this continuous color map to a file.

        Parameters
        ----------
        filename : str
            If `format` is None the format will be inferred from the
            `filename` extension.
        size : tuple of int, optional
            (width, height) of image to make in units of inches.
        format : str, optional
            An image format that will be understood by matplotlib.

        """
        with open(filename, 'wb') as f:
            self._write_image(
                f, 'continuous', format=filename.split('.')[-1], size=size)
