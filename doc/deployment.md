# Deployment and CV hosting

## Build and publish

`.github/workflows/build-and-deploy.yaml` uses GitHub's artifact-based Pages
workflow. Pull requests build and validate the site. A push to `main`, or a
manual workflow run from `main`, also deploys it.

1. Hugo 0.164.0 builds the production site with missing-translation warnings enabled.
2. Offline download-validation tests run, then `python3 scripts/fetch-cvs.py`
   downloads the four current CV releases.
3. `python3 scripts/check-site.py --require-cvs` validates pages, navigation, and PDFs.
4. The workflow uploads `public/` as the Pages artifact.
5. The deployment job publishes it at `https://jkorbmacher.org/`.

Generated files and CV PDFs are never committed. A failed build, CV download, or
validation check prevents deployment; the previously deployed site remains live.

Run the same commands locally before publishing:

```sh
hugo --minify --gc --cleanDestinationDir --printI18nWarnings --panicOnWarning
python3 scripts/fetch-cvs.py
python3 scripts/check-site.py --require-cvs
```

Check all four homepages and the project/slide views at desktop and mobile
widths. Confirm drafts and future pages are absent. After pushing to `main`,
check the workflow result, all language switches, and all four live CV URLs.

The workflow pins Hugo for reproducibility. Test a production build and the
regression checks with a proposed new version before changing the pin. See
[development](development.md) for local preview and embargo checks.

## GitHub Pages configuration

In **Settings → Pages**, select **GitHub Actions** as the source, set the custom
domain to `jkorbmacher.org`, and enable **Enforce HTTPS** when available. Follow
GitHub's current [custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
if DNS changes are needed.

There is no scheduled deployment. When an embargo expires, push a change or run
**Actions → Build and deploy → Run workflow** from `main`. Hugo evaluates
`publishDate` at build time. Never add `-F` to production to bypass the embargo.

## Updating CV releases

| Release | Public URL |
| --- | --- |
| English (US) | `https://jkorbmacher.org/cv_jkorbmacher.pdf` |
| German | `https://jkorbmacher.org/de/cv.pdf` |
| Dutch | `https://jkorbmacher.org/nl/cv.pdf` |
| Italian | `https://jkorbmacher.org/it/cv.pdf` |

Each source URL and public path is maintained in `data/cv.json`. If replacing a
Dropbox file preserves its shared link, rerun the deployment workflow to publish
the new version. If Dropbox creates a new link, update that language's `source`
in the manifest, retain `rlkey`, and use `dl=1`. The optional `st` parameter is
not required. Confirm the link works without a Dropbox login.

The download script stages every PDF, verifies the `%PDF-` signature and EOF
marker, and only then moves the files to their public paths. These checks catch
HTML error pages and incomplete downloads; they do not verify the CV's wording.
Review the release itself when changing it.

The `{{< cv >}}` shortcode in each homepage selects the matching path from the
same manifest. Change labels in `i18n/*.yaml`. Preserve the existing English
public path so old links keep working.

CVs are added after Hugo builds. A clean rebuild removes them; run the fetch
script again afterward. Network-free local checks may omit downloading and run
`python3 scripts/check-site.py` without `--require-cvs`.

## Troubleshooting

- **Build succeeds but does not deploy:** PR builds deliberately do not deploy.
  Check that the workflow ran from `main` and Pages uses GitHub Actions.
- **CV fetch fails:** check network access and the public Dropbox link. Update the
  manifest if its share key changed. Do not substitute an HTML download page.
- **A page is visible only locally:** preview flags may include drafts or future
  content. Check `draft` and `publishDate` in all translations.
- **A translated project link disappears:** it is only listed when that language's
  target page is published. Keep publication fields synchronized.
