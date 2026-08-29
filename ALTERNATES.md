# Alternates

Second sources for OpenDrone parts, grouped by the only thing that makes a
swap possible: one land pattern, one pinout, one function. A part listed here
fits the copper. Whether it fits the *board* is the second half of each
section, and that half disqualifies most candidates.

Nothing here is fitted. The fitted part is named at the top of each class and
is the only one that has been through an assembly run. Promoting an alternate
is a board change: datasheet read, stencil check, bench run, in that order.

Verified means the pinout or the parameter was read out of the manufacturer
datasheet. Screened means it came from a distributor parametric field and
nobody has opened the datasheet. Do not order against a screened row.

**Judge a package by its measured body, not its name.** Every vendor names its
own eight-lead power package and the names do not map onto each other:
Toshiba SOP Advance, Vishay PowerPAK SO-8, Infineon SuperSO8, Nexperia LFPAK56
and a generic PDFN5x6 are all the same size class. Whether one lands on our
copper is arithmetic on the datasheet drawing, not a question about the name,
and the answer for the 5x6 class is in that section.

MOSFET stock and price are JLCPCB parts API, checked 2026-08-29, at the 1000
break unless the row says otherwise. Gate driver rows are LCSC at 2026-08-27.
They move.

## Power MOSFET, DFN 5x6

Used on OpenESC-30x30, Q1-Q24, 24 per board.
Land pattern `4in1ESC-30x30:PDFN-8L_L6.0-W5.0-P1.27`: two rows of four leads
0.58 x 1.08 mm at y +/-2.83, so pads spanning y 2.29 to 3.37, 1.27 mm pitch,
plus a 4.4 x 4.1 mm drain pad centred at y -0.69. Pins 1-3 source, 4 gate,
5-8 drain.

Fitted: **SP40N01GHNK**, C22385416.

**The fitted part has two datasheet revisions under one part number, and they
disagree about the two parameters that decide this whole section.**

| | Ver-1.0 | Ver-1.1 |
|---|---|---|
| EAS | 490 mJ | 1089 mJ |
| RthJC | 1.27 C/W | 0.96 C/W |
| PD | 98 W | 130 W |
| Qg typ | 119 nC | 126 nC |

Both documents are internally self-consistent, so this is a real silicon or
process change that Siliup shipped without touching the MPN. That is exactly
the case where a reorder silently returns the older die. **Confirm the
revision against the reel date code before treating 1089 mJ as the bar.** The
table below is ranked against Ver-1.1. If Ver-1.0 is what ships, every row
from TPHR8504PL down improves relative to it.

Verified 2026-08-29. Every row read from the manufacturer datasheet.

| Part | Vendor | LCSC | Package, body mm | VDSS | RDS(on) max @10V | Qg @10V | EAS | RthJC | Stock | $@1k |
|---|---|---|---|---|---|---|---|---|---|---|
| SP40N01GHNK (fitted) | Siliup | C22385416 | PDFN5x6 | 40 V | 1.5 mOhm | 126 nC typ | 1089 mJ | 0.96 | 1632 | 0.331 |
| NCEP40T15AGU | NCE Power | C5119012 | DFN5X6-8L 4.90 x 6.00 | 40 V | 1.5 mOhm | 62 nC | 1620 mJ | 0.93 | 4017 | 0.490 |
| PSMN1R4-40YLD | Nexperia | C458253 | LFPAK56 4.9 x 6.0 | 40 V | 1.4 mOhm | 143 max | 1641 mJ | 0.56 | 802 | 0.315 |
| TPHR8504PL | Toshiba | C22388172 | SOP Advance, see note | 40 V | 0.85 mOhm | 103 nC | 336 mJ | 0.88 | 37632 | 0.517 |
| HYG009N04LS1C2 | Huayi | C2890387 | PDFN5x6-8L 5.20 x 6.15 | 40 V | 0.96 mOhm | 89 nC | 780 mJ | 2.0 | 14231 | 0.425 |
| XRS225N04LF | XinRui | C50314145 | PDFN-8L 5x6 | 40 V | 1.0 mOhm | 118 nC | 627 mJ | 1.1 | 1896 | 0.316 |
| NCEP40T13GU | NCE Power | C191993 | DFN5X6-8L 4.90 x 6.00 | 40 V | 2.3 mOhm | 70 max | 600 mJ | 1.56 | 7226 | 0.339 |
| CJAC200SN04U | JSCJ Changjing | C19268993 | PDFNWB5x6-8L | 40 V | 0.90 mOhm | 124 nC | 760 mJ | 1.2 | 1381 | 0.707 |
| APG013N04G | ALLPOWER | C5443733 | PDFN5x6-8L 5.10 x 6.05 | 40 V | 1.3 mOhm | 30 nC | 473 mJ | 1.9 | 3630 | 0.344 |
| BSC010N04LS6 | Infineon | C7220836 | SuperSO8 5.15 x 6.15 | 40 V | 1.0 mOhm | 83 max | 376 mJ | 1.0 | 4705 | 0.535 |
| DON160N04T | Doingter | C50386321 | DFN5x6 clip 5.20 x 6.05 | 40 V | 1.6 mOhm | 66 nC | 200 mJ | 1.5 | 2804 | 0.297 |

