# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 0
    assert dut.uio_out.value == 0

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    dut.ui_in.value = 0x80
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0xFF
    assert dut.uio_out.value == 0xFF

    dut.ui_in.value = 0xC0
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0xFD
    assert dut.uio_out.value == 0x20

    async def test_arrow(pattern, flashing, sequential, *sequence):
        if flashing:
            pattern |= 0x10
        if sequential:
            pattern |= 0x20
        pattern |= 0xC0

        dut.ui_in.value = pattern
        dut.rst_n.value = 0
        await ClockCycles(dut.clk, 1)
        lamps = dut.uo_out.value | (dut.uio_out.value << 8)
        assert lamps == sequence[0]
        dut.rst_n.value = 1

        for x in range(0, 12):
            await ClockCycles(dut.clk, 1)
            lamps = dut.uo_out.value | (dut.uio_out.value << 8)
            assert lamps == sequence[x % len(sequence)]

    await test_arrow(0, False, False, 0x20FD)
    await test_arrow(1, False, False, 0x905F)
    await test_arrow(2, False, False, 0x20FD)
    await test_arrow(3, False, False, 0x905F)
    await test_arrow(4, False, False, 0x20FD)
    await test_arrow(5, False, False, 0x905F)
    await test_arrow(6, False, False, 0x20FD)
    await test_arrow(7, False, False, 0x905F)
    await test_arrow(8, False, False, 0xEAFF)
    await test_arrow(9, False, False, 0xF57F)
    await test_arrow(10, False, False, 0xEA95)
    await test_arrow(11, False, False, 0xF554)
    await test_arrow(12, False, False, 0xB0DD)
    await test_arrow(13, False, False, 0xA000)
    await test_arrow(14, False, False, 0x007F)
    await test_arrow(15, False, False, 0xB9D5)

    await test_arrow(0, True, False, 0x20FD, 0)
    await test_arrow(1, True, False, 0x905F, 0)
    await test_arrow(2, True, False, 0x20FD, 0)
    await test_arrow(3, True, False, 0x905F, 0)
    await test_arrow(4, True, False, 0x20FD, 0)
    await test_arrow(5, True, False, 0x905F, 0)
    await test_arrow(6, True, False, 0x20FD, 0)
    await test_arrow(7, True, False, 0x905F, 0)
    await test_arrow(8, True, False, 0xEAFF, 0)
    await test_arrow(9, True, False, 0xF57F, 0)
    await test_arrow(10, True, False, 0xEA95, 0)
    await test_arrow(11, True, False, 0xF554, 0)
    await test_arrow(12, True, False, 0xB0DD, 0)
    await test_arrow(13, True, False, 0xA000, 0)
    await test_arrow(14, True, False, 0x007F, 0)
    await test_arrow(15, True, False, 0xB9D5, 0)

    await test_arrow(0, False, True, 0x0060, 0x0078, 0x20FD, 0x20FD)
    await test_arrow(1, False, True, 0x0003, 0x000F, 0x905F, 0x905F)
    await test_arrow(2, False, True, 0x0060, 0x007C, 0x20FD, 0x20FD)
    await test_arrow(3, False, True, 0x0003, 0x001F, 0x905F, 0x905F)
    await test_arrow(4, False, True, 0x0070, 0x007C, 0x20FD, 0x20FD)
    await test_arrow(5, False, True, 0x0007, 0x001F, 0x905F, 0x905F)
    await test_arrow(6, False, True, 0x8870, 0x4274, 0x20FD, 0x20FD)
    await test_arrow(7, False, True, 0x2107, 0x4417, 0x905F, 0x905F)
    await test_arrow(8, False, True, 0x8870, 0xCA7C, 0xEAFF, 0xEAFF)
    await test_arrow(9, False, True, 0x2107, 0x651F, 0xF57F, 0xF57F)
    await test_arrow(10, False, True, 0x8810, 0xCA14, 0xEA95, 0xEA95)
    await test_arrow(11, False, True, 0x2104, 0x6514, 0xF554, 0xF554)
    await test_arrow(12, False, True, 0xB0DD, 0)
    await test_arrow(13, False, True, 0xA000, 0)
    await test_arrow(14, False, True, 0x007F, 0)
    await test_arrow(15, False, True, 0x2185, 0x9850)

    await test_arrow(0, True, True, 0x0060, 0x0078, 0x20FD, 0)
    await test_arrow(1, True, True, 0x0003, 0x000F, 0x905F, 0)
    await test_arrow(2, True, True, 0x0060, 0x007C, 0x20FD, 0)
    await test_arrow(3, True, True, 0x0003, 0x001F, 0x905F, 0)
    await test_arrow(4, True, True, 0x0070, 0x007C, 0x20FD, 0)
    await test_arrow(5, True, True, 0x0007, 0x001F, 0x905F, 0)
    await test_arrow(6, True, True, 0x8870, 0x4274, 0x20FD, 0)
    await test_arrow(7, True, True, 0x2107, 0x4417, 0x905F, 0)
    await test_arrow(8, True, True, 0x8870, 0xCA7C, 0xEAFF, 0)
    await test_arrow(9, True, True, 0x2107, 0x651F, 0xF57F, 0)
    await test_arrow(10, True, True, 0x8810, 0xCA14, 0xEA95, 0)
    await test_arrow(11, True, True, 0x2104, 0x6514, 0xF554, 0)
    await test_arrow(12, True, True, 0xB0DD, 0)
    await test_arrow(13, True, True, 0xA000, 0)
    await test_arrow(14, True, True, 0x007F, 0)
    await test_arrow(15, True, True, 0x2185, 0x9850)
