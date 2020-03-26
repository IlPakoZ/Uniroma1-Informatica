.data
	.word 6
.text
	lui a0, 0x10010
	lw a0, 0(a0)
	jal fatt
	li a7, 1
	ecall
	li a7, 10
	ecall
	
fatt:	bne a0, zero, ric
	addi a0, a0, 1
	jalr zero, ra, 0
ric:	addi sp, sp, -8
	sw ra, 4(sp)
	sw a0, 0(sp)
	addi a0, a0, -1
	jal fatt 
	lw t0, 0(sp)
	lw ra, 4(sp)
	addi sp, sp, 8
	mul a0, a0, t0
	jalr zero, ra, 0