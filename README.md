# KiCad-Library

The parts catalogue of the OpenDrone hardware line: every symbol, footprint
and 3D model here is used on a board that has been through a real assembly
run, so it is sourced, footprinted and reflow-proven. Its job is lookup, not
enforcement. Board repos keep their own local libraries and nothing requires
a part to live here first.

## Repository layout

| Path | Contents |
|---|---|
| `symbol/Incutec.kicad_sym` | 41 symbols, one library, nickname `Incutec` |
| `footprint/Incutec.pretty/` | 143 footprints |
| `3dmodel/` | 244 model files (129 STEP, 115 WRL). Footprints reference the WRL set; the STEP set is the MCAD counterpart |
| `PARTS-USED.md` | Every LCSC part used on a manufactured board, and which boards use it |
| `tools/build-parts-index.py` | Regenerates `PARTS-USED.md`; `--check` audits membership |
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

**As a checkout.** Clone the repo, then in KiCad set a path variable
`OPENDRONE_LIB` (Preferences > Configure Paths) to the checkout directory.
Footprint 3D paths resolve through it. Add the libraries per project or
globally:

```text
(lib (name "Incutec")(type "KiCad")(uri "${OPENDRONE_LIB}/symbol/Incutec.kicad_sym")(options "")(descr "OpenDrone parts catalogue"))
(lib (name "Incutec")(type "KiCad")(uri "${OPENDRONE_LIB}/footprint/Incutec.pretty")(options "")(descr "OpenDrone parts catalogue"))
```

**For a board design, copy out.** Board repos copy the symbol, footprint and
3D model into their own `lib` libraries rather than referencing this one: a
board keeps working when the catalogue changes. No OpenDrone board references
`Incutec:` directly.

### Path contract (do not break)

Footprint 3D model paths are written as `${OPENDRONE_LIB}/3dmodel/<file>`.
`tools/build-pcm.py` rewrites them to the KiCad third-party directory when
packaging. Keep new footprints on the same form.

## Updating the library

1. Edit here, following [CONTRIBUTING.md](CONTRIBUTING.md).
2. Commit, push, PR to `main`.
3. After a merge that changes library content, rebuild and publish the
   package: `python3 tools/build-pcm.py <version>`, commit `pcm/`, then
   `gh release create pcm-v<version> dist/OpenDrone-KiCad-Library_<version>.zip`.

## Rules

**Membership.** A symbol, footprint or 3D model belongs here only if it is used
on a board whose repo is at `status-alpha` or beyond. Alpha means the board was
manufactured, so everything here has been through a real assembly run. Parts
that exist only on a planned or in-progress design do not qualify, however good
they look on paper. When a board reaches alpha, its parts join.

**Check before you trust it.** `python3 tools/build-parts-index.py --check`
reports every symbol whose part is on no manufactured board, every symbol with
no LCSC number, and every manufactured part still missing from the library.
Run it after any change here and after any board reaches alpha.

## Contributing

Authoring rules for library edits (editing method, naming, property names, pre-PR validation) are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Licensed under [CERN-OHL-S-2.0](https://ohwr.org/cern_ohl_s_v2.txt), the same license as the boards. See [LICENSE](LICENSE).

## Revisions

- **2026-08-14**: pruned to the membership rule: 41 symbols, 143 footprints,
  244 models remain, all on manufactured boards or awaiting an LCSC number.
  3D paths recontracted from the removed submodule layout to
  `${OPENDRONE_LIB}`. First PCM package published. `tools/bump-all.sh`
  deleted with the submodule model.
- **2026-08-04**: library assembled by merging the per-project board libraries: 105 symbols, 195 footprints, full 3D model set. LCSC property unified to `LCSC`, verified FC redraws adopted (`ESP32-C3FH4`, `SX1281IMLTRT`). `tools/bump-all.sh` fixed to commit via pathspec.
- **2026-06-29**: initial `Incutec.kicad_sym` from the OpenRX lineage (21 symbols).
