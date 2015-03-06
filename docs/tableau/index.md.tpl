---
title: 'Tableau Palettes'
layout: page
content: []
---

Palettes taken from [Tableau](http://www.tableau.com/).
All Tableau palettes are qualitative.

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