**EAS in mJ is not comparable across vendors.** Test inductance in this table
spans 18 uH to 0.5 mH, a 28x range, and energy scales with L at fixed current.
Back-computing avalanche current from EAS = 0.5 L I^2 is the honest
comparison, and it reorders the table:

| Part | IAS |
|---|---|
| TPHR8504PL | 120 A stated |
| NCEP40T15AGU | 80.5 A |
| HYG009N04LS1C2 | 72.1 A |
| SP40N01GHNK (fitted) | 66.0 A |
| DON160N04T | 63.2 A |
| XRS225N04LF | 56.0 A |
| CJAC200SN04U | 55.1 A |
| NCEP40T13GU | 49.0 A |
| APG013N04G | 43.5 A |

PSMN1R4-40YLD is the only part in the class publishing an avalanche curve
rather than a single point: 1641 mJ at ID 25 A and 446 mJ at ID 74 A, IAS
190 A, 100% tested.

**The gate is avalanche, not RDS(on).** OpenESC-30x30 has no input clamp. The
avalanche-rated FET *is* the overvoltage backstop, by design
(`OpenDrone-Testing/Tests/ESC/ESC-17-overvoltage-rationale.md`). 8S charged is
33.6 V against a 40 V part, so avalanche capability is the margin.

**30 V parts do not belong on this board.** 8S charged is above their
breakdown. A 30 V part is a valid alternate only if the board is re-rated to
6S. The 40 V floor is what buys 8S in the first place.

**Gate charge is not the binding constraint, and an earlier revision of this
file said it was.** The fitted part is 126 nC typ, not the ~70 nC previously
recorded here. The real arithmetic: 24 FETs x 126 nC x 24 kHz = 72.6 mA, so
the board already spends 12.1% of the LMR54406's 0.6 A rail on gate charge and
works. The worst part in the table, PSMN1R4-40YLD at 143 nC max, is 82.4 mA or
13.7%. Nothing here loads the rail meaningfully harder than what is fitted.
Driver dissipation and edge rate still move with Qg; rail headroom does not.

### Land pattern: almost everything in this size class fits

The reference drain land is 4.4 x 4.1 mm, larger than the fitted part's own
exposed pad at 4.01 x 3.48, so it has margin to spare. Computed from each
datasheet's own overall length, lead length and exposed pad, against pads
spanning y 2.29 to 3.37:

| Part | Lead y-span | Exposed pad |
|---|---|---|
| SP40N01GHNK (fitted) | 2.39-3.02 | 4.01 x 3.48 |
| NCEP40T15AGU | 2.39-3.00 | 3.81 x 3.58 |
| TPHR8504PL 2-5W1A | 2.40-3.05 | 4.21 x 3.69 |
| TPHR8504PL 2-5Q1S | 2.20-3.00 | 4.25 x 3.50 |
| DON160N04T | 2.38-3.02 | 4.00 x 4.10 |
| HYG009N04LS1C2 | 2.48-3.08 | 4.10 x 3.77 |
| JMSH0401AGQ | 2.38-3.08 | 4.10 x 3.53 |
| AGM403A1 | 2.39-3.08 | 4.01 x 3.48 |

**Nexperia LFPAK56 is the one genuine footprint outlier.** It is a copper clip
package with four gullwing leads on one side plus a drain tab, not an 8-lead
DFN. PSMN1R4-40YLD needs a second footprint and its own copper pour.

Three parts overrun a 5.2 x 6.2 window at maximum material condition and their
courtyards must be drawn to MMC, not nominal: HYG009N04LS1C2 (5.4 x 6.35),
JMSH0401AGQ (5.4 x 6.25) and XRS225N04LF (5.4 x 6.15).

