#!/usr/bin/env python3
"""Read-only integrity audit for the generated HTML site and maintainer docs."""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlsplit
from urllib.request import Request, urlopen
import json
import os
import time

REQUIRED = (
    "README.md", "BRANDING.md", "JAHIDS_AI_ALIGNMENT.md", "MAINTENANCE.md",
    "LICENSES.md", "THIRD_PARTY_NOTICES.md", "ASSET_PROVENANCE.md", "index.html",
)
IDENTITY = ("JAHIDS.AI Sovereign AI Platform", "Built by Jahid")


class ReferenceParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.references: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src", "poster", "data"):
            value = attrs.get(key)
            if value:
                self.references.append(value.strip())
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])


def collect_html(root: Path):
    ignored = {".git", ".github", ".venv", "node_modules"}
    return sorted(p for p in root.rglob("*.html")
                  if not any(part in ignored for part in p.relative_to(root).parts))


def audit(root: Path, check_external: bool = False, max_external: int = 80):
    findings: list[str] = []
    missing = [name for name in REQUIRED if not (root / name).is_file()]
    for name in missing:
        findings.append(f"REQUIRED FILE MISSING: {name}")

    docs = []
    for name in ("README.md", "BRANDING.md", "JAHIDS_AI_ALIGNMENT.md"):
        path = root / name
        if path.is_file():
            docs.append(path.read_text(encoding="utf-8", errors="replace"))
    doc_text = "\n".join(docs)
    identity_ok = all(marker in doc_text for marker in IDENTITY)
    if not identity_ok:
        findings.append("CANONICAL IDENTITY MISSING: expected platform name and attribution in maintainer docs")

    html_files = collect_html(root)
    parsed = {}
    for file in html_files:
        parser = ReferenceParser()
        try:
            parser.feed(file.read_text(encoding="utf-8", errors="replace"))
            parsed[file] = parser
        except OSError as exc:
            findings.append(f"HTML READ ERROR: {file.relative_to(root)}: {exc}")

    local_checked = 0
    external_urls = set()
    for file, parser in parsed.items():
        for ref in parser.references:
            if not ref or ref.startswith(("javascript:", "mailto:", "tel:", "data:")):
                continue
            if ref.startswith("#"):
                anchor = unquote(ref[1:])
                if anchor and anchor not in parser.ids:
                    findings.append(f"MISSING LOCAL ANCHOR: {file.relative_to(root)} -> {ref}")
                continue
            parts = urlsplit(ref)
            if parts.scheme.lower() in ("http", "https"):
                external_urls.add(parts.geturl().split("#", 1)[0])
                continue
            if parts.scheme or parts.netloc or ref.startswith("//"):
                continue
            path = unquote(parts.path)
            if not path:
                continue
            local_checked += 1
            try:
                target = (root / path.lstrip("/")).resolve() if path.startswith("/") else (file.parent / path).resolve()
                target.relative_to(root.resolve())
            except ValueError:
                findings.append(f"UNSAFE LOCAL REFERENCE: {file.relative_to(root)} -> {ref}")
                continue
            if not target.exists():
                # Common directory URLs resolve to their index.html in static sites.
                if target.is_dir() and (target / "index.html").is_file():
                    continue
                findings.append(f"MISSING LOCAL TARGET: {file.relative_to(root)} -> {ref}")
            if parts.fragment and target.is_file() and target.suffix.lower() in (".html", ".htm"):
                target_parser = parsed.get(target)
                if target_parser is None:
                    target_parser = ReferenceParser()
                    try:
                        target_parser.feed(target.read_text(encoding="utf-8", errors="replace"))
                    except OSError:
                        target_parser = None
                if target_parser and unquote(parts.fragment) not in target_parser.ids:
                    findings.append(f"MISSING LOCAL ANCHOR: {file.relative_to(root)} -> {ref}")

    online_results = []
    if check_external:
        urls = sorted(external_urls)[:max_external]
        for url in urls:
            status = "UNKNOWN"
            detail = ""
            try:
                request = Request(url, method="HEAD", headers={"User-Agent": "JAHIDS-AI-Repository-Audit/1.0"})
                with urlopen(request, timeout=8) as response:
                    status = str(response.status)
            except HTTPError as exc:
                if exc.code in (403, 405, 501):
                    try:
                        request = Request(url, headers={"Range": "bytes=0-0", "User-Agent": "JAHIDS-AI-Repository-Audit/1.0"})
                        with urlopen(request, timeout=8) as response:
                            status = str(response.status)
                    except Exception as retry_exc:
                        status, detail = str(exc.code), str(retry_exc)[:180]
                else:
                    status, detail = str(exc.code), str(exc.reason)[:180]
            except (URLError, TimeoutError, OSError) as exc:
                detail = str(exc)[:180]
            online_results.append({"url": url, "status": status, "detail": detail})
            time.sleep(0.15)

    report = {
        "required_files": {"status": "PASS" if not missing else "FAIL", "missing": missing},
        "canonical_identity": {"status": "PASS" if identity_ok else "FAIL"},
        "html_files_inspected": len(html_files),
        "local_references_inspected": local_checked,
        "external_urls_found": len(external_urls),
        "external_urls_checked": len(online_results),
        "external_urls_not_checked_due_to_limit": max(0, len(external_urls) - len(online_results)),
        "external_results": online_results,
        "findings": findings,
        "scope_note": "Read-only checks only. External HTTP statuses can be blocked by hosts/CDNs and are evidence for review, not automatic proof of a broken link. Generated HTML is never rewritten.",
    }
    lines = [
        "# Repository health audit", "",
        f"- Required files: {report['required_files']['status']}",
        f"- Canonical identity: {report['canonical_identity']['status']}",
        f"- HTML files inspected: {len(html_files)}",
        f"- Local references inspected: {local_checked}",
        f"- Missing/unsafe local references and anchors: {len(findings) - len(missing) - (0 if identity_ok else 1)}",
        f"- External URLs found: {len(external_urls)}",
        f"- External URLs checked: {len(online_results)}",
        "", "## Findings",
    ]
    lines.extend(f"- {x}" for x in findings[:500] or ["None"])
    lines += ["", "## External URL results", ""]
    lines.extend(f"- [{x['status']}] {x['url']}" + (f" — {x['detail']}" if x["detail"] else "") for x in online_results)
    lines += ["", report["scope_note"], ""]
    return report, "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--report", type=Path, default=Path("repository-health-report.md"))
    parser.add_argument("--json-report", type=Path, default=Path("repository-health-report.json"))
    parser.add_argument("--check-external", action="store_true")
    parser.add_argument("--max-external", type=int, default=80)
    args = parser.parse_args()
    root = args.root.resolve()
    report, markdown = audit(root, args.check_external, max(0, args.max_external))
    args.report.write_text(markdown, encoding="utf-8")
    args.json_report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write(markdown)
    print(markdown)
    if report["required_files"]["status"] != "PASS" or report["canonical_identity"]["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
