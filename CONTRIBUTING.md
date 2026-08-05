# Contributing

## Setup

```
git clone https://github.com/incutec-hw/KiCad-Library.git
```

No submodules here; this repo is the submodule the board repos pin. Use KiCad 10.

## Workflow

- `main` is protected. Work on a feature branch and open a pull request.
- Edit symbols and footprints in the KiCad editors, or scripted via kicad-skip or the pcbnew API. Never text-edit `.kicad_sym` or `.kicad_mod` files.
- Footprint references inside symbols use the `Incutec:` nickname.
- 3D model paths must be `${KIPRJMOD}/../libs/KiCad-Library/3dmodel/<file>`, with the model files committed to `3dmodel/`.
- The LCSC part number property is named `LCSC`.
- Validate before opening a PR:

```
kicad-cli sym export svg symbol/Incutec.kicad_sym -o /tmp/symcheck
kicad-cli fp upgrade /tmp/fpcheck   # on a copy of footprint/Incutec.pretty
```

After a PR merges, re-pin the consuming repos with `tools/bump-all.sh`, run from the directory that contains the hardware repos.

## Documentation

Docs state current fact only: no TODOs, no plans, no aspirational content.

## Licensing

Contributions are licensed under CERN-OHL-S-2.0, the same license as the project.

## Questions

Open a GitHub issue.
