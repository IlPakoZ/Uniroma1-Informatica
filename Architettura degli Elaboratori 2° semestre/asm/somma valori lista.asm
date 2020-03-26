.data
lista:	.word n1
n1:	.word 10, n2
n2:	.word 7, n3
n3: 	.word 8, n4
n4: 	.word 3, n5
n5:     .word 12, 0
.text
	lw a0, lista
	jal sum
	addi a7, zero, 1
	ecall
	addi a7, zero, 10
	ecall 
	
	
sum:	addi t0, zero, 0
loop:	bne a0, zero, yes 
	add a0, zero, t0
	jalr zero, ra, 0
yes:	lw t1, 0(a0)
	add t0, t0, t1
	lw a0, 4(a0)
	beq zero, zero, loop
	
