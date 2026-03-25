---
layout: single
permalink: /scholarly-output/
author_profile: true
redirect_from:
  - /publications/
  - /talks/
---

Publications, theses, and technical reports — organised by type, with links to DOI, arXiv, and PDF where available.

{% include base_path %}

{% if author.googlescholar %}
You can also find my articles on <a href="{{ author.googlescholar }}">my Google Scholar profile</a>.
{% endif %}

## Journal Publications

{% for post in site.publications reversed %}
  {% if post.type == "journal" %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}

---

## Conference Proceedings

{% for post in site.publications reversed %}
  {% if post.type == "conference" %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}

---

## Doctoral Thesis

{% for post in site.publications reversed %}
  {% if post.type == "thesis" %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}

---

## Seminars and Invited Talks

{% for post in site.talks reversed %}
  {% if post.type == "Seminar" %}
    {% include archive-single-talk-cv.html %}
  {% endif %}
{% endfor %}

---

## Conferences

{% if site.talkmap_link == true %}
See a map of all the places I've given a talk.
{% endif %}

{% for post in site.talks reversed %}
  {% if post.type == "Conference" or post.type == "Poster" %}
    {% include archive-single-talk-cv.html %}
  {% endif %}
{% endfor %}

<style>
h2 { margin-top: 1.6rem; margin-bottom: 0.4rem; font-size: 1.1em; }
hr { margin: 0.8rem 0; }
p { margin-bottom: 0.2rem; }
</style>
