# Agent notes

Facts for AI agents working in this repo.

- Library repo, no KiCad project. Contents: `symbol/Incutec.kicad_sym` (105 symbols), `footprint/Incutec.pretty/` (195 footprints), `3dmodel/` (336 STEP/WRL files), `tools/bump-all.sh`.
- Board repos pin this repo as a git submodule at `libs/KiCad-Library` and reference it via project-local lib tables. 3D model paths are `${KIPRJMOD}/../libs/KiCad-Library/3dmodel/<file>`; renaming or moving files breaks every consumer.
- Never edit `.kicad_sym` or `.kicad_mod` files as text. Use the KiCad editors, kicad-skip, or the pcbnew API.
- Footprint refs inside symbols use the `Incutec:` nickname. The LCSC property is named `LCSC`.
- Validation:

```
kicad-cli sym export svg symbol/Incutec.kicad_sym -o /tmp/symcheck
kicad-cli fp upgrade /tmp/fpcheck   # on a copy of footprint/Incutec.pretty
```

- After merging to `main`, re-pin consumers: `tools/bump-all.sh` from the directory containing the hardware repos.
- Merge provenance and collision decisions live in `MANIFEST.md`; keep it updated when importing parts from board repos.
- Docs are deterministic: current fact only, no TODOs or plans.
- `main` is protected; push feature branches and open PRs.
