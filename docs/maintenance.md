# Maintaining content and pages

## Site structure

Hugo turns Markdown, YAML data, templates, and assets into the static files
served by GitHub Pages.

| Path | Purpose |
| --- | --- |
| `content/_index.md` | Homepage title, introduction, and profile-image settings |
| `data/contact.yaml` | Postal address and email address |
| `data/links.yaml` | Links shown under “Elsewhere” |
| `data/projects.yaml` | Links shown under “Projects” |
| `content/projects/digital-proof-tools/index.md` | NWO project page |
| `content/slides/` | Slide entries discovered automatically by the homepage |
| `layouts/slides/` | Independent layouts used by slide pages |
| `layouts/` | HTML templates, including the minimal base layout |
| `assets/css/main.css` | The complete visual design |
| `assets/images/me.png` | Source profile photograph |
| `assets/icons/` | Self-hosted SVG icons |
| `static/` | Files copied unchanged to the finished site |
| `archetypes/` | Templates used by `hugo new content` |

## Editing the homepage

Edit `content/_index.md`. The front matter between the `---` lines controls the
title, description used by search engines, and profile image. The text below
the front matter is ordinary Markdown.

External links written in Markdown automatically open in a new tab and receive
the small external-link indicator. Internal links remain in the same tab.

## Editing contact information

Edit `data/contact.yaml`. The homepage template reads this file directly, so
the contact details do not need to be duplicated in HTML.

Keep the existing field names unless the corresponding markup in
`layouts/home.html` is also updated.

## Editing homepage links

Edit `data/links.yaml`. Each entry follows this form:

```yaml
- title: "Project name"
  url: "https://example.org/"
  icon: "diagram-3"
  enabled: true
```

Set `enabled: false` to retain an entry without publishing it. Available icon
names are the SVG filenames in `assets/icons/`, without the `.svg` extension.

## Editing project links

Edit `data/projects.yaml`. Project entries use the same structure as the
Elsewhere links:

```yaml
- title: "Project title"
  url: "/projects/project-name/"
  icon: "truthmaker"
  description: "A short description shown below this project name."
  enabled: true
```

Use a root-relative URL beginning with `/` for a page in this Hugo site, or a
complete `https://` URL for an external project. Internal project links remain
in the same tab; external ones open in a new tab. `icon` selects the project
mark rendered by `layouts/home.html`; the currently supported values are
`truthmaker` and `proof-ai`. `description` contains the optional italic text
shown directly beneath that project’s name.

## Adding an ordinary page

Create a draft:

```sh
hugo new content pages/page-name.md
```

Edit the new Markdown file and preview it with:

```sh
hugo server -D
```

The `-D` flag includes drafts. Change `draft: true` to `draft: false` when the
page is ready to publish, then add a link to it from `data/links.yaml` or another
appropriate content page. There is deliberately no global menu.

To remove a temporary page from the public site without deleting your work,
set `draft: true` again or remove its public link.

## Adding a project page

Create a page bundle from the project archetype:

```sh
hugo new content --kind projects projects/project-name/index.md
```

The ordinary page design is used automatically. A project can instead have a
completely independent design:

1. Add `layout: "project-name"` to the page front matter.
2. Create `layouts/projects/project-name.html`.
3. Use `layouts/projects/lean.html` as a structural example, or replace its
   markup entirely.

The Digital Proof Tools page demonstrates this mechanism. Set `draft: true` in
a page’s front matter to omit it from production while it is being prepared.

Its `milestones` and `collaborators` are maintained in the page front matter.
Milestone `status` accepts `planned`, `active`, or `complete`; the project
layout turns these into empty, active, or checked markers. The `subtitle` and
milestone `description` fields accept Markdown links. An optional milestone
`url` adds an “Open milestone output” link, while a collaborator `url` links
the collaborator’s name. `funder_url` links the funder shown in the project
metadata.

## Adding slides

The homepage builds the “Slides” list automatically from published pages in
`content/slides/`. Each slide page can use an iframe, Reveal.js, or a completely
custom layout. See [Adding and hosting slides](slides.md) for examples and
maintenance instructions.

## Embargoing a project page

Use Hugo’s `publishDate` front-matter field to commit and develop a page without
publishing it:

```yaml
publishDate: 2027-01-15T09:00:00+01:00
draft: false
```

Set the date, time, and UTC offset to the embargo deadline. Before that moment,
normal production builds omit both the internal project page and its homepage
link and description. External projects are unaffected.

Preview drafts and embargoed pages locally with:

```sh
hugo server -D -F
```

`-D` includes drafts and `-F` includes pages whose `publishDate` is still in the
future. Do not add `-F` to the production workflow.

The Digital Proof Tools page is set to publish from 00:00 Europe/Amsterdam on
1 September 2026. Run the **Build and deploy** workflow manually on or after
that date to update the live site. If the date changes, update `publishDate` in
`content/projects/digital-proof-tools/index.md`. Manual deployment is
documented in `docs/deployment.md`.

## Images and downloadable files

- Put images Hugo should process in `assets/images/`.
- Put files that should be copied unchanged in `static/`.
- A file at `static/slides/talk.pdf` becomes
  `https://jkorbmacher.org/slides/talk.pdf`.

The CV is handled differently so that its binary data is not committed to Git.
See [Deployment and CV hosting](deployment.md#updating-the-cv).

## Design implementation

The homepage aims for the density and directness of a well-maintained README:
Tahoma-based typography, a white background, Markdown-style heading markers,
ordinary underlined links, and minimal decoration.

The design is contained in `assets/css/main.css`. The small Bootstrap Icons
subset is self-hosted in `assets/icons/`; its license and the site’s other
third-party notices are published from `static/third-party-notices.txt`.
