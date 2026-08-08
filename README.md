# KiCad-Library

Reference library for the incutec OpenDrone hardware line: a semi-maintained
mirror of parts we have already used and stocked. Its job is lookup, not
enforcement. If a part is here, we have shipped it on a board, so it is
already sourced and footprinted and reusing it is cheaper than drawing
something new.

Local project libraries are the working default for board design. Nothing
requires a part to live here first.

## Status

**Live**, mirror role since 2026-08-06. Assembled 2026-08-04 from the
per-project libraries; footprints and symbols upgraded to KiCad 10 format
from Bastian's branch 2026-08-06.

Open question, being settled in person: whether board repos keep the submodule
copy or point at one shared clone through an environment variable. No board
currently references `Incutec:`, so nothing depends on the answer yet.

## Repository layout

| Path | Contents |
|---|---|
| `symbol/Incutec.kicad_sym` | 105 symbols, one library, nickname `Incutec` |
| `footprint/Incutec.pretty/` | 195 footprints |
| `3dmodel/` | 336 model files (175 STEP, 161 WRL). Footprints reference the WRL, plus 19 STEP; the rest of the STEP set is the MCAD counterpart |
| `tools/bump-all.sh` | Re-pins the submodule in every consuming repo |
| `PARTS-USED.md` | Every LCSC part used on a board, and which boards use it |
| `tools/build-parts-index.py` | Regenerates `PARTS-USED.md` from the schematics |

## Usage

Git submodule plus project-local lib tables. No global libraries. Every consuming repo pins this library at a fixed path:

```text
<repo>/
├─ .gitmodules                  # pins OpenDrone-hw/KiCad-Library
├─ libs/KiCad-Library/          # the submodule
└─ hardware/                    # KiCad project, one level below repo root
   ├─ <board>.kicad_pro
   ├─ sym-lib-table             # project-local, references the submodule
   └─ fp-lib-table
```

Add it to a repo:

```sh
git submodule add https://github.com/OpenDrone-hw/KiCad-Library.git libs/KiCad-Library
```

Project-local table entries (KiCad: Preferences -> Manage Symbol/Footprint Libraries -> Project Specific, or edit the tables directly):

```text
(lib (name "Incutec")(type "KiCad")(uri "${KIPRJMOD}/../libs/KiCad-Library/symbol/Incutec.kicad_sym")(options "")(descr "incutec shared library"))
(lib (name "Incutec")(type "KiCad")(uri "${KIPRJMOD}/../libs/KiCad-Library/footprint/Incutec.pretty")(options "")(descr "incutec shared library"))
```

Cloning a consuming repo:

```sh
git clone --recursive <repo-url>
# or, after a plain clone:
git submodule update --init
```

### Path contract (do not break)

Footprint 3D model paths are written as `${KIPRJMOD}/../libs/KiCad-Library/3dmodel/<file>`. This resolves only when:

1. the submodule lives at `<repo>/libs/KiCad-Library`, and
2. the KiCad project directory sits exactly one level below the repo root (`hardware/`, or a named project dir like `OpenRX-Lite/`).

All current repos follow this. Keep new ones on the same shape.

## Updating the library

1. Edit here, following [CONTRIBUTING.md](CONTRIBUTING.md).
2. Commit, push, PR to `main`.
3. Bump the pin in consuming repos: run `tools/bump-all.sh` from the directory that contains the hardware repos. It updates and commits every submodule pin.

Repos always build against their pinned commit. Nothing changes under a board until its pin is bumped.

## Rules

- New parts go here and only here. Do not create new project-local symbol or footprint files in board repos.
- Existing boards still carry frozen pre-consolidation local libs (`OpenRX-Shared`, `lib`, `components`, `4in1ESC*`, `whoop`, `sourced`). Those are the historical record for already-routed boards. Do not add to them. Migrate a board to `Incutec:` references only during a deliberate revision pass, with ERC/DRC before and after.

## Contributing

Authoring rules for library edits (editing method, naming, property names, pre-PR validation) are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Licensed under [CERN-OHL-S-2.0](https://ohwr.org/cern_ohl_s_v2.txt), the same license as the boards. See [LICENSE](LICENSE).

## Revisions

- **2026-08-04**: library assembled by merging the per-project board libraries: 105 symbols, 195 footprints, full 3D model set. LCSC property unified to `LCSC`, verified FC redraws adopted (`ESP32-C3FH4`, `SX1281IMLTRT`). `tools/bump-all.sh` fixed to commit via pathspec.
- **2026-06-29**: initial `Incutec.kicad_sym` from the OpenRX lineage (21 symbols).
