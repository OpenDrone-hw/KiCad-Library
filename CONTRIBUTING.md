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
- 3D model paths must follow the [path contract](README.md#path-contract-do-not-break), with the model files committed to `3dmodel/`.
- The LCSC part number property is named `LCSC`.
- Validate before opening a PR:

```sh
kicad-cli sym export svg symbol/Incutec.kicad_sym -o /tmp/symcheck
kicad-cli fp upgrade /tmp/fpcheck   # on a copy of footprint/Incutec.pretty

# every Incutec: footprint ref in the symbol lib resolves to a committed .kicad_mod
comm -23 <(grep -o '"Incutec:[^"]*"' symbol/Incutec.kicad_sym | tr -d '"' | sed 's/Incutec://' | sort -u) \
         <(ls footprint/Incutec.pretty | sed 's/\.kicad_mod$//' | sort)
# prints nothing when clean. kicad-cli does not flag a dangling footprint ref, so run this too
```

After a PR merges, re-pin the consuming repos: see [Updating the library](README.md#updating-the-library).

## Documentation

Docs state current fact only: no TODOs, no plans, no aspirational content.

## Licensing

Contributions are licensed under CERN-OHL-S-2.0, the same license as the project.

## Questions

Open a GitHub issue.
