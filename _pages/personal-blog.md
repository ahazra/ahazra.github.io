---
layout: single
title: ""
permalink: /Personal-blog/
author_profile: true
---

<style>
.page__title { display: none; }
h1.blog-heading { font-size: 1.3em; margin-bottom: 0.2rem; margin-top: 0; }
.blog-meta { font-size: 0.82em; color: #9ca3af; margin-bottom: 0.5rem; }
.blog-excerpt { font-size: 0.9em; line-height: 1.6; margin-bottom: 0.3rem; }
.blog-card { border-bottom: 1px solid #374151; padding: 1.4rem 0; }
.blog-card:last-child { border-bottom: none; }
.blog-tag { display: inline-block; font-size: 0.75em; background: #1f2937; color: #9ca3af; border-radius: 3px; padding: 0.1rem 0.45rem; margin-right: 0.3rem; }
.blog-header { margin-bottom: 1.8rem; }
.coming-soon { font-size: 0.82em; color: #6b7280; font-style: italic; margin-top: 0.3rem; }
</style>

<div class="blog-header">
<h2 style="margin-top:0; font-size:1.15em;">Personal Blog</h2>
<p style="font-size:0.9em; color:#9ca3af; margin-bottom:0;">Notes to be written when something insists on being written. In Bengali and English, as the thought arrives.</p>
</div>

---

{% for post in site.posts %}
<div class="blog-card">
<h1 class="blog-heading"><a href="{{ post.url | relative_url }}" style="color:inherit; text-decoration:none;">{{ post.title }}</a></h1>
<div class="blog-meta">{{ post.date | date: "%B %Y" }}
  {% for tag in post.tags %}<span class="blog-tag">{{ tag }}</span>{% endfor %}
</div>
<div class="blog-excerpt">{{ post.excerpt | strip_html }}</div>
</div>
{% endfor %}
