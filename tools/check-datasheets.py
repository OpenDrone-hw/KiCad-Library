#!/usr/bin/env python3
"""Verify committed datasheets and their shared-symbol mappings."""

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
    errors = []
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
        if not path.is_file():
            errors.append(f"missing document: {filename}")
            continue
        data = path.read_bytes()
        if not data.startswith(b"%PDF-"):
            errors.append(f"not a PDF: {filename}")
        digest = hashlib.sha256(data).hexdigest()
        if digest != entry.get("sha256"):
            errors.append(f"SHA-256 mismatch: {filename}")
        if digest in digests:
            errors.append(f"duplicate PDFs: {digests[digest]} and {filename}")
        digests[digest] = filename
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
    print(
        f"datasheet check passed: {len(mapped)} physical symbols, "
        f"{len(documents)} unique PDFs, {len(exemptions)} explicit exemption"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

