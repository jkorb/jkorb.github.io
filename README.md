# jkorbmacher.org

Source for Johannes Korbmacher’s personal website at
[jkorbmacher.org](https://jkorbmacher.org/).

The site is built with [Hugo](https://gohugo.io/) and deployed automatically to
GitHub Pages. It uses a small custom design: no theme, no JavaScript framework,
and no externally loaded fonts or icons.

## Development

Use Hugo 0.164.0 (the deployment version), then run:

```sh
hugo server -D
```

For a production build:

```sh
hugo --minify --gc --cleanDestinationDir --printI18nWarnings --panicOnWarning
python3 scripts/check-site.py
```

The generated `public/` directory is intentionally ignored by Git.

## Repository structure

- `content/` — Markdown pages
- `data/` — contact details and homepage links
- `i18n/` — English, German, Dutch, and Italian interface text
- `scripts/` — CV downloads and generated-site checks
- `layouts/` — Hugo templates
- `assets/` — processed styles, icons, and images
- `static/` — files copied unchanged to the site
- `archetypes/` — templates for creating new content
- `doc/` — maintenance and deployment documentation
- `.github/workflows/` — automatic GitHub Pages deployment

## Documentation

Start with [AGENTS.md](AGENTS.md) for agent working instructions.

US English is the default at `/`. German, Dutch, and Italian use `/de/`, `/nl/`,
and `/it/`, with a small language control on every translated page. CVs are
fetched from Dropbox during deployment; run `python3 scripts/fetch-cvs.py` after
a local build to include them. Python 3 and curl are required for this step.

The detailed documentation is kept separately:

- [Documentation index](doc/README.md)
- [Development and checks](doc/development.md)
- [Design](doc/design.md)
- [Internationalization](doc/internationalization.md)
- [Maintaining content and pages](doc/maintenance.md)
- [Deployment and CV hosting](doc/deployment.md)
- [Adding and hosting slides](doc/slides.md)

## License notices

The bundled Bootstrap Icons subset is covered by the notices in
[static/third-party-notices.txt](static/third-party-notices.txt). Hugo publishes
that file at `/third-party-notices.txt`.
