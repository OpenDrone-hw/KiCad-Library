#!/usr/bin/env python3
"""Verify the datasheet manifest, symbol mappings and any local PDFs.

PDFs are git-ignored (tools/fetch-datasheets.py rebuilds them). A missing local
PDF is reported but does not fail unless --require-local is given. A present PDF
must still be a PDF with the manifest SHA-256.
"""

import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SYMBOL_LIBRARY = ROOT / "symbol" / "OpenDrone.kicad_sym"
DATASHEETS = ROOT / "datasheet"
MANIFEST = DATASHEETS / "manifest.json"
PROPERTY = re.compile(r'\(property "([^"]+)" "([^"]*)"')


def symbol_properties(text):
    """Return top-level symbol name -> property dictionary."""
    symbols = {}
    for match in re.finditer(r'^\t\(symbol "([^"]+)"', text, re.MULTILINE):
        start = match.start()
        depth = 0
        quoted = False
        escaped = False
        for index in range(start, len(text)):
            char = text[index]
            if quoted:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    quoted = False
                continue
            if char == '"':
                quoted = True
            elif char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0:
                    symbols[match.group(1)] = dict(PROPERTY.findall(text[start:index]))
                    break
    return symbols


def main():
    require_local = "--require-local" in sys.argv[1:]
    errors = []
    missing = []
    manifest = json.loads(MANIFEST.read_text())
    documents = manifest.get("documents", {})
    exemptions = manifest.get("exempt_symbols", {})
    symbols = symbol_properties(SYMBOL_LIBRARY.read_text())
    mapped = {}
    digests = {}

    for filename, entry in documents.items():
        path = DATASHEETS / filename
        if pathlib.Path(filename).name != filename or not filename.endswith(".pdf"):
            errors.append(f"invalid document filename: {filename}")
            continue
        expected = entry.get("sha256", "")
        if len(expected) != 64 or expected in digests:
            errors.append(
                f"duplicate PDFs: {digests[expected]} and {filename}"
                if expected in digests
                else f"invalid SHA-256 in manifest: {filename}"
            )
        digests[expected] = filename
        if not (entry.get("symbols") or entry.get("parts")):
            errors.append(f"entry names no symbols or parts: {filename}")
        for key in ("symbols", "parts", "boards"):
            if key in entry and not (
                isinstance(entry[key], list) and all(isinstance(v, str) for v in entry[key])
            ):
                errors.append(f"{key} must be a list of strings: {filename}")
        if not path.is_file():
            missing.append(filename)
            if require_local:
                errors.append(f"missing document: {filename}")
        else:
            data = path.read_bytes()
            if not data.startswith(b"%PDF-"):
                errors.append(f"not a PDF: {filename}")
            if hashlib.sha256(data).hexdigest() != expected:
                errors.append(f"SHA-256 mismatch: {filename}")
        if not entry.get("source_url", "").startswith(("https://", "http://")):
            errors.append(f"missing source URL: {filename}")
        for symbol in entry.get("symbols", []):
            if symbol in mapped:
                errors.append(f"symbol mapped twice: {symbol}")
            mapped[symbol] = filename

    expected_pdfs = set(documents)
    actual_pdfs = {path.name for path in DATASHEETS.glob("*.pdf")}
    for filename in sorted(actual_pdfs - expected_pdfs):
        errors.append(f"unlisted PDF: {filename}")
    for symbol in sorted(set(mapped) - set(symbols)):
        errors.append(f"manifest names missing symbol: {symbol}")
    for symbol in sorted(set(exemptions) - set(symbols)):
        errors.append(f"exemption names missing symbol: {symbol}")
    for symbol in sorted(set(mapped) & set(exemptions)):
        errors.append(f"symbol is mapped and exempt: {symbol}")
    for symbol in sorted(set(symbols) - set(mapped) - set(exemptions)):
        errors.append(f"physical symbol has no datasheet mapping: {symbol}")

    for symbol, filename in sorted(mapped.items()):
        expected = f"${{OPENDRONE_LIB}}/datasheet/{filename}"
        actual = symbols.get(symbol, {}).get("Datasheet", "")
        if actual != expected:
            errors.append(f"{symbol}: Datasheet is {actual!r}, expected {expected!r}")

    if errors:
        print("datasheet check failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    if missing:
        print(
            f"note: {len(missing)} of {len(documents)} PDFs are not stored locally "
            "(git-ignored); run python3 tools/fetch-datasheets.py"
        )
    print(
        f"datasheet check passed: {len(mapped)} physical symbols, "
        f"{len(documents)} manifest entries, {len(documents) - len(missing)} PDFs verified locally, "
        f"{len(exemptions)} explicit exemption"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

