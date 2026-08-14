# Contributing

## Talk to us first

Before you open an issue, start a project, or write any code or CAD, bring the
idea to the Discord server and tag the developers:

https://discord.gg/v3sWmTcx3R

Say what you want to change and why. Someone may already be working on it, the
board may be held by another contributor, or the change may clash with a
production run that is already committed. A short conversation there saves a
pull request that cannot be merged.

## Setup

```
git clone https://github.com/OpenDrone-hw/KiCad-Library.git
```

No submodules; boards copy parts out of this catalogue rather than referencing it. Use KiCad 10.

## What belongs here

Parts we have actually used on a board. This library mirrors reality, it does
not lead it. Draw parts in the board repo first; promote a part here once the
board is real, so the library stays a trustworthy answer to "have we used this
before".

Do not add a symbol for every value of a passive. If you need to know which
capacitors or resistors we already use, read [PARTS-USED.md](PARTS-USED.md),
which is generated from the board schematics and needs no library symbol.

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

After a PR merges, republish the PCM package: see [Updating the library](README.md#updating-the-library).

## Documentation

Docs state current fact only: no TODOs, no plans, no aspirational content.

## Licensing

Contributions are licensed under CERN-OHL-S-2.0, the same license as the project.

## Questions

Open a GitHub issue.
