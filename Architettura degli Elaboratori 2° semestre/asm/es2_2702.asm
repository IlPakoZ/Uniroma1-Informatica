.data
	.word 6
	.word 1,4,5,6,7,8
.text

	lui x5, 0x10010
	lw x6, 0(x5)
	addi x5, x5, 4
	addi x7, zero, 0
loop:	lw x8, 0(x5)
	add x7, x7, x8
	addi x5, x5, 4
	addi x6, x6, -1
	bne x6, zero, loop
fine:	mv a0, x7
	li a7, 1
	ecall
	li a7, 10
	ecall
	