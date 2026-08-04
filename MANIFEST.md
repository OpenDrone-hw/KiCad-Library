# Merge manifest, 2026-08-04

How `Incutec.kicad_sym` (105 symbols) and `Incutec.pretty` (195 footprints) were
assembled from the per-project libraries in the OpenDrone working dir. Recorded so
every collision decision is auditable and reversible.

## Sources

| Pool | Source | Contributed |
|---|---|---|
| canon-RF | this repo's pre-merge `Incutec.kicad_sym` (built Jul 2026 from OpenRX lineage) | 21 symbols |
| FC | `OpenFC-Lite/hardware/lib.kicad_sym` + `lib.pretty` | 83 symbols, 84 footprints |
| ESC | `4in1-mini/hardware/components.kicad_sym` + `4in1ESC.pretty` | 7 symbols, 22 footprints |
| ESC30 | `4in1/hardware/4in1ESC-30x30.pretty` (footprints only) | 2 extra footprints |
| RF | `OpenRX/shared/libs/OpenRX-Shared.pretty` + `.3dshapes` | 23 footprints |
| RF+ | `AntAIO/shared/libs/OpenRX-Shared.pretty` (6 extra footprints) | DFN-8, IND-SMD, LGA-14, SOD-923, VQFN-15, WSON-8 |
| whoop | `OpenAIO-Whoop/hardware/whoop.pretty` (Bluejay ESC parts) | 13 footprints |
| sourced | `Charger/hardware/libs/sourced.kicad_sym` + `sourced.pretty` | 5 symbols, 66 footprints |
| kicad-std | KiCad 10 bundled `Package_DFN_QFN` | 1 footprint (QFN-32-1EP 5x5) + 8 passive 3D models |

All `Footprint` properties rewritten to the `Incutec:` nickname. All 3D model paths
rewritten to `${KIPRJMOD}/../libs/KiCad-Library/3dmodel/<file>`.

## Verified non-drift

Before merging, every copy of every family lib was compared per-symbol and
per-footprint with UUIDs normalized out:

- `OpenRX-Shared.kicad_sym`: 4 copies (OpenRX, AntAIO, OpenAIO, OpenAIO-Whoop),
  all 20 symbols content-identical. Byte diffs were UUID churn only.
- `components.kicad_sym`: 4 copies, identical except the footprint lib nickname
  (`4in1ESC` vs `4in1ESC-30x30`), which the rewrite unifies.
- `lib.kicad_sym` (FC family): OpenFC-Lite-Mini's 17 and OpenAIO's 17 are exact
  content subsets of OpenFC-Lite's 83.

So no project's local library disagreed with any other in electrical content,
with the exceptions below.

## Symbol collisions (11)

Ten RF symbols existed in both canon-RF and the FC lib. Nine differ only in the
LCSC property name (`LCSC Part` in canon vs `LCSC` in FC). Kept canon.

Two have real drawing differences (FC redrew them in Jun 2026: centered
properties, changed pin label geometry; electrically equivalent):

- `ESP32-C3FH4`: kept canon-RF drawing, FC alternate exists
- `SX1281IMLTRT`: kept canon-RF drawing, FC alternate exists

`LMR51420YDDCR` existed in ESC and FC pools; kept FC (newer).

Follow-up: unify the LCSC property name across all 105 symbols in one pass
(pick one of `LCSC` / `LCSC Part` / `LCSC Part #` based on what the BOM tooling
and Fabrication Toolkit expect).

## Footprint collisions (kept newest by mtime, all logged)

FC evolved several RF-family footprints after they were copied (example:
`QFN-32_L5.0-W5.0-P0.50-TL-EP3.7` gained an extended pad 24). Newest won:

- FC version won over RF: ANT-SMD_47948-0001, ANT-SMD_L3.2-W1.6,
  CRYSTAL-SMD_4P-L1.6-W1.2-BL, FILTER-SMD_4P-L1.0-W0.5-L,
  LED-SMD_4P-L1.0-W1.0-TL_XL-1010RGBC-WS2812B, LGA-14_L3.0-W2.5-P0.50-TL,
  OSC-SMD_4P-L2.0-W1.6-BL_TXC_7Z, QFN-24_L4.0-W4.0-P0.50-TL-EP2.6,
  QFN-32_L5.0-W5.0-P0.50-BL-EP3.7, QFN-32_L5.0-W5.0-P0.50-TL-EP3.7,
  RF-SMD_FRF05002-JSS103M, SW-SMD_4P-L3.0-W2.0-P0.85-LS3.5,
  WSON-8_L2.0-W2.0-P0.50-TL-EP, WSON-8_L6.0-W5.0-P1.27-BL-EP,
  SOT-23-6_L2.9-W1.6-P0.95-LS2.9-BL, SOT-23-3/5 variants (over Charger sourced)
- RF (OpenRX) version won: QFN-12_EP_2x2_Pitch0.5mm, QFN-16_L3.0-W3.0-P0.50-BL-EP1.7
- ESC version won: JST_SM08B-SRSS-TB (over 4in1's copy)
- whoop version won: X2SON-4_L1.0-W1.0-P0.65-TL-EP
- sourced version won: SOT-23-6_L2.9-W1.6-P0.95-LS2.8-BR

If a board's next revision shows an unexpected footprint change against its frozen
local lib, check this list first.

## Validation

- `kicad-cli sym export svg`: all 105 symbols parsed and exported
- `kicad-cli fp upgrade` on a copy: all 195 footprints parsed clean
- All 179 referenced 3D models present in `3dmodel/` (8 pulled from KiCad bundled)

## Not merged (deliberate)

- `OpenFC-Lite-rev1/hardware/lib.kicad_sym` (82 syms): legacy rev, superseded
- `4in1-mini/20x20-ESC-QC/ESC-QC.*`: QC fixture tooling, stays project-local
- `Incutec-Business-Card/IBCard/lib`: art project, empty symbol lib
- `OpenAIO/hardware/imports.kicad_sym`, `OpenAIO-Whoop/hardware/whoop.kicad_sym`:
  empty symbol files
- Frozen local libs in each repo: left untouched by design (see README rules)
