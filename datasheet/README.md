# Datasheets

This directory pins the exact component documents linked from the shared KiCad
symbols. A board repository gets the same files by pinning this repository as a
submodule; it must not keep duplicate component PDFs in its own tree.

`manifest.json` is the source of truth. It maps every physical shared symbol to
one committed PDF and records the source URL and SHA-256 digest. A document may
cover several symbols, so family datasheets are stored only once. Virtual
symbols are listed explicitly under `exempt_symbols`.

Every reusable, datasheet-bearing component from a `status-alpha`,
`status-beta` or `status-launched` board belongs in the shared catalogue and in
this manifest. Generic R/C/L/LED primitives use KiCad's standard libraries and
do not need entries here. `python3 tools/build-parts-index.py --check` enforces
that distinction against all manufactured boards.

Run `python3 tools/check-datasheets.py` after adding or replacing a document.
PDFs retain their publishers' copyrights and notices; the repository hardware
license does not replace the terms embedded in those documents.
