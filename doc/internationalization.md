# Internationalization

## Language and URL policy

| Language | Hugo key / switcher | HTML locale | Homepage | CV |
| --- | --- | --- | --- | --- |
| English (US), default | `en` | `en-US` | `/` | `/cv_jkorbmacher.pdf` |
| German | `de` | `de-DE` | `/de/` | `/de/cv.pdf` |
| Dutch | `nl` | `nl-NL` | `/nl/` | `/nl/cv.pdf` |
| Italian | `it` | `it-IT` | `/it/` | `/it/cv.pdf` |

The switcher uses [ISO 639 two-letter codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).
Italian uses `it`, even though the supplied PDF filename uses `ita`. The English
locale is explicitly US English; the generic `en` key keeps the control compact.
Hugo also generates an `/en/` redirect to `/`. Existing English page URLs remain
unchanged. There is no automatic browser-language redirect or stored preference.

## Editing translations

Use [Hugo's translation-by-filename convention](https://gohugo.io/content-management/multilingual/):

```text
content/_index.md
content/_index.de.md
content/_index.nl.md
content/_index.it.md
content/projects/digital-proof-tools/index.md
content/projects/digital-proof-tools/index.de.md
```

Unsuffixed files belong to English. Use the same base filename and bundle for
translations, and keep slugs unchanged unless deliberately changing a URL.
Translate body text and descriptive front matter. Keep `draft`, `publishDate`,
layout, milestone status identifiers, collaborators, funder URLs, and embed URLs
synchronized. The current project and slide wrapper exist in all four languages.
The presentation title and externally hosted slides remain in their original
language.

Shared headings, status labels, project summaries, accessible labels, and address
floor/country labels live in `i18n/{en,de,nl,it}.yaml`. Add each new key to all four
files. `data/projects.yaml` references summaries with `description_key`; project
names and URLs stay in the shared record. Contact and profile data are shared.
Page metadata lives in front matter; language-specific defaults live in
`hugo.toml`.

Preserve official institution, journal, project, software, and personal names.
Translate surrounding prose and generic disciplines. Preserve research claims,
dates, quantities, and all link destinations. Do not translate paper or talk
titles. Third-party legal notices remain verbatim.

## Navigation and incomplete translations

`languages.html` and `language-alternates.html` use `.AllTranslations`. They offer
only existing, published counterparts; no false fallback page is labeled as a
translation. A page with no translations has no switcher. Translate all public
pages for the current four-language site, and update the regression checks when
adding routes. Hugo's missing-translation warnings are fatal in CI; maintain key
parity because Hugo can otherwise fall back to English.

Resolve internal project links using `site.GetPage` and the resulting page's
`RelPermalink`. Use Hugo's `relref` shortcode for internal links in translated
Markdown, for example `[Project]({{< relref "/projects/digital-proof-tools" >}})`.
Avoid hardcoding `/projects/.../` as a visitor-facing URL in translated prose.

## CVs

`data/cv.json` maps each Hugo language key to a public path and a Dropbox source.
The homepage's `{{< cv >}}` shortcode selects the record and translated label.
`scripts/fetch-cvs.py` reads the same manifest, downloads all PDFs into temporary
files, and validates their signatures and end markers before installing them
into `public/`. English retains its existing public address.

To replace a release, edit only its `source` in the manifest. Keep `rlkey`, use
`dl=1` for downloading, and omit the optional `st` parameter. Build, fetch, and
run `check-site.py --require-cvs` before publishing. See [deployment](deployment.md).
