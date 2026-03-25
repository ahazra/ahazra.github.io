# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Jekyll-based personal academic website for Arijit Hazra (Ramanujan Faculty Fellow, IIT Palakkad), hosted at `ahazra.github.io`. Built on the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) theme (dark skin) via `remote_theme`.

## Commands

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
