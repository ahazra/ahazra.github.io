---
layout: single
permalink: /scholarly-output/
author_profile: true
redirect_from:
  - /publications/
  - /talks/
---

<style>
h2 { margin-top: 1.8rem; margin-bottom: 0.5rem; font-size: 1.05em; }
hr { margin: 0.6rem 0 1rem; border-color: #2d3f55; }
</style>

Publications, theses, and technical reports — organised by type, with links to DOI, arXiv, and PDF where available.

{% if site.author.googlescholar %}
Also on <a href="{{ site.author.googlescholar }}">Google Scholar</a>.
{% endif %}

## Journal Publications

{% bibliography --file publications --query @article --sort_by date --order descending %}

---

## Conference Proceedings

{% bibliography --file publications --query @inproceedings --sort_by date --order descending %}

---

## Doctoral Thesis

{% bibliography --file publications --query @thesis --sort_by date --order descending %}

---

## Seminars and Invited Talks

{% bibliography --file talks --query @unpublished[keywords~=Seminar] --template talk-entry --sort_by date --order descending %}

---

## Conference Talks

{% bibliography --file talks --query @unpublished[keywords~=Conference] --template talk-entry --sort_by date --order descending %}
