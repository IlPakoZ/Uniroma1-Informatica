.data
lista:	.word n1
n1:	.word 10, n2
n2:	.word 7, n3
n3: 	.word 8, n4
n4: 	.word 3, n5
n5:     .word 12, 0
.text
	lw a0, lista
	jal conta
	addi a7, zero, 1
	ecall
	addi a7, zero, 10
	ecall
	
conta:  bne a0, zero, ric
	li a0, 0
	jalr zero, ra, 0
ric:	addi sp, sp, -8
	sw ra, 0(sp)
	add t1, zero, a0
	lw a0, 0(a0)
	sw a0, 4(sp)
	lw a0, 4(t1)
	jal conta
	lw t0, 4(sp)
	lw ra, 0(sp)
	addi sp, sp, 8
	add a0, a0, t0
	jalr zero, ra, 0
	