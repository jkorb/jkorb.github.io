# Development

## How the site works

Hugo reads `hugo.toml`, language-specific Markdown in `content/`, shared records
in `data/`, and interface translations in `i18n/`. The templates in `layouts/`
produce static HTML. Hugo concatenates, minifies, and fingerprints the main and
language CSS. It fingerprints the portrait and inlines the small local SVG icon
set. `static/` is copied unchanged; the legal notices retain their original text.

The homepage is `layouts/home.html`, built on `_default/baseof.html`. The base
provides metadata, a skip link, language navigation, and the footer. Project
pages use `layouts/projects/lean.html`; ordinary pages use `_default/single.html`
and section indexes use `_default/list.html`. The slide iframe template owns its
whole HTML document and shares the language and home-control partials.

Homepage projects come from `data/projects.yaml`. The `project-visible` partial
checks whether an internal page is published in the current language. Its URL
is then obtained from that page's `RelPermalink`. Slides are discovered from the
current language's published slide pages. The draft projects index does not
prevent its published child project from being built.

## Preview and build

Use Hugo 0.164.0, matching the deployment pin. Hugo Extended is also supported.
Python 3 and curl are needed for checks and CV downloads; there are no package
installation steps.

```sh
hugo server -D -F
```

Use the URL printed by Hugo. `-D` shows drafts and `-F` shows future-dated pages.
Omit both to preview publication rules. English is `/`, followed by `/de/`,
`/nl/`, and `/it/`. Stop the preview with Ctrl-C.

```sh
hugo --minify --gc --cleanDestinationDir --printI18nWarnings --panicOnWarning
python3 scripts/check-site.py
python3 scripts/test-fetch-cvs.py
python3 scripts/fetch-cvs.py
python3 scripts/check-site.py --require-cvs
```

The first check is offline and allows CVs to be absent. The fetch requires
network access and adds all four PDFs to `public/`. Run it after Hugo: a clean
build removes downloaded files. A Hugo preview does not automatically fetch CVs.
To preview them, run the fetch after starting the server; a subsequent clean
build may require fetching again.

If Hugo cannot write its default cache, pass
`--cacheDir /tmp/jkorbmacher-hugo-cache` to the Hugo commands. `public/`, generated
resources, and the build lock are ignored by Git.

## Checks

`test-fetch-cvs.py` checks successful installation and ensures HTML responses,
truncated PDFs, and download failures leave existing CVs intact. It runs offline.

`check-site.py` checks all 16 published HTML pages: language tags, reciprocal
language switches, canonical and alternate URLs, localized CV links, local
assets and links, fragment targets, project names, milestone count, slide title,
home-return links, and absence of draft section indexes. `--require-cvs` also
checks the downloaded PDF signatures and end markers. It does not check the
availability of every third-party website or replace a visual review.

To check the original project embargo across all languages:

```sh
hugo --destination /tmp/jkorbmacher-embargo --clock 2026-08-31T12:00:00Z --cleanDestinationDir --printI18nWarnings --panicOnWarning
python3 scripts/check-site.py /tmp/jkorbmacher-embargo --embargoed
```

When adding or retiring public pages, update the route expectations in
`scripts/check-site.py`. When changing publication dates, update the embargo
fixture as well.

For layout changes, inspect all languages at desktop and 320–375 px widths.
Tab through the skip link and language control, follow a translated project
link, switch language on that project, and return home. Check the full-screen
slide viewer separately. Names should wrap without horizontal scrolling.
