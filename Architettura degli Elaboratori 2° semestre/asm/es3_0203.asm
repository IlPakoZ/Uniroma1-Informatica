.data
lista: 	.word n0
n0:	.word 4, n1
n1:	.word 8, n2
n2:	.word -2, n3
n3:	.word 7, n4
n4: 	.word 1, 0

.text
	lui a0, 0x10010
	lw a0, 0(a0)
	jal conta
	li a7, 1
	ecall
	li a7, 10
	ecall

conta: 	bne a0, zero, ric
	addi a0, zero, 0
	jalr zero, ra, 0
ric:	addi sp, sp, -4
	sw ra, 0(sp)
	lw a0, 4(a0)
	jal conta
	addi a0, a0, 1
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, ra, 0