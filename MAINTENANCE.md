# Maintenance Guide

## First principle

This repository's `gh-pages` branch is generated HTML output, not the authoritative catalogue data or build configuration. For content changes, start with the upstream [data repository](https://github.com/awesome-selfhosted/awesome-selfhosted-data) and its [Makefile](https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/Makefile).

## Why generated files can change

The upstream Makefile's `export_html` target clones the upstream HTML project, generates HTML with hecat and Sphinx, and clears the generated output directory before writing a fresh build. Its `push_html` target commits and pushes the generated files. Consequently, direct edits to generated pages are fragile and can be overwritten.

## Safe workflow for this fork

1. Inspect the upstream data and HTML repositories and record the exact commit or revision used.
2. Keep fork-specific documentation separate from generated assets, and preserve it explicitly when synchronizing output.
3. Build from the documented upstream process where possible; do not hand-edit a generated page to fix an underlying data or template issue.
4. Compare the new generated tree against the current fork before applying changes. Review deleted pages, renamed tags, scripts, stylesheets, and image assets.
5. Preserve all embedded attribution and per-file copyright/licence notices.
6. Run a local-link check, an external URL check with rate limits, and secret/security scanning.
7. Open a pull request for review and verify the GitHub Pages deployment.
8. Report each check as PASS, FAIL, BLOCKED, or NOT TESTED. Never describe an unrun check as passed.

## Licence handling

The catalogue/list is identified upstream as CC BY-SA 3.0. Do not assume that every generated HTML file or bundled third-party asset has the same licence. For uncertain assets, record the source and mark the licence unverified until reliable evidence is available. Do not add a blanket licence to inherited material without a rights review.

## Scope

This guide is operational documentation, not legal advice. See [LICENSES.md](./LICENSES.md), [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md), and [ASSET_PROVENANCE.md](./ASSET_PROVENANCE.md).

## Automated repository health audit

The GitHub Actions workflow at `.github/workflows/repository-health.yml` checks that maintainer documentation is present, verifies the canonical JAHIDS.AI attribution, and records missing or unsafe relative references in generated HTML. It runs on pushes to `gh-pages`, pull requests targeting `gh-pages`, weekly, and on manual dispatch. The report is retained as a workflow artifact for 30 days.

This audit is intentionally non-destructive: it does not rewrite generated HTML, change upstream assets, or infer licences. It does not validate external URL availability, in-page anchors, browser rendering, security vulnerabilities, or per-file rights. Review its findings before making changes.

When regenerating the site, preserve `.github/workflows/repository-health.yml` alongside this fork's maintainer documentation. A successful workflow run is evidence only for the checks it actually executes.
