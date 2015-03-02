---
title: 'Colorbrewer : Diverging'
layout: page
content: ['']
---

# Contents

{% for p in palettes %}
- [{{p}}](#{{p | lower}})
{%- endfor %}

# Previews

{% for p in palettes %}
<section id="{{p | lower}}">
    <p class="h4">{{p}}</p>

    <img class="img-responsive" src="./img/{{p + '_continuous.png'}}" alt="{{p + ' continuous'}}">
    <br>
    <img class="img-responsive" src="./img/{{p + '_discrete.png'}}" alt="{{p + ' discrete'}}">

</section>
{% endfor %}
