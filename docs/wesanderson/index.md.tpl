---
title: 'Wes Anderson Palettes'
layout: page
content: []
---

These are taken from the
[Wes Anderson Palettes](http://wesandersonpalettes.tumblr.com/) blog.
All Wes Anderson palletes are qualitative.

# Contents

{% for p in palettes %}
- [{{p}}](#{{p | lower}})
{%- endfor %}

# Previews

{% for p in palettes %}
<section id="{{p | lower}}">
    <p class="h4">{{p}}</p>

    <img src="./img/{{p + '_discrete.png'}}" alt="{{p + ' discrete'}}">

</section>
{% endfor %}
