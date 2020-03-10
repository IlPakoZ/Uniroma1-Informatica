.data
	.word 8,9,0
.text
	lui x3, 0x10010
	lw x4, 0(x3)
	lw x5, 4(x3)
	add x4, x4, x5
	sw x4, 8(x3)
	addi a7, x0, 10
	ecall
	