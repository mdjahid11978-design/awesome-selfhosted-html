"""Tests for the read-only repository health audit script."""
import tempfile
import unittest
from pathlib import Path
from scripts.repository_health_audit import audit


class RepositoryHealthAuditTests(unittest.TestCase):
    def write(self, root, path, content):
        """Write content to path under root, creating parent dirs as needed."""
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def test_reports_missing_local_target_and_preserves_branding(self):
        """Audit should flag a missing local link/anchor while keeping branding checks passing."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("README.md", "BRANDING.md", "JAHIDS_AI_ALIGNMENT.md"):
                self.write(root, name, "JAHIDS.AI Sovereign AI Platform\nBuilt by Jahid\n")
            for name in ("MAINTENANCE.md", "LICENSES.md", "THIRD_PARTY_NOTICES.md", "ASSET_PROVENANCE.md"):
                self.write(root, name, "docs")
            self.write(root, "index.html", '<a href="missing.html">missing</a><a href="page.html#ok">ok</a><a href="#no-such-id">bad anchor</a>')
            self.write(root, "page.html", '<h1 id="ok">ok</h1>')
            report, markdown = audit(root)
            self.assertEqual(report["required_files"]["status"], "PASS")
            self.assertEqual(report["canonical_identity"]["status"], "PASS")
            self.assertTrue(any("MISSING LOCAL TARGET" in x for x in report["findings"]))
            self.assertIn("MISSING LOCAL ANCHOR", markdown)

    def test_detects_unsafe_path_escape(self):
        """Audit should flag local references that escape the repository root."""
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name in ("README.md", "BRANDING.md", "JAHIDS_AI_ALIGNMENT.md"):
                self.write(root, name, "JAHIDS.AI Sovereign AI Platform\nBuilt by Jahid\n")
            for name in ("MAINTENANCE.md", "LICENSES.md", "THIRD_PARTY_NOTICES.md", "ASSET_PROVENANCE.md"):
                self.write(root, name, "docs")
            self.write(root, "index.html", '<a href="../outside.html">escape</a>')
            report, _ = audit(root)
            self.assertTrue(any("UNSAFE LOCAL REFERENCE" in x for x in report["findings"]))


if __name__ == "__main__":
    unittest.main()
