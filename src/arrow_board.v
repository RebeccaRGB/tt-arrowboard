module arrow_board (
	input wire [1:0] phase,
	input wire [3:0] pattern,
	input wire flashing,
	input wire sequential,
	input wire lt, bi, al,
	output wire [15:0] lamps
);

	reg [15:0] data;
	assign lamps = ((data | {16{~lt}}) & {16{bi}}) ^ {16{~al}};

	always_comb begin
		case (pattern)

			4'h0: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h0078 : 16'h0060) : (flashing & phase[0]) ? 16'h0000 : 16'h20FD;
			4'h1: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h000F : 16'h0003) : (flashing & phase[0]) ? 16'h0000 : 16'h905F;
			4'h2: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h007C : 16'h0060) : (flashing & phase[0]) ? 16'h0000 : 16'h20FD;
			4'h3: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h001F : 16'h0003) : (flashing & phase[0]) ? 16'h0000 : 16'h905F;
			4'h4: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h007C : 16'h0070) : (flashing & phase[0]) ? 16'h0000 : 16'h20FD;
			4'h5: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h001F : 16'h0007) : (flashing & phase[0]) ? 16'h0000 : 16'h905F;
			4'h6: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h4274 : 16'h8870) : (flashing & phase[0]) ? 16'h0000 : 16'h20FD;
			4'h7: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h4417 : 16'h2107) : (flashing & phase[0]) ? 16'h0000 : 16'h905F;
			4'h8: data = (sequential & ~phase[1]) ? (phase[0] ? 16'hCA7C : 16'h8870) : (flashing & phase[0]) ? 16'h0000 : 16'hEAFF;
			4'h9: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h651F : 16'h2107) : (flashing & phase[0]) ? 16'h0000 : 16'hF57F;
			4'hA: data = (sequential & ~phase[1]) ? (phase[0] ? 16'hCA14 : 16'h8810) : (flashing & phase[0]) ? 16'h0000 : 16'hEA95;
			4'hB: data = (sequential & ~phase[1]) ? (phase[0] ? 16'h6514 : 16'h2104) : (flashing & phase[0]) ? 16'h0000 : 16'hF554;

			4'hC: data = ((sequential | flashing) & phase[0]) ? 16'h0000 : 16'hB0DD;
			4'hD: data = ((sequential | flashing) & phase[0]) ? 16'h0000 : 16'hA000;
			4'hE: data = ((sequential | flashing) & phase[0]) ? 16'h0000 : 16'h007F;

			4'hF: data = sequential ? (phase[0] ? 16'h9850 : 16'h2185) : (flashing & phase[0]) ? 16'h0000 : 16'hB9D5;

		endcase
	end

endmodule