**TPHR8504PL: one MPN, two packages.** Toshiba ships it as either 2-5Q1S
(SOP Advance, 5.0 x 6.0 overall, gullwing) or 2-5W1A (SOP Advance(N),
5.15 x 6.10 overall, flat lead). Both land on our pattern, per the table above,
so the ambiguity is not a blocker here, but the part number does not determine
what arrives and a stencil check has to cover both. Its V(BR)DSS is also
specified at ID = 10 mA, looser than the 250 uA every Chinese vendor in the
table uses, and V(BR)DSX collapses to 25 V min at VGS = -20 V.

### What actually beats the fitted part

**NCEP40T15AGU.** Higher avalanche current at an identical L = 0.5 mH test
condition, the only like-for-like avalanche comparison available. Half the gate
charge, marginally better RthJC, same RDS(on) max, lands on the existing
copper. Costs $3.81 more per board. 4017 pieces is 167 boards, so it has to be
reserved before a batch, not after.

**PSMN1R4-40YLD** is the strongest technical answer to what this board actually
fails at: copper clip with solder die attach, Rth(j-mb) 0.56 against the fitted
0.96, and the most rigorously characterised avalanche behaviour in the class.
It is currently cheaper than the fitted part. It is held back by 802 pieces and
by being the one real footprint job.

Note the fitted part is down to 1632 pieces, 68 boards. That is the near-term
constraint regardless of what this section concludes.

Not checked for any part in this class: repetitive avalanche EAR/IAR ratings,
AEC-Q101 status, MSL and reflow profile, and body-diode reverse recovery under
this board's real di/dt. Datasheet Qrr is measured at 100 A/us, likely
optimistic here.

## Power MOSFET, DFN 3x3

Used on OpenESC-20x20, Q1-Q24, 24 per board.
Land pattern `Package_SON:Diodes_PowerDI3333-8` (KiCad global library, not the
project library). Four lead pads 0.7 x 0.42 mm at x -1.5 on 0.65 mm pitch
(three source, one gate), four matching pads at x +1.5 for the drain leads, and
a 1.71 x 1.71 mm drain tab at x +0.455. The four drain-lead pads carry no pad
number in that footprint, so KiCad gives them no net: they solder to the part
but are invisible to DRC.

Fitted: **DOY180N03T**, C49441966, 30 V.

Verified 2026-08-29. AON7140, APG035N04Q and SP40N03GNJ were verified in the
2026-08-27 pass from datasheets in `OpenESC-20x20/hardware/datasheets/` and
their stock and price columns were not re-pulled, so those three are older than
the rest of the table.

