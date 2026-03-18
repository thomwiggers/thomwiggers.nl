# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
pnpm dev      # Hugo dev server (hugo server --disableFastRender)
pnpm build    # Build site + generate Pagefind search index
hugo          # Build only
```

The Hugo version is pinned in `hugoblox.yaml`. The site is deployed to Cloudflare Pages via `wrangler.toml`.

## Architecture

Hugo static site using the [Hugo Blox](https://hugoblox.com/) academic theme. Content is in `content/`, theme components are vendored in `_vendor/` (Hugo modules). Config lives in `config/_default/` (split across `hugo.yaml`, `params.yaml`, `module.yaml`, `menus.yaml`).

Frontend: Tailwind CSS v4, Preact, Pagefind (client-side search index built post-`hugo --minify`).

## Content Structure

### Events / Talks

`content/events/YYYY-MM-DD-event-name/index.md` — each event in its own directory. Key frontmatter fields:

```yaml
title: "Talk title"
event_url: https://example.com/event/
location: Venue Name
address:
  street: null
  city: City
  region: null
  postcode: null
  country: Country
summary: |
  One-line description.
abstract: null
date: <last-updated date>
authors: [thom]
tags: [relevant, tags]
links:
  - icon: slides
    name: Slides
    url: local-filename.pdf        # or external URL
event_start: 2025-07-22T09:30:00+02:00
event_end: 2025-07-22T11:00:00+02:00
event_all_day: false
event_name: "Conference Name"
slides: ""
projects: []
```

Featured images should be saved as `featured.png` (prefer PNG over JPG). If no featured image exists but a slides PDF is available, generate one from the first slide using `magick -density 150 "name.pdf[0]" featured.png`. Local slides PDFs and papers should be named after the directory (e.g. `2025-07-22-IETF-123-PQUIP.pdf`) — they are picked up automatically and do not need an explicit entry in `links`. Use `links` only for external URLs (e.g. datatracker, paper DOI). Use `icon: custom/ietf` for IETF-related links.

### Publications

`content/publications/` — one directory per paper with `index.md` (similar frontmatter pattern to events).

### Slides

`content/slides/` — Hugo Blox slide decks (rendered with Reveal.js). Uses cascade config to output both HTML and `present` format.
