# Design

## Intent

A personal academic website with the directness of a README. Readers should
quickly find the biography, contact details, CV, projects, and presentations.
Content determines the page length. Avoid global menus, cards, animation,
decorative imagery, frameworks, tracking, and remote font dependencies.

## Visual system

- White background `#ffffff`, dark text `#1f2328`, secondary text `#59636e`.
- Blue links `#0969da`, hover `#0550ae`, subdued separators `#d1d9e0b3`.
- Tahoma with Arial and sans-serif fallbacks; base text 1rem with 1.4 line height.
- Content width 48rem; page gutters 1rem. The homepage pairs a 12rem grayscale
  portrait with the introduction. At 40rem and below it becomes a single column
  and the portrait is 9rem wide.
- `#` and `##` heading markers, underlined links, small inline SVG icons.
- Contact, profiles, projects, and slides form a simple vertical sequence.
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

`main.css` owns the site layout; `languages.css` is shared with the independent
slide viewer. No runtime JavaScript is needed. Use Hugo templates and data for
repeated structure, Markdown for prose, and language dictionaries for shared
labels. Add a custom layout only when the content needs one.
