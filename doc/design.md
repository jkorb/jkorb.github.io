# Design

## Intent

A personal academic website with the directness of a README. Readers should
quickly find the biography, contact details, CV, projects, and presentations.
Content determines the page length. Avoid global menus, cards, animation,
decorative imagery, frameworks, tracking, and remote font dependencies.

## Visual system

- White background `#ffffff`, dark text `#1f2328`, secondary text `#59636e`.
- Blue links `#0969da`, hover `#0550ae`, subdued separators `#d1d9e0b3`.
- The site uses CMU Serif for prose and headings, with Latin
  Modern Roman, Georgia, and serif fallbacks. Body text is 1.1875rem (19px at the
  default browser size), or 1.125rem (18px) on narrow screens. Descriptive text,
  abstracts, and prose use 1.45 line height; the general body default is 1.55.
  Headings use regular weight; the homepage title scales from 2.125rem
  to 3rem. Section headings are 1.75rem. Real bold and italic faces support
  emphasis and milestone titles.
- Open Sans, with Arial and sans-serif fallbacks, is reserved for language
  navigation, the skip link, project metadata, status labels, and the footer.
  This gives the LaTeX typeface room to establish the site's academic identity
  while keeping small interface text clear.
- Content width 48rem; page gutters 1rem. The homepage pairs a 12rem grayscale
  portrait with the introduction, separated by 2.5rem. At 40rem and below it
  becomes a single column and the portrait is 9rem wide. The introduction has
  0.625rem (10px) paragraph spacing, as do prose and project body paragraphs;
  the lower sections begin 2.75rem below the introduction and are separated by
  2.5rem.
- Plain headings and underlined links. Prose links omit external-link arrows;
  compact metadata, collaborator lists, profile links, and PDF/CV links retain
  their useful icons.
- Contact, profiles, projects, and slides form a simple vertical sequence.
- Project descriptions use upright body text. Reserve italics for explicit
  emphasis in the content rather than applying them to entire descriptions.
- Project pages add a compact metadata line and a milestone list. Status markers
  are accompanied by words, so color is not the only indication of state.

The existing design uses gray accents. Do not introduce a new palette based on
older instructions elsewhere in the workspace.

## Language control

Four small text links (`en`, `de`, `nl`, `it`) sit above the content at the right
edge. The current language has a thin border and bold text. Each target is at
least 32 by 32 CSS pixels, has a native-language accessible name and a visible
keyboard focus outline. Flags are unnecessary: these are language choices.

The control uses ordinary links in a labeled `nav`, so it works without scripts,
cookies, or browser language detection. A switch goes to the equivalent page.
Only published translations are offered. The slide viewer uses the same control
in its upper-right corner, opposite the existing home-return control.

## Accessibility and metadata

Set the document language and link language explicitly. Translate image alt
text, skip links, navigation labels, metadata, section labels, and status words.
Preserve a logical heading hierarchy and visible focus states. The current
language uses `aria-current="page"`; decorative icons are hidden from assistive
technology. Each page declares its own canonical URL and links to actual
translations using `hreflang`, with English as `x-default` when available.

External Markdown links open in a new tab with `noopener noreferrer`. Navigation
and CV links stay in the same tab. Keep institutional, publication, and project
names intact. Third-party slide contents and license texts retain their original
language.

## Boundaries

`fonts.css` declares local font faces and family variables. `main.css` owns the
site layout; `languages.css` and `fonts.css` are shared with the independent slide
viewer. No runtime JavaScript is needed. Use Hugo templates and data for
repeated structure, Markdown for prose, and language dictionaries for shared
labels. Add a custom layout only when the content needs one.

## Bundled fonts

