---
layout: archive
[//]: # title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}
# Journal Publications
{% for post in site.publications reversed %}
{% if post.type == 'journal' %}
{% include archive-single-cv.html %}
{% endif %}
{% endfor %}

# Conference Proceedings 
{% for post in site.publications reversed %}
{% if post.type == 'conference' %}
{% include archive-single.html %}
{% endif %}
{% endfor %}
# Doctoral Thesis
{% for post in site.publications reversed %}
{% if post.type == 'thesis' %}
{% include archive-single.html %}
{% endif %}
{% endfor %}
