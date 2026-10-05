# Website knowledge base

`jkorbmacher.org` is a small, static Hugo website deployed to GitHub Pages.
Start with the [agent guide](../AGENTS.md) for working rules.

- [Development](development.md): architecture, local commands, checks, and file map.
- [Design](design.md): visual principles, layout, accessibility, and constraints.
- [Internationalization](internationalization.md): languages, translations, and CV mapping.
- [Content maintenance](maintenance.md): editing and adding pages and projects.
- [Deployment and CVs](deployment.md): GitHub Pages and Dropbox releases.
- [Slides](slides.md): embedded presentations and custom layouts.

| Task | Source |
| --- | --- |
| Edit biography | `content/_index.md` and `content/_index.{de,nl,it}.md` |
| Change interface labels | `i18n/{en,de,nl,it}.yaml` |
| Change contact details / profile links | `data/contact.yaml` / `data/links.yaml` |
| Edit project links / descriptions | `data/projects.yaml` / `i18n/*.yaml` |
| Edit project text and milestones | `content/projects/digital-proof-tools/index*.md` |
| Update CV releases | `data/cv.json` |
| Replace portrait | `assets/images/me.png` |
| Change styling | `assets/css/main.css`, `assets/css/languages.css`, `assets/css/fonts.css` |
| Change languages or site defaults | `hugo.toml` |
| Publish | [Deployment](deployment.md) |
