#!/usr/bin/env python3
"""Exercise CV download validation without network access."""

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('fetch_cvs', Path(__file__).with_name('fetch-cvs.py'))
fetcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetcher)
CVS = json.loads((Path(__file__).resolve().parents[1] / 'data/cv.json').read_text())
PDF = b'%PDF-1.7\nfixture\n%%EOF\n'


class DownloadTests(unittest.TestCase):
    def run_fixture(self, invalid=None, fail=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for cv in CVS.values():
                target = root / cv['path']
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(b'existing CV')

            def download(command, check):
                self.assertTrue(check)
                source = command[-3]
                self.assertIn(source, [cv['source'] for cv in CVS.values()])
                if source == CVS['it']['source'] and fail:
                    raise subprocess.CalledProcessError(22, command)
                data = invalid if source == CVS['it']['source'] and invalid is not None else PDF
                Path(command[-1]).write_bytes(data)

            with patch.object(fetcher.subprocess, 'run', side_effect=download):
                if fail or invalid is not None:
                    with self.assertRaises((ValueError, subprocess.CalledProcessError)):
                        fetcher.fetch_cvs(root)
                else:
                    fetcher.fetch_cvs(root)
            for cv in CVS.values():
                self.assertEqual((root / cv['path']).read_bytes(), b'existing CV' if fail or invalid is not None else PDF)
            self.assertEqual(list(root.glob('.cvs-*')), [])

    def test_success(self):
        self.run_fixture()

    def test_html_error_does_not_replace_existing_cvs(self):
        self.run_fixture(invalid=b'<html>Login required</html>')

    def test_truncated_pdf_does_not_replace_existing_cvs(self):
        self.run_fixture(invalid=b'%PDF-1.7\nincomplete')

    def test_network_error_does_not_replace_existing_cvs(self):
        self.run_fixture(fail=True)


if __name__ == '__main__':
    unittest.main()
