.data
	.word 8, 7, 0
.text
	lui s0, 0x10010
	lw s1, 0(s0)
	lw s2, 4(s0)
	add s1, s1, s2
	sw s1, 8(s0)
	addi a7, zero, 10
	ecall