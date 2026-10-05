# Working on jkorbmacher.org

This directory is the live website source. Start with [doc/README.md](doc/README.md)
and [doc/design.md](doc/design.md). The parent workspace contains historical
material; do not copy it into the site.

- Hugo with custom templates, plain CSS, Markdown, and small data files. No theme,
  runtime JavaScript, package manager, remote fonts, or icon CDN. Fonts are
  self-hosted in `static/fonts/` with their licenses.
- US English is the default at `/`; German, Dutch, and Italian use `/de/`, `/nl/`,
  and `/it/`. English Markdown has no language suffix; translations have `.de`,
  `.nl`, or `.it` before `.md`. Shared interface text is in `i18n/*.yaml`.
- Translate prose, metadata, image descriptions, and accessibility labels. Keep
  publication/project titles, official names, people, URLs, and identifiers intact.
  Update all translations when changing a factual claim or publication setting.
- Preserve the minimalist README-like appearance: Open Sans body text, Merriweather headings,
  white background,
  dark text, blue links, grayscale portrait, and plain headings. Keep the
  compact language links usable by keyboard and without JavaScript.
- `data/cv.json` is the single source for public CV paths and Dropbox URLs. The
  `cv` shortcode links the current language's PDF. PDFs belong only in build
  output; never commit them. Preserve `/cv_jkorbmacher.pdf` for English.
- Internal project links must resolve through the current Hugo site. Hide links
  to unpublished pages. Keep `draft` and `publishDate` consistent across languages;
  never add `-D` or `-F` to the production workflow.
- The slide viewer has its own full HTML layout. Changes to global language
  metadata/navigation must account for it as well as `baseof.html`.
- GitHub Actions builds PRs; pushes to `main` deploy automatically. Do not push
  merely to preview a change. Generated `public/` and `resources/_gen/` are ignored.

## Commands (run from this directory)

```sh
hugo server -D -F                       # preview drafts and future pages
hugo --minify --gc --cleanDestinationDir --printI18nWarnings --panicOnWarning
python3 scripts/check-site.py           # generated-page regression checks
python3 scripts/test-fetch-cvs.py       # offline download-failure tests
python3 scripts/fetch-cvs.py             # network required; run after Hugo
python3 scripts/check-site.py --require-cvs
```

Use the Hugo version pinned in `.github/workflows/build-and-deploy.yaml` for
release checks (currently 0.164.0). Python 3 and curl are needed for CV downloads
and validation; no Python packages are needed. If the default Hugo cache is
unwritable, add `--cacheDir /tmp/jkorbmacher-hugo-cache`.

Check desktop and narrow mobile layouts after styling changes. Check language
switching, home return links, CV mapping, and the independent slide viewer. See
[doc/development.md](doc/development.md) for the embargo regression check and
[doc/internationalization.md](doc/internationalization.md) before adding content.
