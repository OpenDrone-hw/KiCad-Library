# Datasheets

`manifest.json` is the committed record of every component datasheet used on an
OpenDrone board: file name, source URL, SHA-256, the library symbols that link
to it (`symbols`), the manufacturer part numbers it covers (`parts`) and the
board repositories that use them (`boards`). The PDFs themselves are git-ignored.

Rebuild the local PDF store on any machine:

```sh
python3 tools/fetch-datasheets.py           # download missing PDFs, verify SHA-256
python3 tools/fetch-datasheets.py --check   # report only
```

A family document is stored once and lists every part it covers. Virtual
symbols are listed under `exempt_symbols`. Scope and the full schema are in the
repository README, "Datasheets".

Run `python3 tools/check-datasheets.py` after editing the manifest. PDFs retain
their publishers' copyrights and notices; the repository hardware license does
not replace the terms embedded in those documents.
