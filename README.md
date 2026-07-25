# jkorbmacher.org

Source for Johannes Korbmacher’s personal website at
[jkorbmacher.org](https://jkorbmacher.org/).

The site is built with [Hugo](https://gohugo.io/) and deployed automatically to
GitHub Pages. It uses a small custom design: no theme, no JavaScript framework,
and no externally loaded fonts or icons.

## Development

Install Hugo Extended 0.146 or newer, then run:

```sh
hugo server -D
```

For a production build:

```sh
hugo --minify --gc --cleanDestinationDir
```

The generated `public/` directory is intentionally ignored by Git.

## Repository structure

- `content/` — Markdown pages
- `data/` — contact details and homepage links
- `layouts/` — Hugo templates
- `assets/` — processed styles, icons, and images
- `static/` — files copied unchanged to the site
- `archetypes/` — templates for creating new content
- `docs/` — maintenance and deployment documentation
- `.github/workflows/` — automatic GitHub Pages deployment

## Documentation

The detailed documentation is kept separately:

- [Documentation index](docs/README.md)
- [Maintaining content and pages](docs/maintenance.md)
- [Deployment and CV hosting](docs/deployment.md)
- [Adding and hosting slides](docs/slides.md)

## License notices

The bundled Bootstrap Icons subset is covered by the notices in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