The site uses self-hosted WOFF2 files in `static/fonts/computer-modern/`:
CMU Serif Roman, Italic, Bold, and BoldItalic. These are Computer Modern Unicode
fonts, a Unicode implementation of the Computer Modern family. The files were
downloaded unchanged on 2026-10-20 from
[vsalvino/computer-modern](https://github.com/vsalvino/computer-modern/tree/f55b094cc91a643fecde154bb7ddb6fd9fed1b54/fonts),
at commit `f55b094cc91a643fecde154bb7ddb6fd9fed1b54`. That distribution converts
the [Computer Modern Unicode](https://cm-unicode.sourceforge.io/) fonts to
WOFF2. Its original copyright notices and SIL Open Font License 1.1 are bundled
at `static/fonts/computer-modern/OFL.txt`.

Open Sans normal, with variable weights 400–700, supplies interface text. Its
Latin and Latin Extended subsets cover the four site languages. `font-display:
swap` keeps text visible while the fonts load. Browsers fetch only the faces
and subsets used on a page. Mathematical project symbols retain their dedicated
font stacks. The independent slide viewer uses the same sans-serif interface
font; the presentation inside its iframe controls its own typography.

The earlier Open Sans italic and Merriweather files remain as unused assets
from the previous pairing. They are not declared or requested by the current
stylesheets.

The Open Sans and Merriweather files were downloaded from the [Google Fonts CSS API](https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400..700;1,400..700&family=Merriweather:wght@700&display=swap)
on 2026-10-05 using a current Chrome user agent (Open Sans service version v44,
Merriweather v33). The downloaded font files are unchanged. There are no Google
Fonts requests at runtime. The original SIL Open Font License texts are bundled
at `static/fonts/open-sans/OFL.txt` and `static/fonts/merriweather/OFL.txt`, from
[Open Sans](https://github.com/google/fonts/tree/main/ofl/opensans) and
[Merriweather](https://github.com/google/fonts/tree/main/ofl/merriweather).

To change the pairing, edit the families in `assets/css/fonts.css` and replace
font files and license notices as necessary. The font CSS is concatenated into
both the main stylesheet and the slide control stylesheet; relative font URLs
resolve from `/css/` to `/fonts/`.

## Favicon

The `JK` mark in `static/favicon.svg` uses outlines from the bundled CMU Serif
Bold font. Bold keeps the strokes visible at tab size; page headings retain
their lighter regular weight. The mark preserves the white rounded tile and
dark text. Each letter is shifted 1.5 units inward on the 64-unit canvas to
tighten the pair while retaining a small gap between the top serifs. Outlined
letters render without an installed font or a font download.

`static/favicon.ico` is the fallback, with 16, 32, 48, and 64px images.
`layouts/partials/favicons.html` supplies both formats to the main layout and
the independent slide viewer. Home-return controls use the same SVG mark.
To regenerate the ICO after editing the SVG, use ImageMagick:

```sh
magick -background none -density 384 static/favicon.svg -define icon:auto-resize=64,48,32,16 static/favicon.ico
```

This is an asset-maintenance command; the Hugo build does not need ImageMagick.

## Social-sharing images

The 1200 × 630 sharing cards use CMU Serif Roman for the name and description,
Open Sans for the blue site address, and the site's white background and muted
gray accents. Each language has its own card:

| Language | Vector source | Published image |
| --- | --- | --- |
| English | `assets/social/og.svg` | `static/og.png` |
| German | `assets/social/og.de.svg` | `static/og.de.png` |
| Dutch | `assets/social/og.nl.svg` | `static/og.nl.png` |
| Italian | `assets/social/og.it.svg` | `static/og.it.png` |

The artwork uses the name and description from the corresponding homepage
front matter. Its letters are outlined from the bundled fonts, so exports do
not depend on installed fonts. Keep the artwork in sync when changing those
fields. The SVG titles, descriptions, and comments retain the text represented
by the paths.

`layouts/partials/social-metadata.html` selects the matching image, publishes
its dimensions, and supplies translated image descriptions for Open Graph and
Twitter cards. Both the main layout and the independent slide viewer use this
partial. Page-specific titles and descriptions remain separate from the shared
identity card.

To export a revised SVG with ImageMagick:

```sh
magick -background white assets/social/og.svg -strip PNG24:static/og.png
```

Use the corresponding `.de`, `.nl`, or `.it` paths for translated cards.
The PNGs are committed assets; the Hugo build needs no additional tools.
