.data
tree: 	.word n0
n0:	.word 5, n1, n2
n1:	.word 3, n3, 0
n2:	.word 2, n4, n5
n3:	.word -5, n6, 0
n4: 	.word 1, 0, 0
n5:	.word -3, 0, 0
n6: 	.word 2, 0, 0

.text
	lw a0, tree
	jal conta
	li a7, 1
	ecall
	li a7, 10
	ecall

conta:	bne a0, zero, ric
	jalr zero, ra, 0
ric:	addi sp, sp, -12
	sw ra, 0(sp)
	sw a0, 4(sp)
	lw a0, 4(a0)
	jal conta
	addi a0, a0, 1
	sw a0, 8(sp)
	lw a0, 4(sp)
	lw a0, 8(a0)
	jal conta
	lw t0, 8(sp)
	add a0, a0, t0 
	lw ra, 0(sp)
	addi sp, sp, 12
	jalr zero, ra, 0
	 
	
