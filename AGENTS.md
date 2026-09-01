# OpenDrone KiCad library

This repository contains shared KiCad symbols, footprints, models, and pinned
component datasheets. Follow
[`../AGENTS.md`](../AGENTS.md). Keep library items deterministic and reusable;
verify pin numbering, pad geometry, courtyard, fabrication data, and model
alignment against authoritative component documentation. Every orderable
physical symbol must map to one exact PDF in `datasheet/manifest.json`; generic
passives use KiCad's standard libraries and virtual symbols need an explicit
exemption. Run the repository's library checks and inspect dependent design
impact before reporting completion.