| Part | Vendor | LCSC | Package, body mm | VDSS | RDS(on) @10V | Qg @10V | EAS | RthJC | Stock | $ |
|---|---|---|---|---|---|---|---|---|---|---|
| DOY180N03T (fitted) | Doingter | C49441966 | TDFN3333-8PL 3.30 x 3.30 | 30 V | 1.0 typ / 1.2 max | 39.8 nC | 100 mJ | 0.33, see note | 1815 | 0.184 @5k |
| DOY170N04T | Doingter | C50386319 | TDFN3333-8PL 3.30 x 3.30 | 40 V | 1.7 typ / 2.2 max | 39.8 nC | 200 mJ | 0.70 | 2437 | 0.286 |
| JMSL0302AU | JieJie JJM | C2890409 | PDFN3x3-8L 3.28 x 3.33 | 30 V | 1.2 typ / 1.5 max | 39 nC | 101 mJ | 2.5 max | 4680 | 0.157 @500 |
| IQE013N04LM6 | Infineon | C3289346 | PG-TSON-8-4 3.30 x 3.30 | 40 V | 1.1 typ / 1.35 max | 55 max | 255 mJ | 1.4 max | 90 | 1.582 |
| BSZ018N04LS6 | Infineon | C534643 | PG-TSDSON-8 FL 3.30 x 3.30 | 40 V | 1.6 typ / 1.8 max | 31 nC | 189 mJ | 1.8 max | 93 | 1.073 |
| AON7418 | Alpha & Omega | C74384 | DFN3.3x3.3, see note | 30 V | 1.4 typ / 1.7 max | 65 max | 109 mJ | 1.5 max | 483 | 0.341 |
| NCEP4065QU | NCE Power | C502974 | DFN3.3x3.3-8L 3.35 x 3.30 | 40 V | 2.2 typ / 2.8 max | 34.8 nC | 500 mJ | 2.3 | 1910 | 0.346 |
| TPN2R304PL | Toshiba | C5802634 | TSON Advance, see note | 40 V | 1.8 typ / 2.3 max | 41 nC | 39 mJ | 1.43 | 2595 | 0.457 |
| PTQ10HN03B | HT JinYu | C49384054 | PDFN3333 3.15 x 3.05 | 30 V | 3.1 typ / 4.0 max | 55 nC | 163 mJ | 2.31 | 4670 | 0.069 |
| XRS80N04D | XinRui | C50314143 | PDFN3333-8L 3.15 x 3.30 | 40 V | 3.4 typ / 4.5 max | 32 nC | 125 mJ | 1.9 max | 3025 | 0.102 |
| AON7140 | Alpha & Omega | C2758662 | DFN3x3 | 40 V | 1.9 typ / 2.3 max | 42 typ / 60 max | 135 mJ | not read | 2131 | 0.491 |
| APG035N04Q | ALLPOWER | C5443653 | PDFN3x3 | 40 V | 2.8 typ / 3.5 max | 20.3 nC | 100 mJ | 2.42 | 1436 | 0.143 |
| SP40N03GNJ | Siliup | C22466709 | PDFN3x3 | 40 V | 2.9 typ | 26 nC | 169 mJ | 2.27 | 958 | 0.111 @5k |
| PSMN3R3-40MSH | Nexperia | none | LFPAK33 (SOT1210), see note | 40 V | 2.6 typ / 3.3 max | 42 max | 200 mJ | 1.48 max | not listed | n/a |

Body dimensions not read from a mechanical drawing, so the package column is
screened for these three: **AON7418**, whose datasheet contains no package
outline drawing at all (the 3.3 x 3.3 is a page-1 label); **TPN2R304PL**, taken
from Toshiba's package designation; and **PTQ10HN03B**, whose name refers to
the 3.30 x 3.30 lead span, not the 3.15 x 3.05 body. PTQ10HN03B also publishes
two different bottom-view pad options under one package name with no statement
of which one ships.

EAS test conditions differ here as they do in the 5x6 class. AON7140 is at
L 0.3 mH and IAS 30 A, softer than the 0.5 mH the Doingter and NCE parts use,
so the mJ figures are not directly comparable.

**DOY170N04T is the only zero-work change in this class.** Same vendor, same
TDFN3333-8PL drawing symbol for symbol as the fitted part, so it drops onto the
existing land pattern. It doubles EAS to 200 mJ and buys 8S headroom, at
2.2 mOhm max against 1.2, roughly +83% conduction loss per FET.

**JMSL0302AU is the natural qualified second source.** 1.5 mOhm max against the
fitted 1.2 at the same 39 nC, with 2.6x the stock at 60% of the price and an
honestly published thermal number. It stays 30 V, so it does nothing for cell
count.

Every 40 V row costs conduction loss. The trade is cell count, since 30 V VDSS
is what caps OpenESC-20x20 and OpenAIO at 6S. Take a 40 V part only if the
board is being re-rated, and re-run the thermal case, not just the arithmetic.

**The thermal ranking in this class is unanchored.** The fitted part's stated
0.33 C/W RthJC is back-computed from PD = 379 W at TC = 25 C in a 3.3 x 3.3 mm
package, which is not a physical figure. The same vendor's identical package
drawing states PD = 179 W and RthJC = 0.70 C/W for DOY170N04T, a factor of two
in the same package. Nobody has measured either, and the measured 20x20 failure
mode is FET joint reflow, so this is the number that matters most and the one
least worth trusting.

Following from that: nobody has computed at what phase current DOY170N04T's
2.2 mOhm reaches the same die temperature the fitted part reaches at 1.2 mOhm,
on the 20x20's real copper and airflow. That calculation decides whether the
40 V drop-in is adoptable, and it needs a measured board RthJA, not a datasheet
RthJC.

Not buildable today: IQE013N04LM6 at 90 pieces, BSZ018N04LS6 at 93 and AON7418
at 483. At 24 FETs per board, 90 pieces is under four boards. BSZ018N04LS6 is
the best part in the class on paper and is effectively out of stock.

