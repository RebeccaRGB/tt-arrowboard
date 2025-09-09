![](../../workflows/gds/badge.svg) ![](../../workflows/docs/badge.svg) ![](../../workflows/test/badge.svg) ![](../../workflows/fpga/badge.svg)

# Arrow Board

## How it works

This project displays various flashing and animated arrow signs used for controlling traffic.

There are sixteen patterns selectable with inputs 0-3. Input 4 enables flashing and input 5 enables an animated sequence.

| Pattern | Steady/Flashing     | Animated Sequence                                           |
| ------- | ------------------- | ----------------------------------------------------------- |
| 0       | ![](docs/p20FD.svg) | ![](docs/p0060.svg) ![](docs/p0078.svg) ![](docs/p20FD.svg) |
| 1       | ![](docs/p905F.svg) | ![](docs/p0003.svg) ![](docs/p000F.svg) ![](docs/p905F.svg) |
| 2       | ![](docs/p20FD.svg) | ![](docs/p0060.svg) ![](docs/p007C.svg) ![](docs/p20FD.svg) |
| 3       | ![](docs/p905F.svg) | ![](docs/p0003.svg) ![](docs/p001F.svg) ![](docs/p905F.svg) |
| 4       | ![](docs/p20FD.svg) | ![](docs/p0070.svg) ![](docs/p007C.svg) ![](docs/p20FD.svg) |
| 5       | ![](docs/p905F.svg) | ![](docs/p0007.svg) ![](docs/p001F.svg) ![](docs/p905F.svg) |
| 6       | ![](docs/p20FD.svg) | ![](docs/p8870.svg) ![](docs/p4274.svg) ![](docs/p20FD.svg) |
| 7       | ![](docs/p905F.svg) | ![](docs/p2107.svg) ![](docs/p4417.svg) ![](docs/p905F.svg) |
| 8       | ![](docs/pEAFF.svg) | ![](docs/p8870.svg) ![](docs/pCA7C.svg) ![](docs/pEAFF.svg) |
| 9       | ![](docs/pF57F.svg) | ![](docs/p2107.svg) ![](docs/p651F.svg) ![](docs/pF57F.svg) |
| 10      | ![](docs/pEA95.svg) | ![](docs/p8810.svg) ![](docs/pCA14.svg) ![](docs/pEA95.svg) |
| 11      | ![](docs/pF554.svg) | ![](docs/p2104.svg) ![](docs/p6514.svg) ![](docs/pF554.svg) |
| 12      | ![](docs/pB0DD.svg) | ![](docs/pB0DD.svg) ![](docs/p0000.svg)                     |
| 13      | ![](docs/pA000.svg) | ![](docs/pA000.svg) ![](docs/p0000.svg)                     |
| 14      | ![](docs/p007F.svg) | ![](docs/p007F.svg) ![](docs/p0000.svg)                     |
| 15      | ![](docs/pB9D5.svg) | ![](docs/p9850.svg) ![](docs/p2185.svg)                     |

## How to test

Set `ui_in[7]` low and `ui_in[6]` low. All outputs should be low.

Set `ui_in[7]` high and `ui_in[6]` low. All outputs should be high.

Set `ui_in[3:0]` to one of the sixteen patterns. Set `ui_in[4]` low and `ui_in[5]` low. Set `ui_in[6]` high. Pulse `clk` at a desired rate. Outputs should reflect a steady pattern.

Set `ui_in[3:0]` to one of the sixteen patterns. Set `ui_in[4]` high and `ui_in[5]` low. Set `ui_in[6]` high. Pulse `clk` at a desired rate. Outputs should alternate between a steady pattern and a blank pattern.

Set `ui_in[3:0]` to one of the sixteen patterns. Set `ui_in[4]` low and `ui_in[5]` high. Set `ui_in[6]` high. Pulse `clk` at a desired rate. Outputs should reflect a sequential pattern with a repeated last frame.

Set `ui_in[3:0]` to one of the sixteen patterns. Set `ui_in[4]` high and `ui_in[5]` high. Set `ui_in[6]` high. Pulse `clk` at a desired rate. Outputs should reflect a sequential pattern with a blank last frame.

Special cases: The animated versions of patterns 12, 13, and 14 behave the same as the flashing versions and are unaffected by input 4. The animated version of pattern 15 always alternates between the same two frames without repeated or blank frames.

## External hardware

An array of 25 LEDs in the following configuration:

![](docs/arrowboard-rd.svg)

| Lamp | Output       | Lamp | Output       |
| ---- | ------------ | ---- | ------------ |
| A    | `uo_out[0]`  | J    | `uio_out[0]` |
| B    | `uo_out[1]`  | K    | `uio_out[1]` |
| C    | `uo_out[2]`  | L    | `uio_out[2]` |
| D    | `uo_out[3]`  | M    | `uio_out[3]` |
| E    | `uo_out[4]`  | N    | `uio_out[4]` |
| F    | `uo_out[5]`  | P    | `uio_out[5]` |
| G    | `uo_out[6]`  | Q    | `uio_out[6]` |
| H    | `uo_out[7]`  | R    | `uio_out[7]` |

Set `ui_in[7]` high if a high level lights the LED or low if a low level lights the LED.

## What is Tiny Tapeout?

Tiny Tapeout is an educational project that aims to make it easier and cheaper than ever to get your digital and analog designs manufactured on a real chip.

To learn more and get started, visit https://tinytapeout.com.

## Resources

- [FAQ](https://tinytapeout.com/faq/)
- [Digital design lessons](https://tinytapeout.com/digital_design/)
- [Learn how semiconductors work](https://tinytapeout.com/siliwiz/)
- [Join the community](https://tinytapeout.com/discord)
- [Build your design locally](https://www.tinytapeout.com/guides/local-hardening/)
