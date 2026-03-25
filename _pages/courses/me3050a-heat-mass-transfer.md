---
layout: single
title: "ME 3050A: Heat and Mass Transfer"
permalink: /courses/me3050a-heat-mass-transfer/
author_profile: true
---

<style>
h2 { margin-top: 1.6rem; margin-bottom: 0.5rem; font-size: 1.05em; }
li { font-size: 0.9em; margin-bottom: 0.3rem; }
p  { font-size: 0.9em; }
.course-meta { font-size: 0.85em; color: #9ca3af; margin-bottom: 1.2rem; }
.no-materials { font-size: 0.88em; color: #6b7280; font-style: italic; }
</style>

<p class="course-meta">Undergraduate · offered 2025</p>

## Course Materials

{% assign data = site.data.courses.me3050a-heat-mass-transfer %}
{% if data.materials and data.materials.size > 0 %}
<ul>
{% for item in data.materials %}
  <li><a href="{{ '/assets/courses/me3050a-heat-mass-transfer/' | append: item.file | relative_url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
{% else %}
<p class="no-materials">No materials posted yet.</p>
{% endif %}
