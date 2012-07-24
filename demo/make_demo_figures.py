"""
Make color map figures for the web page.

Three figures are made, one each for the sequential, diverging, and qualitative
color maps. For each named color map the one with the most defined colors
is shown.

"""

import math

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.colorbar import ColorbarBase
from mpl_toolkits.axes_grid1 import ImageGrid

import brewer2mpl


# for each named color map, get the one with the most colors
def filter_maps():
    all_maps = brewer2mpl.COLOR_MAPS

    max_maps = {}

    for map_type in all_maps:
        max_maps[map_type] = {}

        for map_name in all_maps[map_type]:
            max_num = max(all_maps[map_type][map_name].iterkeys(), key=int)
            max_maps[map_type][map_name] = \
                brewer2mpl.get_map(map_name, map_type, int(max_num))

    return max_maps


# show the color maps on axes ala
# http://matplotlib.sourceforge.net/examples/api/colorbar_only.html
def make_figure(map_type, bmaps):
    fig = plt.figure(figsize=(8, 2 * len(bmaps)))
    fig.suptitle(map_type,
                 x=0.5, y=0.98,                     # top middle
                 verticalalignment='top',
                 horizontalalignment='center',
                 fontsize=20)

    grid = ImageGrid(fig, (0.15, 0.01, 0.82, 0.94),
                     nrows_ncols=(2 * len(bmaps), 1),
                     aspect=False, axes_pad=0.1)

    map_names = sorted(bmaps.keys())

    for i, ax in enumerate(grid):
        map_name = map_names[int(math.floor(i / 2.))]
        ax.set_axis_off()

        if i % 2 == 0:
            # make the smooth, interpolated color map
            ColorbarBase(ax, cmap=bmaps[map_name].mpl_colormap,
                         orientation='horizontal')
            ax.set_title(map_name,
                         position=(-0.01,0.5),          # on the left side
                         size=15,
                         verticalalignment='center',
                         horizontalalignment='right')
        else:
            # make a bounded color map showing only the defined colors
            ncolors = bmaps[map_name].number
            norm = BoundaryNorm(range(ncolors + 1), ncolors=ncolors)
            cmap = ListedColormap(bmaps[map_name].mpl_colors)
            ColorbarBase(ax, cmap=cmap, norm=norm, orientation='horizontal')

    fig.savefig(map_type + '.png')


def main():
    bmaps = filter_maps()

    for map_type in brewer2mpl.MAP_TYPES:
        make_figure(map_type, bmaps[map_type])


if __name__ == '__main__':
    main()
