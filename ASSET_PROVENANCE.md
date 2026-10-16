# Generated Asset Provenance Inventory

## Scope and method

This is a snapshot of the public `gh-pages` tree for [mdjahid11978-design/awesome-selfhosted-html](https://github.com/mdjahid11978-design/awesome-selfhosted-html), compared with the `gh-pages` tree of [awesome-selfhosted/awesome-selfhosted-html](https://github.com/awesome-selfhosted/awesome-selfhosted-html) using GitHub's recursive Git Trees API on 2026-10-16. It records repository paths and tree differences, not the legal status of every file.

## Snapshot counts

| Measure | Observed value |
| --- | ---: |
| Fork tree entries (files + directories) | 176 |
| Fork file entries (blobs) | 170 |
| Fork directory entries | 6 |
| Upstream tree entries in comparison | 172 |
| Fork-only paths | 6 |
| Upstream-only paths | 2 |

The tree includes generated HTML, Sphinx-related assets, search data, and fork-specific documentation. Generated pages can be large and should not be edited manually as a substitute for changing source data.

## Path differences observed

### Paths present only in this fork's snapshot

- `JAHIDS_AI_ALIGNMENT.md`
- `README.md`
- `THIRD_PARTY_NOTICES.md`
- `platforms/django.html`
- `tags/monitoring.html`
- `tags/status--uptime-pages.html`

### Paths present in upstream snapshot but absent from this fork's snapshot

- `tags/monitoring--status-pages.html`
- `tags/travel-organization.html`

Many shared generated paths have different Git blob identifiers between the two snapshots. This is evidence that the generated output is not byte-for-byte identical; it does not, by itself, establish whether the differences are intended, stale, or defective. Reconcile them against the authoritative data repository and build process before replacing generated pages.

## Asset categories and licence review status

| Category | Examples | Status |
| --- | --- | --- |
| Generated catalogue pages | `index.html`, `platforms/*.html`, `tags/*.html` | Inherited/generated; file-level rights and freshness not exhaustively verified |
| Sphinx support files | `genindex.html`, `search.html`, `searchindex.js`, `_static/doctools.js`, `_static/searchtools.js` | Generated framework files; inspect source/version notices |
| Furo theme assets | `_static/styles/furo.css`, `_static/scripts/furo.js`, maps and extension files | Theme/bundled asset notices must be preserved and reviewed |
| Sphinx Design assets | `_sphinx_design_static/*`, `_static/sphinx-design.min.css`, `_static/design-tabs.js` | Upstream package/source and licence should be verified |
| Images and identity assets | `_static/awesome.png`, `_static/logo.svg`, `_static/favicon.ico` | Rights-holder and terms not individually confirmed by this inventory |
| Fork documentation | `README.md`, `JAHIDS_AI_ALIGNMENT.md`, `THIRD_PARTY_NOTICES.md`, `LICENSES.md`, this file | Fork-maintained documentation; does not relicense inherited content |

## Licence evidence

- The upstream catalogue/list README identifies the catalogue/list as **CC BY-SA 3.0**. This statement is scoped to the catalogue/list and is not a blanket licence for every asset in this generated HTML repository.
- The upstream HTML repository metadata reports no repository-level licence in the inspected metadata, and its generated branch has no root-level `LICENSE` file in the inspected tree.
- A Sphinx/Furo file may contain its own copyright or licence notice. Such notices must be checked per file and retained.
- No complete file-by-file licence scan has been performed. Unknown items remain unverified, not “free of restrictions.”

See [LICENSES.md](./LICENSES.md) and [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md).

## Next audit actions

1. Compare generated output against the current authoritative data and generation configuration.
2. Trace each bundled script, stylesheet, map, icon, logo, and favicon to its upstream source and licence.
3. Run internal-link checks against all generated HTML and separately test external links with sensible rate limits.
4. Run secret scanning and static/security checks suitable for a static HTML publication.
5. Verify the published site in a browser after deployment.
6. Refresh this inventory when the generated tree changes.

## Limitations

This report is reproducible from GitHub tree metadata and the comparison paths above, but it does not contain a complete URL crawl, visual/browser check, security scan, dependency analysis, or legal opinion. Do not report those checks as passed until they are actually run.
