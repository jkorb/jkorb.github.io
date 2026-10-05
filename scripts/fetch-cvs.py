#!/usr/bin/env python3
"""Add the four Dropbox CV releases to a Hugo build (Python standard library)."""

import argparse
import json
from pathlib import Path
import subprocess
import tempfile


def fetch_cvs(destination):
    manifest = Path(__file__).resolve().parents[1] / "data/cv.json"
    cvs = json.loads(manifest.read_text())
    destination.mkdir(parents=True, exist_ok=True)
    # Validate every download before replacing any existing CV.
    with tempfile.TemporaryDirectory(prefix=".cvs-", dir=destination) as staging:
        for language, cv in cvs.items():
            download = Path(staging) / (language + ".pdf")
            subprocess.run([
                "curl", "--fail", "--location", "--retry", "3",
                "--connect-timeout", "15", "--max-time", "120",
                "--silent", "--show-error", cv["source"],
                "--output", str(download),
            ], check=True)
            data = download.read_bytes()
            if not (data.startswith(b"%PDF-") and b"%%EOF" in data[-1024:]):
                raise ValueError(f"The {language} CV download is not a complete PDF")
        for language, cv in cvs.items():
            output = destination / cv["path"]
            output.parent.mkdir(parents=True, exist_ok=True)
            (Path(staging) / (language + ".pdf")).replace(output)
            print(f"Added {language} CV: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", nargs="?", type=Path, default=Path("public"))
    fetch_cvs(parser.parse_args().destination)
