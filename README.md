# ahazra.github.io

Personal academic website of **Arijit Hazra**, Ramanujan Faculty Fellow in the Department of Mechanical Engineering at IIT Palakkad. Hosted at [ahazra.github.io](https://ahazra.github.io).

The site covers research (computational methods for PDEs, inverse problems, scientific machine learning), scholarly output (publications and talks), teaching, and a personal blog.

## Stack

- [Jekyll](https://jekyllrb.com/) with the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme (dark skin) via `remote_theme`
- Hosted on GitHub Pages

## Local development

```bash
# Serve locally with live reload
bundle exec jekyll serve --livereload

# Build for production
bundle exec jekyll build

# Serve with dev config overrides
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Dependencies are managed via Bundler (`Gemfile`). Run `bundle install` if gems are missing.

## Architecture

### Collections (`_config.yml`)
Two active Jekyll collections, each producing output pages:
- `_publications/` — academic papers. Each file's front matter must include `type:` (`"journal"`, `"conference"`, or `"thesis"`) to appear in the correct section of the Scholarly Output page.
- `_talks/` — talks and presentations. Each file's front matter must include `type:` (`"Conference"`, `"Seminar"`, etc.) to filter correctly.

### Pages (`_pages/`)
| Page | Permalink | Notes |
|------|-----------|-------|
| `about.md` | `/` | Homepage |
| `cv.md` | `/cv/` | Static markdown CV |
| `scholarly-output.md` | `/scholarly-output/` | Auto-renders publications + talks by type; redirects from `/publications/` and `/talks/` |
| `teaching-supervision.md` | `/teaching-supervision/` | Static markdown |

Navigation is defined in `_data/navigation.yml`.

### Custom includes (`_includes/`)
- `archive-single-cv.html` — renders a single publication entry in the CV-style list
- `archive-single-scholarly.html` — renders a publication with DOI/PDF/arXiv links
- `archive-single-talk-cv.html` — renders a single talk entry

### Layouts (`_layouts/`)
- `profile.html` — custom profile layout (extends `default.html`)
- Standard Minimal Mistakes layouts: `single.html`, `archive.html`, `splash.html`, etc.

## Adding content

**New publication** — create `_publications/YYYY-MM-DD-slug.md` with front matter:
```yaml
---
title: "..."
collection: publications
type: "journal"          # journal | conference | thesis
permalink: /publication/YYYY-MM-DD-slug
date: YYYY-MM-DD
venue: "Journal Name"
authors: ["Author One", "Author Two"]
doi: "10.xxxx/..."      # optional
arxiv: "XXXX.XXXXX"     # optional
citation: "..."
---
```

**New talk** — create `_talks/slug.md` with front matter:
```yaml
---
title: "..."
collection: talks
type: "Conference"       # Conference | Seminar | Invited Talk
permalink: /talks/slug
venue: "..."
date: YYYY-MM-DD
location: "City, Country"
---
```

**New news item** — prepend an entry to `_data/news.yml` (newest first):
```yaml
items:
  - date: "YYYY-MM-DD"
    category: paper        # paper | conference | award | general
    text: "One-line description of the update."
    url: "https://..."     # leave "" if no link
```
Badge colours by category: `paper` → blue, `conference` → emerald, `award` → amber, `general` → indigo.
The news box on the homepage is scrollable (150 px max-height); all items in the list are shown.

## Homepage layout

Section order is controlled by `_data/homepage.yml`. Reorder the three lines to change what appears first below the bio:

```yaml
sections:
  - news        # Recent News box (scrollable)
  - research    # Research at a Glance cards
  - positions   # Open Positions box
```

Any permutation of the three values is valid. Changes require a Jekyll rebuild to take effect locally (`bundle exec jekyll serve --livereload` picks them up automatically on save).
