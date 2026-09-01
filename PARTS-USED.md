# Parts used

Every component that has actually been manufactured on an OpenDrone board.

A part is listed here only if it is used on a board whose repo is at
`status-alpha` or beyond, which means it has been through a real assembly
run: sourced, footprinted, and it survived a reflow oven. Parts that exist
only on a planned or in-progress design are deliberately absent, however
good they look on paper. When a board reaches alpha, its parts join.

Regenerate: `python3 tools/build-parts-index.py`

112 parts across 8 manufactured boards: OpenESC-20x20, OpenESC-30x30, OpenFC-Lite, OpenFC-Lite-Mini, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono.

| LCSC | Value | MPN | Footprint | Boards |
|---|---|---|---|---|
| C106225 | 10k | RC0201FR-0710KL | R_0201_0603Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C76939 | 100nF | GRM033R61E104KE14D | C_0201_0603Metric | OpenAIO, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C270365 | 10k | 0201WMF1001TEE | R0201 | OpenAIO, OpenESC-20x20, OpenESC-30x30, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C15525 | 10uF | CL05A106MQ5NUNC | C_0402_1005Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C206435 | 2.5nH | LQP03TN2N5C02D | L_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C206441 | 24nH | LQP03TN24NH02D | L_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C2168164 | 10nF | GRM033R61A103KA01J | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C2651081 | 2450FM07D0034T | 2450FM07D0034T | FILTER-SMD_4P-L1.0-W0.5-L | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C2762594 | 22uF | CL10A226MO7JZNC | C_0603_1608Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30, OpenFC-Lite, OpenFC-Lite-Mini |
| C2861882 | TLV75533PDQNR | TLV75533PDQNR | X2SON-4_L1.0-W1.0-P0.65-TL-EP | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C2875272 | CJ17-400001010B20 | CJ17-400001010B20 | CRYSTAL-SMD_4P-L1.6-W1.2-BL | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C2976675 | TS2306A 240GF MSM 9_C2976675 | TS2306A 240gf MSM 9 | SW-SMD_4P-L3.0-W2.0-P0.85-LS3.5 | OpenAIO, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini, OpenRX-Gemini |
| C5349953 | XL-1010RGBC-WS2812B | XL-1010RGBC-2812B | LED-SMD_4P-L1.0-W1.0-TL_XL-1010RGBC-WS2812B | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C76935 | 1uF | GRM033R61A105ME44D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C76991 | 10uF | GRM155R60J106ME44D | C_0402_1005Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C85891 | 15pF | GRM0335C1H150JA01D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C85895 | 1.2pF | GRM0335C1H1R2BA01D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C85926 | 470nF | GRM033R60J474KE90D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C86125 | 2.0nH | LQP03TN2N0B02D | L_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C89334 | 2450AT18A100E | 2450AT18A100E | ANT-SMD_L3.2-W1.6 | OpenAIO, OpenRX-Gemini, OpenRX-Lite, OpenRX-Lite-UFL, OpenRX-Mono |
| C160407 | SM08B-SRSS-TB | SM08B-SRSS-TB(LF)(SN) | JST_SM08B-SRSS-TB | OpenESC-20x20, OpenESC-30x30, OpenFC-Lite, OpenFC-Lite-Mini |
| C166281 | 2.4k | RTT012401FTH | R_0201_0603Metric | OpenAIO, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C2107920 | 6.49k | AF0201FR-076K49L | R_0201_0603Metric | OpenAIO, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C270344 | 5.1k | 0201WMF5101TEE | R_0201_0603Metric | OpenAIO, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C270364 | 100k | 0201WMF1003TEE | R_0201_0603Metric | OpenAIO, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C88374 | Conn_Coaxial_Small | U.FL-R-SMT-1(80) | U.FL_Hirose_U.FL-R-SMT-1_Vertical | OpenAIO, OpenRX-Gemini, OpenRX-Lite-UFL, OpenRX-Mono |
| C965793 | LED_1_Green | XL-1005UGC  | LED_0402_1005Metric | OpenAIO, OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C105226 | 22uF | CL05A226MQ5QUNC | C_0402_1005Metric | OpenESC-20x20, OpenESC-30x30, OpenFC-Lite |
| C106224 | 100k | RC0201FR-07100KL | R_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C106226 | 10R | RC0201FR-0710RL | R_0201_0603Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C150853 | SKY13373-460LF |  | QFN-12_EP_2x2_Pitch0.5mm | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C151629 | SDM02U30LP3-7B | SDM02U30LP3-7B | X3-DFN0603-2_L0.6-W0.3-RD | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C160405 | SM06B-SRSS-TB(LF)(SN) | SM06B-SRSS-TB(LF)(SN) | CONN-SMD_SM06B-SRSS-TB-LF-SN | OpenAIO, OpenFC-Lite, OpenFC-Lite-Mini |
| C161488 | 2.2nF | GRM033R71E222KA12D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C181043 | 100nF | GRM033R6YA104KE14D | C_0201_0603Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C19213 | RFX2401C | RFX2401C | QFN-16_L3.0-W3.0-P0.50-BL-EP1.7 | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C192855 | 47nH | LQW15AN47NJ00D | L_0402_1005Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C194437 | 10uH | MLZ1608N100LT000 | L_0603_1608Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C19842466 | 0900PC16J0042001E | 0900PC16J0042001E | FILTER-SMD_10P-L2.0-W1.6-BL | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C2058245 | INA186A3IDCKR | INA186A3IDCKR | SOT-363_SC-70-6 | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C2074788 | 220 | ERJ-1GNF2200C | R_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C2151551 | SX1281IMLTRT | SX1281IMLTRT | QFN-24_L4.0-W4.0-P0.50-TL-EP2.6 | OpenAIO, OpenRX-Lite, OpenRX-Lite-UFL |
| C22355736 | LED_1_Blue | XL-1005UBC | LED_0402_1005Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C22381772 | OW7EL89CENUYO3YLC-32M | OW7EL89CENUYO3YLC-32M | OSC-SMD_4P-L2.0-W1.6-BL_TXC_7Z | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C22434896 | OW7EL89CENUNFAYLC-52M | OW7EL89CENUNFAYLC-52M | OSC-SMD_4P-L2.0-W1.6-BL_TXC_7Z | OpenAIO, OpenRX-Lite, OpenRX-Lite-UFL |
| C226468 | 220R | AC0201FR-07220RL | R_0201_0603Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C23733 | 4.7uF | CL05A475MP5NRNC | C_0402_1005Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C2673087 | SN74LVC1G3157DTBR | SN74LVC1G3157DTBR | X2SON-6_L1.0-W0.8-BL | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C270363 | 12k | 0201WMF1202TEE | R_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C273280 | 3.9k | RC0201FR-073K9L | R_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C274337 | 200 | RC0201FR-07200RL | R_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C274342 | 10k |  | R0201 | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C274878 | 75R | RC0201FR-0775RL | R_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C2765098 | AT32F421G8U7 | AT32F421G8U7 | QFN-28_L4.0-W4.0-P0.40-TL-EP2.4 | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C2836813 | BMI270 | BMI270 | LGA-14_L3.0-W2.5-P0.50-BR | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C2849580 | AP1606 | AP1606 | DFN-3L_L1.0-W0.6-P0.65-BR | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C2876045 | TLV7031DPWR | TLV7031DPWR | X2SON-4_L0.8-W0.8-P0.48-TL-A | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C2876234 | LP5912-1.8DRVR | LP5912-1.8DRVR | WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C307331 | 100nF | CL05B104KB54PNC | C_0402_WIDE | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C384956 | 10pF | GRM0335C1H100FA01D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C39846837 | XRTC303020D4R7MBCA | XRTC303020D4R7MBCA | IND-SMD_L3.0-W3.0_AFE303020S | OpenAIO, OpenFC-Lite, OpenFC-Lite-Mini |
| C41414478 | NSG2065Q | NSG2065Q | QFN-24_L4.0-W4.0-P0.50-TL-EP2.8 | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C415703 | 22uF | GRM155R60J226ME11D | C_0402_1005Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C423739 | 1.4k | 0201WMF1401TEE | R_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C459538 | DMN1150UFB-7B |  | DFN-3L_L1.0-W0.6-P0.65-BR | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C473048 | 10k |  | R0201 | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C473509 | 680R | 0201WMF6800TEE | R_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C473542 | 15R | 0201WMF150JTEE | R_0201_0603Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C474437 | 7.5k | RC0201FR-077K5L | R_0201_0603Metric | OpenAIO, OpenFC-Lite, OpenFC-Lite-Mini |
| C5187472 | TYPE-C 16P QTWT | TYPE-C 16P QTWT | USB-TYPE-C-SMD_TYPE-C-16P-QTWT | OpenAIO, OpenFC-Lite, OpenFC-Lite-Mini |
| C524780 | LP5912-3.3DRVR | LP5912-3.3DRVR | WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C5267406 | LSM6DSV16XTR |  | LGA-14_L3.0-W2.5-P0.50-BR | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C526944 | 470p | CC0201JRX7R9BB471 | C_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C52923 | 1uF | CL05A105KA5NQNC | C_0402_1005Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C57784 | 510R | RC0201FR-07510RL | R_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C64890 | DSK24 | DSK24 | SOD-123_L2.8-W1.8-LS3.7-RD | OpenAIO, OpenFC-Lite, OpenFC-Lite-Mini |
| C66942 | 1nF | 0201B102K500NT | C_0201_0603Metric | OpenAIO, OpenRX-Lite, OpenRX-Lite-UFL |
| C695806 | 0.2mR | ASR-S-3-0.2F | R_2512_6332Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C7463385 | COS8051SOT | COS8051SOT | SOT-23-5_L3.0-W1.7-P0.95-LS2.8-BR | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C7498014 | LR1121IMLTRT | LR1121IMLTRT | QFN-32-1EP_5x5mm_P0.5mm_EP3.7x3.7mm | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C7500381 | 1uF | CC0402KRX7R6BB105 | C_0402_1005Metric | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C76928 | 100n | GRM033R60J104KE19D | C_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C76937 | 100nF 16v |  | C0201 | OpenAIO, OpenESC-20x20, OpenESC-30x30 |
| C778391 | 30R | NQ01WMJ0300TEE | R_0201_0603Metric | OpenFC-Core, OpenFC-Lite, OpenFC-Lite-Mini |
| C85908 | 47p | GRM0335C1H470JA01D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C85934 | 1n | GRM033R71H102KA12D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C907939 | 220pF | GRM0335C1E221JA01D | C_0201_0603Metric | OpenAIO, OpenRX-Gemini, OpenRX-Mono |
| C98192 | 4.7uF 50v | CL21A475KBQNNNE | C_0805_2012Metric | OpenAIO, OpenFC-Lite, OpenFC-Lite-Mini |
| C166378 | 115k | RTT011153FTH | R_0201_0603Metric | OpenESC-20x20, OpenESC-30x30 |
| C2848334 | TLV76733DRVR | TLV76733DRVR | WSON-6_L2.0-W2.0-P0.65-TL-EP | OpenESC-20x20, OpenESC-30x30 |
| C320695 | 13.7k | RC-01W1372FT | R_0201_0603Metric | OpenAIO, OpenFC-Lite-Mini |
| C37635340 | XTM25012000JT00351001 | XTM25012000JT00351001 | CRYSTAL-SMD_4P-L2.5-W2.0-BL-A | OpenFC-Lite, OpenFC-Lite-Mini |
| C380366 | 4.7uF | TCC1206X7R475K500HT | C_1206_3216Metric | OpenESC-20x20, OpenESC-30x30 |
| C42411119 | AOTA-B201610S3R3-101-T | AOTA-B201610S3R3-101-T | IND-SMD_L2.0-W1.6_AOTA-B201610S3R3-101-T | OpenFC-Lite, OpenFC-Lite-Mini |
| C46594347 | FTC160808S4R7MBCA | FTC160808S4R7MBCA | IND-SMD_L1.6-W0.8_FTC160865SR47MBCA | OpenESC-20x20, OpenESC-30x30 |
| C48391583 | XRIM160808SR47MBCD |  | IND-SMD_L1.6-W0.8_FTC160865SR47MBCA | OpenESC-20x20, OpenESC-30x30 |
| C49441966 | DOY180N03T | DOY180N03T | Diodes_PowerDI3333-8 | OpenAIO, OpenESC-20x20 |
| C498185 | TF-021B-H265 | TF-021B-H265 | TF-SMD_TF-021B-H265 | OpenFC-Core, OpenFC-Lite-Mini |
| C5219261 | LMR51430YFDDCR | LMR51430YFDDCR | SOT-23-6_L2.9-W1.6-P0.95-LS2.9-BL | OpenAIO, OpenFC-Lite-Mini |
| C5219316 | LMR54406DBVR | LMR54406DBVR | SOT-23-6_L2.9-W1.6-P0.95-LS2.8-BR | OpenESC-20x20, OpenESC-30x30 |
| C5383002 | LMR51420YDDCR |  | SOT-23-6_L2.9-W1.6-P0.95-LS2.9-BL | OpenAIO, OpenFC-Lite-Mini |
| C76923 | 20p | GRM0335C1H200JA01D | C_0201_0603Metric | OpenFC-Lite, OpenFC-Lite-Mini |
| C152351 | 47948-0001 | 479480001 | ANT-SMD_47948-0001 | OpenRX-Lite |
| C160403 | SM03B-SRSS-TB | SM03B-SRSS-TB(LF)(SN) | CONN-SMD_SM03B-SRSS-TB-LF-SN-P | OpenFC-Lite |
| C160404 | SM04B-SRSS-TB | SM04B-SRSS-TB(LF)(SN) | CONN-SMD_4P-P1.00_SM04B-SRSS-TB-LF-SN | OpenFC-Lite |
| C22385416 | SP40N01GHNK | SP40N01GHNK | PDFN-8L_L6.0-W5.0-P1.27 | OpenESC-30x30 |
| C320741 | 19.1k | RC-01W1912FT | R_0201_0603Metric | OpenFC-Lite |
| C332577 | 8.87k | RTT018871FTH | R_0201_0603Metric | OpenFC-Lite |
| C393941 | TF PUSH | TF PUSH | TF-SMD_TF-PUSH | OpenFC-Lite |
| C39843328 | RP2354B_C39843328 | RP2354B | QFN-80_L10.0-W10.0-P0.40-TL-EP3.4 | OpenFC-Lite |
| C41378174 | RP2354A | RP2354A | QFN-60_L7.0-W7.0-P0.40-TL-EP3.4 | OpenFC-Lite-Mini |
| C45262770 | LMR51635YDDCR | LMR51635YDDCR | SOT-23-6_L2.9-W1.6-P0.95-LS2.8-BL | OpenFC-Lite |
