# Deployment and CV hosting

## Local preview

Install [Hugo Extended](https://gohugo.io/installation/) version 0.146 or newer.
From the repository root, run:

```sh
hugo server -D -F
```

Open the local address printed by Hugo. The `-D` flag includes draft pages and
`-F` includes embargoed pages with a future `publishDate`. Stop the server with
`Ctrl-C`.

To perform the production build used during deployment:

```sh
hugo --minify --gc --cleanDestinationDir
```

The generated site is written to `public/`. This directory is ignored by Git
because GitHub Actions builds it afresh.

## Deployment

The workflow in `.github/workflows/build-and-deploy.yaml` uses GitHub’s
artifact-based Pages deployment:

1. A push to `main` starts the workflow.
2. Hugo builds the site into `public/`.
3. The workflow downloads the current CV from Dropbox into the temporary build.
4. The finished `public/` directory is uploaded as a GitHub Pages artifact.
5. GitHub Pages deploys that artifact at `jkorbmacher.org`.

Generated files and the CV are not committed to `main`, a `gh-pages` branch, or
Git history.

The workflow pins the Hugo version instead of installing an untested `latest`
release. When updating that version, install the same Hugo release locally,
run the production build, and then change `hugo-version` in the workflow.

The workflow also builds pull requests as a check, but only deploys from
`main`. It can be started manually from the GitHub Actions interface.

There are no scheduled deployments. To publish future-dated content, wait until
after its `publishDate`, open the repository’s **Actions** tab, select
**Build and deploy**, choose **Run workflow**, and run it from `main`. A normal
push to `main` after the publication date has the same effect.

### Initial GitHub Pages configuration

After placing this project in the GitHub repository:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Confirm that the custom domain is `jkorbmacher.org`.
4. Enable **Enforce HTTPS** once the domain is working correctly.
5. Push to `main` and confirm that **Build and deploy** succeeds under the
   repository’s **Actions** tab.

The domain’s DNS records must point to GitHub Pages. GitHub’s recommended
records can change, so consult the current
[custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
before changing DNS.

### Replacing an existing repository

If the previous site’s history is not useful, replacing `main` with one clean
commit is reasonable. Keep a local copy of the old repository first. Prefer
`--force-with-lease` over `--force`: it refuses to overwrite a remote update
that appeared after the remote branch was last fetched.

A safe outline is:

1. Make a local backup of the old repository.
2. Initialize this project as a new Git repository and make its initial commit.
3. Add the existing GitHub repository as `origin`.
4. Fetch `origin/main` so Git knows the exact branch state it is replacing.
5. Push the new `main` with `--force-with-lease`.
6. Confirm the GitHub Pages source is still **GitHub Actions** and inspect the
   first **Build and deploy** run.

Repository settings—including the custom domain and Pages configuration—are
not part of branch history, so replacing `main` does not normally remove them.
Branch protection may reject the replacement; if so, temporarily permit force
pushes for the branch and restore the protection immediately afterward.

If preserving history matters, copy this project over the old checkout and
make an ordinary commit instead. That is safer but leaves the old site in Git
history.

## Updating the CV

The public CV address is:

```text
https://jkorbmacher.org/cv_jkorbmacher.pdf
```

The PDF itself remains in Dropbox. During deployment, the workflow follows the
Dropbox shared link and adds the PDF only to the temporary Pages artifact.
This provides a first-party-looking URL without adding a binary file to the
repository.

To publish a revised CV:

1. Replace the existing file in Dropbox while preserving its shared link.
2. Open the GitHub repository’s **Actions** tab.
3. Select **Build and deploy**.
4. Choose **Run workflow** and run it from `main`.
5. After deployment completes, check
   `https://jkorbmacher.org/cv_jkorbmacher.pdf`.

A normal push to `main` also fetches and deploys the current Dropbox copy.

The workflow checks that the download starts with the PDF file signature. If
the Dropbox link is broken, private, or returns an error page, deployment fails
instead of replacing the CV with invalid content. The previously deployed site
remains available.

### Changing the Dropbox source link

If Dropbox creates a new shared link:

1. Open `.github/workflows/build-and-deploy.yaml`.
2. Find `CV_URL` under **Add current CV to deployment**.
3. Replace its value with the new shared link.
4. Change the final `dl=0` to `dl=1`, or add `&dl=1` if there is no `dl`
   parameter.
5. The optional Dropbox `st` parameter can be removed.
6. Commit and push the workflow change to `main`.

The relevant part of the workflow looks like this:

```yaml
env:
  CV_URL: "https://www.dropbox.com/scl/fi/.../cv_jkorbmacher.pdf?rlkey=...&dl=1"
```

Test the new shared link in a private browser window before deploying. It must
work without signing in to Dropbox.

### Changing the public CV address

The filename used on `jkorbmacher.org` is set by the workflow’s `--output`
argument:

```sh
--output public/cv_jkorbmacher.pdf
```

For example, changing this to:

```sh
--output public/cv.pdf
```

makes the deployed address `https://jkorbmacher.org/cv.pdf`.

After changing the output filename, update the final CV link in
`content/_index.md` to match:

```md
[Recent CV](https://jkorbmacher.org/cv.pdf)
```

The output filename and homepage URL must agree. Otherwise, the homepage will
link to a file that does not exist.

### Changing or hiding the homepage link

The visible “Recent CV” link is the final paragraph in `content/_index.md`.
Change its Markdown label to rename it, change its URL to point somewhere else,
or remove that paragraph to hide it.

Changing the Markdown link does not change where the workflow obtains the PDF.
The Dropbox source is controlled separately by `CV_URL` in the workflow.

## Publishing checklist

- Run `hugo --minify --gc --cleanDestinationDir`.
- Preview the homepage at desktop and mobile widths.
- Check every public link.
- Confirm that unfinished pages still have `draft: true`.
- Push to `main`.
- Verify the **Build and deploy** workflow.
- Check the live homepage and CV URL after deployment.

## Troubleshooting

### The site workflow builds but does not deploy

Confirm that **Settings → Pages → Source** is set to **GitHub Actions**, and
that the workflow was run from `main`. Pull requests are intentionally built
without being deployed.

### The CV download step fails

Open the Dropbox shared link in a private browser window to confirm that it is
publicly accessible. If Dropbox generated a new shared link, replace `CV_URL`
in the workflow and run it again.

### A draft page appears locally but not online

This is expected when using `hugo server -D`. Production builds omit pages with
`draft: true`.
