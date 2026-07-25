# Adding and hosting slides

## How the homepage list works

The homepage automatically lists published pages from `content/slides/` under
“Slides”. There is no separate YAML list to keep synchronized.

Each slide entry supports these front-matter fields:

```yaml
title: "Presentation title"
description: "A short description for page metadata."
layout: "embed"
embed_url: "https://example.org/presentation"
weight: 10
listed: true
draft: false
```

- `title` is the link text shown on the homepage.
- `layout` selects the page design.
- `embed_url` is used by the reusable iframe layout.
- `weight` controls the list order; lower numbers appear first.
- `listed: false` keeps a published page off the homepage.
- `draft: true` omits both the page and its homepage link from production.

“No Variables (Gap.12, September 2025)” is configured in
`content/slides/excalidraw-presentation.md`. Change its `title` to rename the
homepage link or change `embed_url` to display a different Excalidraw page.

## Adding another embedded presentation

Create a draft from the slide archetype:

```sh
hugo new content --kind slides slides/presentation-name.md
```

Edit the generated file, replace `embed_url`, and preview it with:

```sh
hugo server -D -F
```

When it is ready, set `draft: false`. The link then appears automatically on
the homepage.

The iframe page includes a small clickable favicon in the upper-left corner
that returns to `jkorbmacher.org`. Its template is
`layouts/slides/embed.html`.

Not every external website permits embedding. A provider can block iframes
with its security headers. If that happens, use an ordinary external link or a
locally hosted slide framework instead.

## Linking directly to externally hosted slides

To make a homepage item open an external slide URL rather than an internal
page, add `external_url`:

```yaml
title: "Presentation title"
external_url: "https://slides.example.org/talk/"
weight: 20
listed: true
draft: false
```

External slide links open in a new tab.

## Using Reveal.js or another framework

Slide pages are intentionally layout-agnostic. For a custom presentation:

1. Create `content/slides/presentation-name.md`.
2. Set a distinct layout name, such as `layout: "reveal"`.
3. Create `layouts/slides/reveal.html`.
4. Put that presentation’s scripts, styles, and media under a dedicated
   directory such as `static/slides/presentation-name/`, or process them
   through Hugo’s `assets/` pipeline.

A slide layout can be a complete standalone HTML document and does not have to
inherit the website’s normal header, footer, typography, or stylesheet.

For framework code that is maintained as a separate repository, a Git
submodule can be appropriate. For a small presentation, committing the source
directly is usually simpler. Avoid loading framework code from a public CDN if
you want deployments to remain self-contained and reproducible.
