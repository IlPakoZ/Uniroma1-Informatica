.data
	.word 7,9,15
.text
	lui t0, 0x10010
	lw x5, 0(t0)
	lw x6, 4(t0)
	lw x7, 8(t0)
	li x8, 0
	add x8, x8, x5
	add x8, x8, x6
	add x8, x8, x7
	
	