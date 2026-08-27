# Alternates

Second sources for OpenDrone parts, grouped by the only thing that makes a
swap possible: one land pattern, one pinout, one function. A part listed here
fits the copper. Whether it fits the *board* is the second half of each
section, and that half disqualifies most candidates.

Nothing here is fitted. The fitted part is named at the top of each class and
is the only one that has been through an assembly run. Promoting an alternate
is a board change: datasheet read, stencil check, bench run, in that order.

Verified means the pinout or the parameter was read out of the manufacturer
datasheet. Screened means it came from the LCSC parametric field and nobody has
opened the datasheet. Do not order against a screened row.

Stock and price are LCSC at the 1000 break unless the row says otherwise,
checked 2026-08-27. They move.

## Power MOSFET, DFN 5x6

Used on OpenESC-30x30, Q1-Q24, 24 per board.
Land pattern `4in1ESC-30x30:PDFN-8L_L6.0-W5.0-P1.27`: two rows of four leads
0.58 x 1.08 mm at y +/-2.83, 1.27 mm pitch, plus a 4.4 x 4.1 mm drain pad
centred at y -0.69. Pins 1-3 source, 4 gate, 5-8 drain.

Fitted: **SP40N01GHNK**, C22385416.

| Part | LCSC | VDSS | RDS(on) max @10V | Qg @10V | EAS | RthJC | Stock | $@1k |
|---|---|---|---|---|---|---|---|---|
| SP40N01GHNK (fitted) | C22385416 | 40 V | 1.5 mOhm | ~70 nC | 1089 mJ | 0.96 C/W | 3905 | 0.223 |
| TPHR8504PL | C22388172 | 40 V | 0.85 mOhm | 103 nC | 336 mJ | 0.88 C/W | 5587 | 0.501 |
| XRS280N03C | C50314140 | **30 V** | 0.5 mOhm | 147 nC | not read | not read | 4490 | 0.459 |

All three verified against the datasheet except the XRS280N03C EAS and RthJC.

**The gate is avalanche energy, not RDS(on).** OpenESC-30x30 has no input
clamp. The avalanche-rated FET *is* the overvoltage backstop, by design
(`OpenDrone-Testing/Tests/ESC/ESC-17-overvoltage-rationale.md`). 8S charged is
33.6 V against a 40 V part, so EAS is the margin. Anything below the
SP40N01GHNK's 1089 mJ shrinks the only protection the board has.

**30 V parts do not belong on this board.** XRS280N03C is 30 V VDSS. The board
is rated 2-8S and 8S charged is 33.6 V, above its breakdown. It is a valid
alternate only if the board is re-rated to 6S. The 40 V floor is what buys 8S
in the first place.

Second gate: gate charge. The +10 V buck is an LMR54406 at 0.6 A and 24 FETs
switch off it. 103 nC parts draw about 60 mA at 24 kHz, which the rail carries,
but driver dissipation and edge rate both move with Qg.

Screened only, no datasheet read, EAS unknown for every row:

| Part | LCSC | VDSS | RDS(on) | Qg | Stock | $@1k |
|---|---|---|---|---|---|---|
| HYG025N04NA1C2 | C2917677 | 40 V | 1.4 mOhm @10V | 122 nC | 5227 | 0.446 |
| NTMFS5C410NT1G | C604434 | 40 V | 0.92 mOhm @10V | 86 nC | 2667 | 0.983 |
| AGM4025A | C7466516 | 40 V | 2.0 mOhm @10V | 46 nC | 1028 | 0.306 |
| AON6144 | C133142 | 40 V | 3.5 mOhm @4.5V | 70 nC | 4995 | 0.573 |

## Power MOSFET, DFN 3x3

Used on OpenESC-20x20, Q1-Q24, 24 per board.
Land pattern `Package_SON:Diodes_PowerDI3333-8` (KiCad global library, not the
project library). Four lead pads 0.7 x 0.42 mm at x -1.5 on 0.65 mm pitch
(three source, one gate), four matching pads at x +1.5 for the drain leads, and
a 1.71 x 1.71 mm drain tab at x +0.455. The four drain-lead pads carry no pad
number in that footprint, so KiCad gives them no net: they solder to the part
but are invisible to DRC.

Fitted: **DOY180N03T**, C49441966, 30 V.

| Part | LCSC | VDSS | RDS(on) @10V | Qg @10V | EAS | RthJC | Stock | $ |
|---|---|---|---|---|---|---|---|---|
| DOY180N03T (fitted) | C49441966 | 30 V | 1.0 typ / 1.2 max | 39.8 nC | 100 mJ | 0.33 C/W | 1815 | 0.184 @5k |
| NCEP4065QU | C502974 | 40 V | 2.2 typ / 2.8 max | 34.8 nC | 500 mJ | 2.3 C/W | 2843 | 0.241 |
| SP40N03GNJ | C22466709 | 40 V | 2.9 typ | 26 nC | 169 mJ | 2.27 C/W | 958 | 0.111 @5k |
| AON7140 | C2758662 | 40 V | 1.9 typ / 2.3 max | 42 typ / 60 max | 135 mJ | not read | 2131 | 0.491 |
| APG035N04Q | C5443653 | 40 V | 2.8 typ / 3.5 max | 20.3 nC | 100 mJ | 2.42 C/W | 1436 | 0.143 |
| BSZ018N04LS6 | C534643 | 40 V | 1.8 max | 31 nC | 189 mJ | 1.8 C/W | 164 | 1.075 |

All verified from datasheets in
`OpenESC-20x20/hardware/datasheets/`. AON7140 EAS is at L 0.3 mH and IAS 30 A,
a softer condition than the 0.5 mH the others use, so it is not directly
comparable.

Every 40 V row costs conduction loss: the fitted 30 V part is 1.0 mOhm and the
best 40 V candidate here is 1.9 mOhm typ. The trade is cell count, since 30 V
VDSS is what caps OpenESC-20x20 and OpenAIO at 6S. Take a 40 V part only if the
board is being re-rated, and re-run the thermal case, not just the arithmetic.

Treat the fitted part's 0.33 C/W RthJC as unconfirmed. A 3.3 x 3.3 mm package
claiming three times better junction-to-case than the 5 x 6 mm SP40N01GHNK is
not physical. Nobody has measured it, and the measured 20x20 failure mode is
FET joint reflow.

BSZ018N04LS6 is the best part in the class on paper and is effectively out of
stock at LCSC. PSMN1R6-40YLC and PSMN1R8-40YLC were screened and dropped: both
are LFPAK56, a 5 x 6 mm package, and both are under 50 pieces at LCSC.

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
