# KiCad-Library

Shared parts catalogue of the OpenDrone hardware line: one symbol library,
one footprint library, the 3D models, and the exact datasheet PDF for every
physical symbol. Board repositories pin it as the submodule
`hardware/KiCad-Library` under the nickname `OpenDrone`. This is a library,
not a board: there is no schematic, no ERC and no DRC here.

[README.md](README.md) is the human guide. It owns the layout table, the
usage modes, the path contract and the membership, datasheet and authoring
rules. Do not restate them; follow them.

## What an agent may change

- Symbols in `symbol/OpenDrone.kicad_sym` and footprints in
  `footprint/OpenDrone.pretty/`, through the KiCad editors or kicad-skip and
  the pcbnew API. Never text-edit `.kicad_sym` or `.kicad_mod`. Close KiCad
  before a scripted write.
- Models in `3dmodel/`, referenced from footprints as
  `${OPENDRONE_LIB}/3dmodel/<file>`.
- PDFs in `datasheet/` and their entries in `datasheet/manifest.json`.
- `PARTS-USED.md` only through `tools/build-parts-index.py`; `pcm/` only
  through `tools/build-pcm.py`. Both files are generated.
- `ALTERNATES.md` by hand, keeping its verified and screened distinction.

A part joins the catalogue only when a board that uses it is at
`status-alpha` or beyond. A part on a planned design stays in that board's
local `lib`; promotion here is its own reviewed pull request.

## Tools

All three run with system `python3` from the repository root and take no
`--help`: an unknown argument is ignored, and two of them write files.

| Command | Effect |
|---|---|
| `python3 tools/build-parts-index.py` | Rewrites `PARTS-USED.md` from the `.kicad_sch` files of every board repository checked out next to this one (it scans the parent directory, so it finds nothing from an isolated clone). Board stage comes from the `status-*` GitHub topic through `gh`, cached in `tools/.status-cache.json` for offline runs. |
| `python3 tools/build-parts-index.py --check` | Same, then exits 1 when a symbol is on no manufactured board, a symbol has no `LCSC` property, or a manufactured non-generic part is missing from the catalogue. |
| `python3 tools/check-datasheets.py` | Verifies that every physical symbol maps to one PDF in the manifest, that each PDF exists, is a PDF, and matches its SHA-256. |
| `python3 tools/build-pcm.py <version>` | Writes `dist/OpenDrone-KiCad-Library_<version>.zip` (git-ignored) and rewrites `pcm/packages.json` and `pcm/repository.json`. With no argument it uses `1.0.0`. |

## Validation

Before every pull request, from the repository root:

```sh
python3 tools/check-datasheets.py
python3 tools/build-parts-index.py --check   # from a checkout next to the board repos
```

plus the symbol, footprint and dangling-reference checks in the README
"Authoring" rule. A change to `pcm/` or `dist/` belongs only in a release
commit.

## By task

- Add a part from LCSC: confirm a board at `status-alpha` or beyond uses it (`PARTS-USED.md`, or the board's schematic). Bring the symbol, footprint and models from that board's `hardware/lib*` into the KiCad editors here; set the symbol's Footprint to `OpenDrone:<footprint>`, the LCSC number in a property named `LCSC`, and the model path to `${OPENDRONE_LIB}/3dmodel/<file>`. Then add the datasheet (next task) and run the checks.
- Add a datasheet: copy the PDF to `datasheet/<file>.pdf`, add a `documents` entry in `datasheet/manifest.json` with `symbols`, `source_url` and `sha256` (`shasum -a 256 datasheet/<file>.pdf`), set each listed symbol's `Datasheet` field to `${OPENDRONE_LIB}/datasheet/<file>.pdf`, run `python3 tools/check-datasheets.py`. A virtual symbol goes under `exempt_symbols` instead.
- Update `PARTS-USED.md`: from a checkout next to the board repositories run `python3 tools/build-parts-index.py --check`, read the four counts it prints, commit the regenerated file. Never edit it by hand.
- Run the checks: the two commands under Validation, then the `kicad-cli` and `comm` lines in the README "Authoring" rule.
- Publish a package after a merge that changed library content: `python3 tools/build-pcm.py <version>`, commit `pcm/`, then `gh release create pcm-v<version> dist/OpenDrone-KiCad-Library_<version>.zip`. Only on request.
- Answer "which boards use part X": read the `Boards` column of `PARTS-USED.md`; for second sources read `ALTERNATES.md` and order only against a verified row.
