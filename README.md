# KiCad-Library

The parts catalogue of the OpenDrone hardware line: every physical symbol
links to an exact datasheet, and every symbol, footprint and 3D model here is
used on a board that has been through a real assembly run. Datasheets also
cover the important ICs of boards that have not reached assembly yet. Its
job is lookup, not enforcement. Board repos pin this repository and keep only
parts that have not yet qualified in their local libraries.

## Repository layout

| Path | Contents |
|---|---|
| `symbol/OpenDrone.kicad_sym` | 54 symbols, one library, nickname `OpenDrone` |
| `footprint/OpenDrone.pretty/` | 145 footprints |
| `3dmodel/` | 246 model files (130 STEP, 116 WRL). Footprints reference the WRL set; the STEP set is the MCAD counterpart |
| `datasheet/manifest.json` | Committed record of every datasheet: file, source URL, SHA-256, symbols, parts, boards |
| `datasheet/*.pdf` | Local PDF store, git-ignored; rebuilt by `tools/fetch-datasheets.py` |
| `PARTS-USED.md` | Every LCSC part used on a manufactured board, and which boards use it |
| `ALTERNATES.md` | Second sources for the FETs and gate drivers, grouped by land pattern and pinout |
| `tools/build-parts-index.py` | Regenerates `PARTS-USED.md`; `--check` audits membership |
| `tools/check-datasheets.py` | Verifies symbol coverage, paths and manifest schema; checks PDF signatures and SHA-256 of local PDFs (`--require-local` fails on missing ones) |
| `tools/fetch-datasheets.py` | Downloads every manifest PDF missing locally and verifies SHA-256 (`--check` only reports) |
| `tools/build-pcm.py` | Builds the KiCad PCM package and repository metadata |
| `pcm/` | The PCM repository files KiCad reads |

## Usage

**As a KiCad package (easiest).** Preferences > Plugin and Content Manager >
Manage repositories, add:

```text
https://raw.githubusercontent.com/OpenDrone-hw/KiCad-Library/main/pcm/repository.json
```

Install "OpenDrone KiCad Library" from the Libraries tab. KiCad places the
content in its third-party directory and registers the libraries with a
`PCM_` prefix.

