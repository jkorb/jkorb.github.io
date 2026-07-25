# Website documentation

This folder contains the practical documentation for maintaining
`jkorbmacher.org`.

## Guides

- [Maintaining content and pages](maintenance.md) explains how to edit the
  homepage, contact information, links, images, and Hugo pages.
- [Deployment and CV hosting](deployment.md) explains local builds, GitHub
  Pages deployment, the Dropbox-backed CV, and the publishing checklist.
- [Adding and hosting slides](slides.md) explains the homepage slide list,
  embedded presentations, external slide links, and custom layouts.

## Most common tasks

| Task | Where to look |
| --- | --- |
| Change the introductory text | `content/_index.md` |
| Change the CV link shown in the description | `content/_index.md` |
| Change contact details | `data/contact.yaml` |
| Add or remove a homepage link | `data/links.yaml` |
| Add or remove a research project | `data/projects.yaml` |
| Add, rename, or remove slides | [slides.md](slides.md) |
| Replace the profile photograph | `assets/images/me.png` |
| Change the visual design | `assets/css/main.css` |
| Add a temporary or permanent page | [maintenance.md](maintenance.md) |
| Update the CV | [deployment.md](deployment.md#updating-the-cv) |
| Publish the site | [deployment.md](deployment.md#deployment) |