**PSMN3R3-40MSH is the only different thermal construction available.** LFPAK33
is a copper clip package rated to 175 C junction with 1.48 C/W max to the
mounting base, which is the most direct structural answer to solder joint
reflow. It has no LCSC listing, is Mouser/DigiKey/Farnell only, and needs a
completely new footprint: four clip leads on one side plus a drain mounting
base, not an 8-lead DFN. PSMN1R6-40YLC and PSMN1R8-40YLC were screened and
dropped earlier for being LFPAK56, which is the 5 x 6 package; LFPAK33 is the
3.3 x 3.3 member of the same family and does belong in this class.

## Three-phase gate driver, QFN-24 4x4

Used on OpenESC-30x30 (U4, U6, U8, U10), OpenESC-20x20 (U3, U7, U9, U11) and
OpenAIO, four per board.
Land pattern `4in1ESC:QFN-24_L4.0-W4.0-P0.50-TL-EP2.8`: 24 pads 0.55 x 0.28 mm
on 0.5 mm pitch, pin 1 top left, plus a 1.4 x 1.4 mm centre pad.

Fitted: **NSG2065Q**, C41414478.

Reference pinout, which every part below matches exactly:

| Pin | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | LIN1 | LIN2 | LIN3 | VCC | NC | COM | NC | NC | LO3 | LO2 | LO1 | VS3 |

| Pin | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | HO3 | VB3 | VS2 | HO2 | VB2 | VS1 | HO1 | VB1 | NC | HIN1 | HIN2 | HIN3 |

**An integrated bootstrap diode is mandatory.** Neither ESC carries a single
diode: the 30x30 board has 24 Q, 93 C, 81 R, 13 U and no D at all, and the
20x20 is the same. A pin-compatible driver without the internal diode has no
path to charge the bootstrap capacitor and will not run the high side.
Non-inverting input logic is also mandatory, because AM32 drives these
non-inverted.

| Part | LCSC | Pinout | Integrated BSD | Stock | $@1k |
|---|---|---|---|---|---|
| NSG2065Q (fitted) | C41414478 | verified | yes | 4876 | 0.239 |
| 6288Q-MNS | C49424413 | verified | yes | 9295 | 0.178 @5k |
| HL6288Q | C50331902 | verified | yes | 6020 | 0.182 @500 |
| SD6288Q | see note | verified | yes | n/a | n/a |
| JSM6288Q | C52196409 | verified | not confirmed | 2513 | 0.278 |
| FD6288Q | C328453 | verified | yes | 66 | n/a |
| NSG20652Q | C41414479 | screened | screened | 1367 | 0.310 |
| G2063Q | C49449773 | screened | screened | 5486 | 0.239 |
| HXFD6288QFN24 | C54423134 | screened | screened | 2967 | 0.227 @500 |
| SL6288Q | C53085155 | screened | screened | 417 | 0.126 @5k |
| ZH639D0NU | C53184465 | screened | screened | 1628 | 0.278 |

6288Q-MNS, HL6288Q and JSM6288Q pinouts were read from the datasheets in
`OpenESC-20x20/hardware/datasheets/`. FD6288Q is the original that the family
clones and is nearly out of stock; the clones are the supply.

SD6288Q has a verified pinout and integrated BSD but no LCSC listing under that
number. What LCSC stocks is **SD6287Q**, C44606225, 7458 pieces. In this family
the 6287 suffix marks the variant without the bootstrap diode, exactly as
FD6287 does against FD6288. Confirm before ordering; the datasheet on disk is
for the 6288.

Same package, will not work:

| Part | LCSC | Why not |
|---|---|---|
| DRV8300NLQ | C50345924 | Pin-compatible, pins 5 and 21 become MODE and DT and both default correctly when floating, but the **N** variant has no bootstrap diode. DRV8300D is the one with diodes. DRV8300DI and NI invert the low-side logic. |
| EG2124A | C2856308 | Pin-compatible three-phase driver, but its own datasheet specifies an external bootstrap diode. |
| AMT49406, SBD63006, FT1215Q, FT8132Q, FT8215Q, MS8829 | various | BLDC controllers with integrated output stages or I2C, not gate drivers. Unrelated pinouts. |

The 1.4 x 1.4 mm centre pad is worth noting: the NSG2065Q exposed pad is 2.6 to
2.8 mm square, so the land is about a quarter of its area. That undersizing
applies equally to every part in this table, which makes vendor differences in
exposed pad size irrelevant to the choice.
