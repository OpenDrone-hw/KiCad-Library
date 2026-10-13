#!/usr/bin/env python3
"""Rebuild the local datasheet PDF store from datasheet/manifest.json.

Datasheet PDFs are git-ignored; the manifest (file, source URL, SHA-256) is
the committed record. Run from anywhere with system python3, no extra deps.

  python3 tools/fetch-datasheets.py           download every missing PDF
  python3 tools/fetch-datasheets.py --check   report only, download nothing

A PDF that is already present with the right SHA-256 is never touched. A
present PDF with a wrong hash is reported and never overwritten. A download
that is not a PDF or has a wrong hash is discarded. Exit 1 on any mismatch,
dead URL or (with --check) missing file; exit 0 otherwise.
"""

import hashlib
import json
import pathlib
import ssl
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATASHEETS = ROOT / "datasheet"
MANIFEST = DATASHEETS / "manifest.json"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
CA_FALLBACKS = ("/etc/ssl/cert.pem", "/etc/ssl/certs/ca-certificates.crt")


def ssl_context():
    """Default context; python.org builds on macOS ship without CA roots."""
    context = ssl.create_default_context()
    if not context.cert_store_stats().get("x509_ca") and not ssl.get_default_verify_paths().cafile:
        for candidate in CA_FALLBACKS:
            if pathlib.Path(candidate).is_file():
                return ssl.create_default_context(cafile=candidate)
    return context


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def download(url, context):
    request = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,*/*"}
    )
    with urllib.request.urlopen(request, timeout=90, context=context) as response:
        return response.read()


def main():
    check_only = "--check" in sys.argv[1:]
    documents = json.loads(MANIFEST.read_text())["documents"]
    context = ssl_context()
    counts = {"present": 0, "fetched": 0, "missing": 0, "bad_hash": 0, "failed": 0}
    problems = []

    for filename, entry in sorted(documents.items()):
        path = DATASHEETS / filename
        expected = entry.get("sha256", "")
        if path.is_file():
            if sha256(path.read_bytes()) == expected:
                counts["present"] += 1
            else:
                counts["bad_hash"] += 1
                problems.append(f"SHA-256 mismatch (kept, not overwritten): {filename}")
            continue
        if check_only:
            counts["missing"] += 1
            problems.append(f"missing locally: {filename}")
            continue
        url = entry.get("source_url", "")
        try:
            data = download(url, context)
        except (urllib.error.URLError, OSError, ValueError) as error:
            counts["failed"] += 1
            problems.append(f"download failed: {filename}: {url}: {error}")
            continue
        if not data.startswith(b"%PDF-"):
            counts["failed"] += 1
            problems.append(f"not a PDF (blocked or dead URL): {filename}: {url}")
        elif sha256(data) != expected:
            counts["bad_hash"] += 1
            problems.append(
                f"downloaded file has a different SHA-256 (discarded, publisher "
                f"updated the document?): {filename}: {url}"
            )
        else:
            path.write_bytes(data)
            counts["fetched"] += 1
            print(f"fetched {filename}")

    for problem in problems:
        print(f"  - {problem}")
    print(
        f"datasheet fetch {'check ' if check_only else ''}summary: "
        f"{len(documents)} manifest entries, {counts['present']} present and verified, "
        f"{counts['fetched']} fetched, {counts['missing']} missing, "
        f"{counts['bad_hash']} hash mismatches, {counts['failed']} failed"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
