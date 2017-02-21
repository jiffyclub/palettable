---
title: 'Matplotlib Palettes'
layout: page
content: []
---

Palettes taken from the [new perceptual colormaps](https://bids.github.io/colormap)
added to Matplotlib in version 1.5.
All are sequential.

# Contents

{% for p in palettes %}
- [{{p}}](#{{p | lower}})
{%- endfor %}

# Previews

{% for p in palettes %}
<section id="{{p | lower}}">
    <p class="h4">{{p}}</p>

    <div><img src="./img/{{p + '_continuous.png'}}" alt="{{p + ' continuous'}}"></div>
    <br>
    <img src="./img/{{p + '_discrete.png'}}" alt="{{p + ' discrete'}}">

</section>
{% endfor %}
