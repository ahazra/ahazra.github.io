---
layout: archive
[//]: # title: "Talks and presentations"
permalink: /talks/
author_profile: true
---

{% if site.talkmap_link == true %}

<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>

{% endif %}
# Conferences
{% for post in site.talks reversed %}
{% if post.type == 'Conference' %}
{% include archive-single-talk-cv.html %}
{% endif %}
{% endfor %}

# Posters
{% for post in site.talks reversed %}
{% if post.type == 'Poster' %}
{% include archive-single-talk-cv.html %}
{% endif %}
{% endfor %}

# Colloquium
{% for post in site.talks reversed %}
{% if post.type == 'Seminar' %}
{% include archive-single-talk-cv.html %}
{% endif %}
{% endfor %}
