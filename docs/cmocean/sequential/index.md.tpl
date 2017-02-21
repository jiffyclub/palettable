---
title: 'cmocean : Sequential'
layout: page
content: []
---

Sequential palettes taken from [cmocean](http://matplotlib.org/cmocean/).

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