**In a board repo.** Every repo started from
[hardware-template](https://github.com/OpenDrone-hw/hardware-template) carries
this library as the git submodule `hardware/KiCad-Library`, pinned to a commit,
with the project's `OPENDRONE_LIB` text variable pointing at it. Parts place
straight from the `OpenDrone` library; `git submodule update --remote` pulls a
newer catalogue in. How to set that up and update it is in the org
[CONTRIBUTING](https://github.com/OpenDrone-hw/.github/blob/main/CONTRIBUTING.md).

**As a checkout.** Clone the repo, then in KiCad set a path variable
`OPENDRONE_LIB` (Preferences > Configure Paths) to the checkout directory.
Footprint 3D paths resolve through it. Add the libraries per project or
globally:

```text
(lib (name "OpenDrone")(type "KiCad")(uri "${OPENDRONE_LIB}/symbol/OpenDrone.kicad_sym")(options "")(descr "OpenDrone parts catalogue"))
(lib (name "OpenDrone")(type "KiCad")(uri "${OPENDRONE_LIB}/footprint/OpenDrone.pretty")(options "")(descr "OpenDrone parts catalogue"))
```

### Path contract (do not break)

Footprint 3D model paths are written as `${OPENDRONE_LIB}/3dmodel/<file>` and
symbol datasheet fields as `${OPENDRONE_LIB}/datasheet/<file>.pdf`. Board repos
define `OPENDRONE_LIB` as a project text variable, checkouts as a KiCad path
variable, and `tools/build-pcm.py` rewrites both prefixes to KiCad's third-party
directories when packaging. Keep new library items on those forms.

## Updating the library

1. Edit here, following the [rules](#rules).
2. Commit, push, PR to `main`.
3. After a merge that changes library content, rebuild and publish the
   package: `python3 tools/build-pcm.py <version>`, commit `pcm/`, then
   `gh release create pcm-v<version> dist/OpenDrone-KiCad-Library_<version>.zip`.

## Rules

**Membership.** Every reusable, datasheet-bearing component used on a board
whose repo is at `status-alpha` or beyond belongs here. Alpha means the board
was manufactured, so everything here has been through a real assembly run.
Parts that exist only on a planned or in-progress design do not qualify,
however good they look on paper. When a board reaches alpha, its ICs,
semiconductors, sensors, connectors and other non-generic parts join; ordinary
R/C/L/LED primitives remain in KiCad's standard libraries.

**Datasheets.** Two scopes, different gates.

- Symbols, footprints and 3D models: only parts used on a board at
  `status-alpha` or beyond (the membership rule above).
- Datasheets: every important component used on any OpenDrone board, at any
  status. Important means ICs, MCUs, RF parts, regulators, drivers, MOSFETs,
  protection and power diodes, sensors, connectors with custom footprints and
  crystals or TCXOs. Generic R/C/L, ferrites, signal diodes and LEDs are not
  stored (the WS2812 RGB LED is a driver IC and is).

PDFs are git-ignored. `datasheet/manifest.json` is the committed record and
`python3 tools/fetch-datasheets.py` rebuilds the local store on any machine.
A family PDF serves several parts and is stored once. Every custom symbol for an
orderable physical component maps to one manifest entry through `symbols`; set
its `Datasheet` field to `${OPENDRONE_LIB}/datasheet/<file>.pdf`. Virtual or
interface symbols need an explicit `exempt_symbols` entry. Product repositories
do not duplicate these PDFs.

Manifest schema (`datasheet/manifest.json`, `documents` keyed by PDF filename):

| Field | Required | Meaning |
|---|---|---|
| `symbols` | yes (may be `[]`) | Library symbol names that link to this PDF |
| `parts` | no | Manufacturer part numbers covered, spelled as in the board BOM |
| `boards` | no | Board repository names that use any of those parts |
| `source_url` | yes | Where `tools/fetch-datasheets.py` downloads it |
| `sha256` | yes | SHA-256 of the exact PDF |

Each entry needs at least one of `symbols` or `parts`. Parts without a
datasheet in the manifest are listed in the pull request that added the
store, not in the manifest.

**Check before you trust it.** `python3 tools/build-parts-index.py --check`
reports every symbol whose part is on no manufactured board, every symbol with
no LCSC number, every intentionally unpromoted generic primitive, and every
datasheet-bearing manufactured part still missing from the library. Missing
non-generic parts fail the check. Run it after any change here and after any
board reaches alpha.

**Authoring.** Edit symbols and footprints in the KiCad editors, or scripted
via kicad-skip or the pcbnew API; never text-edit `.kicad_sym` or `.kicad_mod`
files. Footprint references inside symbols use the `OpenDrone:` nickname, the
LCSC part number property is named `LCSC`, and 3D model paths follow the
[path contract](#path-contract-do-not-break). Do not add a symbol for every
value of a passive: [PARTS-USED.md](PARTS-USED.md) already answers which
resistors and capacitors we use. Validate before opening a PR:

```sh
kicad-cli sym export svg symbol/OpenDrone.kicad_sym -o /tmp/symcheck
kicad-cli fp upgrade /tmp/fpcheck   # on a copy of footprint/OpenDrone.pretty
python3 tools/fetch-datasheets.py   # once per machine; --check to only report
python3 tools/check-datasheets.py

# every OpenDrone: footprint ref in the symbol lib resolves to a committed .kicad_mod
comm -23 <(grep -o '"OpenDrone:[^"]*"' symbol/OpenDrone.kicad_sym | tr -d '"' | sed 's/OpenDrone://' | sort -u) \
         <(ls footprint/OpenDrone.pretty | sed 's/\.kicad_mod$//' | sort)
# prints nothing when clean. kicad-cli does not flag a dangling footprint ref, so run this too
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Licensed under [CERN-OHL-S-2.0](https://ohwr.org/cern_ohl_s_v2.txt), the same license as the boards. See [LICENSE](LICENSE).
Third-party PDFs retain their publishers' copyrights and notices.

## Revisions

- **2026-10-13**: datasheet PDFs are git-ignored and rebuilt from
  `datasheet/manifest.json` by `tools/fetch-datasheets.py`. The manifest now also
  records `parts` and `boards`, and covers the important ICs of every OpenDrone
  board, not only alpha boards. The symbol, footprint and 3D model membership
  rule is unchanged.

- **2026-09-01**: exact component PDFs moved into the shared catalogue, linked
  through `OPENDRONE_LIB`, hash-checked by a manifest and included in PCM builds.
  The alpha-board audit then promoted every remaining datasheet-bearing part:
  54 symbols now map 53 physical components to 46 deduplicated PDFs, with one
  virtual exemption. The membership check fails when a future manufactured
  non-generic part is missing; 71 ordinary R/C/L/LED primitives remain outside
  the catalogue by design.
- **2026-08-15**: library nickname and files renamed `Incutec` to `OpenDrone`
  (`symbol/OpenDrone.kicad_sym`, `footprint/OpenDrone.pretty`). PCM package
  1.1.0. Board repos now carry the library as a pinned submodule from the
  template.
- **2026-08-14**: pruned to the membership rule: 41 symbols, 143 footprints,
  244 models remain, all on manufactured boards or awaiting an LCSC number.
  3D paths recontracted from the removed submodule layout to
  `${OPENDRONE_LIB}`. First PCM package published. `tools/bump-all.sh` <!-- pointer-check: skip -->
  deleted with the submodule model.
- **2026-08-04**: library assembled by merging the per-project board libraries: 105 symbols, 195 footprints, full 3D model set. LCSC property unified to `LCSC`, verified FC redraws adopted (`ESP32-C3FH4`, `SX1281IMLTRT`). `tools/bump-all.sh` fixed to commit via pathspec. <!-- pointer-check: skip -->
- **2026-06-29**: initial `Incutec.kicad_sym` from the OpenRX lineage (21 symbols).
