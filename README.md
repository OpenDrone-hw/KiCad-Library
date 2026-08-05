# KiCad-Library

Shared KiCad library for the incutec OpenDrone hardware line. One symbol library, one footprint library, and a full 3D model set cover every product family: OpenRX receivers, OpenFC flight controllers, OpenESC 4-in-1 ESCs, OpenAIO, Whoop, Charger. Board repos consume it as a pinned git submodule through project-local lib tables, so a library edit never silently alters a released design.

## Status

**Live**, canonical since 2026-08-04, assembled by merging the per-project board libraries. Full source mapping, collision decisions, and validation record: [MANIFEST.md](MANIFEST.md). Revision history: [CHANGELOG.md](CHANGELOG.md).

## Repository layout

| Path | Contents |
|---|---|
| `symbol/Incutec.kicad_sym` | 105 symbols, one library, nickname `Incutec` |
| `footprint/Incutec.pretty/` | 195 footprints |
| `3dmodel/` | 336 model files (175 STEP, 161 WRL) referenced by the footprints |
| `tools/bump-all.sh` | Re-pins the submodule in every consuming repo |
| `MANIFEST.md` | Merge provenance: sources, collisions, validation |

## Usage

Git submodule plus project-local lib tables. No global libraries. Every consuming repo pins this library at a fixed path:

```text
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

1. Edit here with the KiCad symbol/footprint editors pointed at this checkout, or scripted (kicad-skip, pcbnew API). Never text-edit `.kicad_*` files.
2. Commit, push, PR to `main`.
3. Bump the pin in consuming repos: run `tools/bump-all.sh` from the directory that contains the hardware repos. It updates and commits every submodule pin.

Repos always build against their pinned commit. Nothing changes under a board until its pin is bumped.

## Rules

- New parts go here and only here. Do not create new project-local symbol or footprint files in board repos.
- Existing boards still carry frozen pre-consolidation local libs (`OpenRX-Shared`, `lib`, `components`, `4in1ESC*`, `whoop`, `sourced`). Those are historical record for already-routed boards. Do not add to them. Migrate a board to `Incutec:` references only during a deliberate revision pass, with ERC/DRC before and after (see [MANIFEST.md](MANIFEST.md) for drift notes).
- Footprint refs inside symbols use the `Incutec:` nickname.
- The LCSC part number property is named `LCSC`, nothing else.
- Validate before pushing:

```sh
kicad-cli sym export svg symbol/Incutec.kicad_sym -o /tmp/symcheck
kicad-cli fp upgrade /tmp/fpcheck   # on a copy of footprint/Incutec.pretty
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Licensed under [CERN-OHL-S-2.0](https://ohwr.org/cern_ohl_s_v2.txt), the same license as the boards. See [LICENSE](LICENSE).
