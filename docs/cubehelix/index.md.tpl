---
title: 'Cubehelix Palettes'
layout: page
content: []
---

Cubehelix was designed by [D.A. Green](http://adsabs.harvard.edu/abs/2011arXiv1108.5083G) to provide a color mapping that would degrade gracefully to grayscale without losing information.
This quality makes Cubehelix useful for continuous color scales in scientific visualizations that might be printed in grayscale at some point.

The `palettable.cubehelix` module provides several pre-made Cubehelix palettes, or you can [make your own](#make).

### See Also

- *[A colour scheme for the display of astronomical intensity images](http://adsabs.harvard.edu/abs/2011BASI...39..289G)*, D.A. Green (2011) Bulletin of the Astronomical Society of India, 39, 289
- *[Cubehelix, or How I Learned to Love Black & White Printers](http://www.ifweassume.com/2013/05/cubehelix-or-how-i-learned-to-love.html)* by James Davenport.

# Contents

- Previews
{% for p in palettes %}
    * [{{p}}](#{{p | lower}})
{%- endfor %}

- [Making your own Cubehelix palette](#make)

# Previews

{% for p in palettes %}
<section id="{{p | lower}}">
    <p class="h4">{{p}}</p>

    <div><img src="./img/{{p + '_continuous.png'}}" alt="{{p + ' continuous'}}"></div>
    <br>
    <div><img src="./img/{{p + '_discrete.png'}}" alt="{{p + ' discrete'}}"></div>

</section>
{% endfor %}


<a id="make"></a>
# Making your own Cubehelix palette

With the `Cubehelix.make` classmethod you can create arbitrary Cubehelix palettes.
For example:

    from palettable.cubehelix import Cubehelix
    palette = Cubehelix.make(start=0.3, rotation=-0.5, n=16)

and then use that `palette` instance as usual.


## `Cubehelix.make` Argument Reference

- `start` (scalar, optional).
    Sets the starting position in the RGB color space. 0=blue, 1=red,
    2=green. Default is `0.5` (purple).
- `rotation` (scalar, optional).
    The number of rotations through the rainbow. Can be positive
    or negative, indicating direction of rainbow. Negative values
    correspond to Blue&rarr;Red direction. Default is `-1.5`.
- `start_hue` (scalar, optional).
    Sets the starting color, ranging from (-360, 360). Combined with
    `end_hue`, this parameter overrides `start` and `rotation`.
    This parameter is based on the D3 implementation by @mbostock.
    Default is `None`.
- `end_hue` (scalar, optional)
    Sets the ending color, ranging from (-360, 360). Combined with
    `start_hue`, this parameter overrides ``start`` and ``rotation``.
    This parameter is based on the D3 implementation by @mbostock.
    Default is ``None``.
- `gamma` (scalar, optional).
    The gamma correction for intensity. Values of `gamma < 1`
    emphasize low intensities while `gamma > 1` emphasises high
    intensities. Default is `1.0`.
- `sat` (scalar, optional).
    The uniform saturation intensity factor. `sat=0` produces
    grayscale, while `sat=1` retains the full saturation. Setting
    `sat>1` oversaturates the color map, at the risk of clipping
    the color scale. Note that `sat` overrides both `min_stat`
    and `max_sat` if set.
- `min_sat` (scalar, optional).
    Saturation at the minimum level. Default is `1.2`.
- `max_sat` (scalar, optional).
    Satuation at the maximum level. Default is `1.2`.
- `min_light` (scalar, optional).
    Minimum lightness value. Default is `0`.
- `max_light` (scalar, optional).
    Maximum lightness value. Default is `1`.
- `n` (scalar, optional).
    Number of discrete rendered colors. Default is `256`.
- `reverse` (bool, optional).
    Set to `True` to reverse the color map. Will go from black to
    white. Good for density plots where shade &rarr; density.
    Default is `False`.
- `name` (str, optional).
    Name of the color map (defaults to `'custom_cubehelix'`).
