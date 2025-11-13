# Tech Notes — Quarto Blog

Minimalist, dark-themed technical notes built with [Quarto](https://quarto.org/). Supports code highlighting, LaTeX math, images, and PDF export.

## Prerequisites

- Install Quarto: https://quarto.org/docs/get-started/
- (Optional) LaTeX distribution for PDF output (e.g., TinyTeX, TeX Live, MiKTeX)

## Local Preview

```bash
quarto preview
```

This starts a local server and watches for file changes.

## Render the Site (static files)

```bash
quarto render
```

The static site is generated into the `docs/` directory (configured in `_quarto.yml`).

## Export a Single Post to PDF

```bash
quarto render posts/math-and-code-demo.qmd --to pdf
```

This requires a LaTeX installation. Adjust the path for any post you want to export.

## Deploy to GitHub Pages

1. Initialize a Git repository and push to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initialize Quarto tech blog"
   git branch -M main
   git remote add origin https://github.com/<your-user>/<your-repo>.git
   git push -u origin main
   ```
2. On GitHub, open the repository Settings → Pages.
3. Under "Build and deployment", choose "Deploy from a branch".
4. Select branch `main` and folder `/docs` as the Pages source.
5. Save. Your site will be published at `https://<your-user>.github.io/<your-repo>/`.

### Optional: Publish via Quarto

If you have GitHub Pages support set up in Quarto locally, you may also publish using:

```bash
quarto publish gh-pages
```

This is optional; the branch-based Pages deployment described above is sufficient and recommended for most setups.

