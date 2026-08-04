# KiCad-Library

Canonical shared KiCad library for all incutec hardware. Symbols, footprints, and 3D
models for every product family: OpenRX receivers, OpenFC flight controllers, OpenESC
4in1 ESCs, OpenAIO, Whoop, Charger.

- `symbol/Incutec.kicad_sym` - 105 symbols, one library, nickname `Incutec`
- `footprint/Incutec.pretty/` - 195 footprints
- `3dmodel/` - WRL + STEP models referenced by the footprints

License: CERN-OHL-S-2.0 (same as the boards).

## Usage: git submodule, project-local tables. No global libraries.

Every consuming repo pins this library as a submodule at a fixed path:

```
<repo>/
├─ .gitmodules                  # pins incutec-hw/KiCad-Library
├─ libs/KiCad-Library/          # the submodule
└─ hardware/                    # KiCad project, one level below repo root
   ├─ <board>.kicad_pro
   ├─ sym-lib-table             # project-local, references the submodule
   └─ fp-lib-table
```

Add it to a repo:

```sh
git submodule add https://github.com/incutec-hw/KiCad-Library.git libs/KiCad-Library
```

Project-local table entries (KiCad: Preferences -> Manage Symbol/Footprint Libraries
-> Project Specific, or edit the tables directly):

```
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

Footprint 3D model paths are written as
`${KIPRJMOD}/../libs/KiCad-Library/3dmodel/<file>`. This resolves only when:

1. the submodule lives at `<repo>/libs/KiCad-Library`, and
2. the KiCad project directory sits exactly one level below the repo root
   (`hardware/`, or a named project dir like `OpenRX-Lite/`).

All current repos follow this. Keep new ones on the same shape (see
`_template/CONVENTIONS.md` in the OpenDrone working dir).

## Updating the library

1. Edit here (KiCad symbol/footprint editors pointed at this checkout, or scripted).
2. Commit, push, PR to `main`.
3. Bump the pin in consuming repos: `tools/bump-all.sh` from the directory that
   contains the hardware repos updates and commits every submodule pin.

Repos always build against their pinned commit. Nothing changes under a board
until its pin is bumped, so a library edit can never silently alter a released design.

## Rules

- New parts go here and only here. Do not create new project-local symbol or
  footprint files in board repos.
- Existing boards still carry frozen pre-consolidation local libs
  (`OpenRX-Shared`, `lib`, `components`, `4in1ESC*`, `whoop`, `sourced`). Those are
  historical record for already-routed boards. Do not add to them. Migrate a board
  to `Incutec:` references only during a deliberate revision pass, with ERC/DRC
  before and after (see MANIFEST.md for drift notes).
- Footprint refs inside symbols use the `Incutec:` nickname.
- Validate before pushing:

```sh
kicad-cli sym export svg symbol/Incutec.kicad_sym -o /tmp/symcheck
kicad-cli fp upgrade /tmp/fpcheck   # on a copy of footprint/Incutec.pretty
```

## Provenance

Built 2026-08-04 by merging the per-project libraries. Full source mapping, the
collision list, and the two symbols with known alternate drawings are in
[MANIFEST.md](MANIFEST.md).
