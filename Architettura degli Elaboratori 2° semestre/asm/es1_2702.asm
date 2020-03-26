.data
	.word 48,40
.text
	lui x5, 0x10010
	lw x6, 0(x5)
	lw x7, 4(x5)
	add x6, x6, x7