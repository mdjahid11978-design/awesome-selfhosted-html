# Awesome-Selfhosted HTML

A fork of the generated HTML publication for [Awesome-Selfhosted](https://awesome-selfhosted.net/).

[**View the published site**](https://mdjahid11978-design.github.io/awesome-selfhosted-html/)

## Repository map

| Resource | Purpose |
| --- | --- |
| This fork | https://github.com/mdjahid11978-design/awesome-selfhosted-html |
| Published site | https://mdjahid11978-design.github.io/awesome-selfhosted-html/ |
| Upstream HTML project | https://github.com/awesome-selfhosted/awesome-selfhosted-html |
| Catalogue and project overview | https://github.com/awesome-selfhosted/awesome-selfhosted |
| Catalogue data and build instructions | https://github.com/awesome-selfhosted/awesome-selfhosted-data |
| Published branch | `gh-pages` |

This repository is a **fork of the upstream HTML publication repository**. Its `gh-pages` branch contains generated HTML and static assets. It is not the authoritative source for catalogue data or the upstream site generator.

## What the project contains

The upstream Awesome-Selfhosted project catalogues free software network services and web applications that can be hosted on your own servers. This repository publishes a generated HTML view of that catalogue.

- Browse the [published site](https://mdjahid11978-design.github.io/awesome-selfhosted-html/).
- Consult the [upstream HTML project](https://github.com/awesome-selfhosted/awesome-selfhosted-html) for generated site output.
- Consult the [upstream catalogue](https://github.com/awesome-selfhosted/awesome-selfhosted) and [data repository](https://github.com/awesome-selfhosted/awesome-selfhosted-data) for catalogue content and contribution rules.

## Provenance, licensing, and third-party material

This is a fork. It includes inherited and generated upstream content and must not be presented as wholly original work.

The upstream catalogue README identifies the **catalogue/list** as licensed under Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0). See the [upstream licence](https://github.com/awesome-selfhosted/awesome-selfhosted/blob/master/LICENSE) and [Creative Commons licence terms](https://creativecommons.org/licenses/by-sa/3.0/).

That statement is scoped to the catalogue/list; it is **not** a blanket licence for every HTML file, stylesheet, script, logo, icon, font, or third-party asset. Review relevant upstream source, file-specific notices, and applicable terms before reuse or redistribution. The [upstream authors list](https://github.com/awesome-selfhosted/awesome-selfhosted-data/blob/master/AUTHORS) provides catalogue contributor attribution.

See:
- [LICENSES.md](./LICENSES.md) — confirmed licence scope and treatment of unverified files.
- [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md) — provenance and attribution notes.
- [ASSET_PROVENANCE.md](./ASSET_PROVENANCE.md) — dated tree comparison, asset categories, and remaining audit actions.
- [MAINTENANCE.md](./MAINTENANCE.md) — safe workflow for generated pages.

Rules for this fork:
- Preserve upstream copyright, attribution, and licence notices.
- Do not claim inherited work as original or imply upstream endorsement.
- Follow attribution and ShareAlike terms for material actually covered by CC BY-SA 3.0.
- A catalogue entry does not grant rights to a listed project's name, logo, code, or assets.
- Do not add a root-level licence purporting to relicense all inherited content without a documented rights review.

## JAHIDS.AI engineering alignment

[JAHIDS_AI_ALIGNMENT.md](./JAHIDS_AI_ALIGNMENT.md) records intended engineering alignment with JAHIDS.AI. It does not change upstream identity, transfer third-party rights, replace applicable licences, or imply ownership of the upstream project.

## Maintenance and verification

Prefer fixing catalogue data or generation configuration in the upstream source project and regenerating HTML rather than editing generated pages directly. The upstream data repository's Makefile describes `export_html` and `push_html`; the latter pushes generated output to the upstream HTML repository. Generated pages may be replaced wholesale during regeneration. Read [MAINTENANCE.md](./MAINTENANCE.md) before synchronizing output.

A successful Pages deployment proves that GitHub Pages processed the branch; it does not prove every link works, every asset's licence is verified, or the site passed a security review. The outstanding checks are listed in [ASSET_PROVENANCE.md](./ASSET_PROVENANCE.md).

---

This README documents the fork and its relationship to upstream projects. Upstream authorship, third-party rights, and applicable licences remain with their respective rightsholders.
