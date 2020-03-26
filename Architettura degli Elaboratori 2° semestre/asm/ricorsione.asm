.data
x: 	.word 6
.text

	lw a0, x
	jal fatt
	li a7, 1
	ecall
	li a7, 10
	ecall
	
fatt:   bne a0, zero, ric #a0 contiene n
	li a0, 1
	jalr zero, ra, 0
ric:	addi sp, sp, -8
	sw ra, 0(sp)
	sw a0, 4(sp)
	addi a0, a0, -1
	jal fatt
	#backwards
	lw t0, 4(sp)
	mul a0, a0, t0
	lw ra, 0(sp)
	addi sp, sp, 8
	jalr zero, ra, 0