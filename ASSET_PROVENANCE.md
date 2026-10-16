# Generated Asset Provenance Inventory

## Scope and baseline

This comparison was captured from GitHub's recursive Git Trees API on 2026-10-16, using baseline commit `f2c5f97cbd80bc0fd458632116c43e41854df33b` for this fork and the upstream `gh-pages` tree available at the time. The baseline was taken **before** this audit added `LICENSES.md` and `ASSET_PROVENANCE.md`; therefore counts and path differences below describe the pre-audit generated tree, not the current repository after documentation additions.

This is a file-tree comparison, not a per-file licence determination or proof that every content difference is a bug.

## Baseline counts

| Measure | Observed value |
| --- | ---: |
| Fork tree entries (files + directories) | 176 |
| Fork file entries (blobs) | 170 |
| Fork directory entries | 6 |
| Upstream tree entries in comparison | 172 |
| Fork-only paths | 6 |
| Upstream-only paths | 2 |

## Path differences observed

### Paths present only in the fork's baseline snapshot

- `JAHIDS_AI_ALIGNMENT.md`
- `README.md`
- `THIRD_PARTY_NOTICES.md`
- `platforms/django.html`
- `tags/monitoring.html`
- `tags/status--uptime-pages.html`

### Paths present in upstream snapshot but absent from the fork's baseline

- `tags/monitoring--status-pages.html`
- `tags/travel-organization.html`

Many shared generated paths had different Git blob identifiers between the snapshots. This proves the output was not byte-for-byte identical, but does not by itself establish whether differences are intentional, stale, or defective. Check the source data and generation process before replacing generated pages.

## Verified generation process

The upstream data repository's [Makefile](https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/Makefile) documents the `export_html` target. It clones the upstream HTML repository, generates HTML with `hecat` and Sphinx, removes the contents of the generated HTML output directory, and its `push_html` target commits and pushes generated output to the upstream HTML repository. This means the HTML tree is a build artifact, not the authoritative place to edit catalogue data or generator configuration.

Before synchronizing generated pages, preserve fork-specific documentation and inspect the diff. An upstream regeneration can replace generated files wholesale, and a manual fix to an HTML page may disappear at the next build.

## Asset categories and licence review status

| Category | Examples | Status |
| --- | --- | --- |
| Generated catalogue pages | `index.html`, `platforms/*.html`, `tags/*.html` | Inherited/generated; file-level rights and freshness not exhaustively verified |
| Sphinx support files | `genindex.html`, `search.html`, `searchindex.js`, `_static/doctools.js`, `_static/searchtools.js` | Generated framework files; inspect source/version notices |
| Furo theme assets | `_static/styles/furo.css`, `_static/scripts/furo.js`, maps and extension files | Preserve and review upstream package notices |
| Sphinx Design assets | `_sphinx_design_static/*`, Sphinx Design CSS and JavaScript | Verify upstream package and licence |
| Images and identity assets | `_static/awesome.png`, `_static/logo.svg`, `_static/favicon.ico` | Rights-holder and terms not individually confirmed by this inventory |
| Fork documentation | `README.md`, `JAHIDS_AI_ALIGNMENT.md`, `THIRD_PARTY_NOTICES.md`, `LICENSES.md`, this file | Documentation; does not relicense inherited content |

## Licence evidence

- The upstream catalogue README identifies the catalogue/list as **CC BY-SA 3.0**. That scope is not a blanket licence for every asset in the generated HTML repository.
- The upstream HTML repository metadata did not identify a repository-wide SPDX licence in the inspected metadata, and the inspected generated branch had no root-level `LICENSE` file.
- The upstream Makefile injects an attribution string into the generated Furo page identifying hecat, Sphinx, Furo, the CC BY-SA 3.0 catalogue content, the source-code repository, and the raw-data repository. Preserve this attribution when regenerating or modifying the page.
- A Sphinx/Furo file may have its own copyright or licence notice. Check and retain file-specific notices.
- No complete file-by-file licence scan has been performed. Unknown items remain unverified, not free of restrictions.

See [LICENSES.md](./LICENSES.md) and [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

## Remaining audit actions

1. Trace bundled scripts, stylesheets, maps, icons, logos, and favicons to their exact upstream source and licence.
2. Run internal-link checks across all generated HTML and external-link checks with sensible rate limits.
3. Run secret scanning and suitable static/security checks.
4. Verify the published site in a browser after deployment.
5. Refresh this inventory when the generated tree changes.

## Limitations

This inventory does not represent a complete URL crawl, visual/browser check, security scan, dependency analysis, or legal opinion. Those checks must be run before they can be reported as passed.
