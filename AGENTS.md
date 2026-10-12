# KiCad-Library

Shared parts catalogue of the OpenDrone hardware line: symbols, footprints, 3D models and datasheets, pinned by board repositories as `hardware/KiCad-Library`.

Validate: `python3 tools/check-datasheets.py && python3 tools/build-parts-index.py --check`

## Boundaries

- Never text-edit `.kicad_sym` or `.kicad_mod`: use the KiCad editors, or kicad-skip / the pcbnew API with KiCad closed.
- `PARTS-USED.md` is generated only by `tools/build-parts-index.py`; `pcm/` only by `tools/build-pcm.py`, in a release commit.
- `tools/build-parts-index.py` rewrites files and ignores unknown arguments; it finds board repositories only as siblings of this checkout.

## Pointers

- Layout, path contract, authoring rules: `README.md`
