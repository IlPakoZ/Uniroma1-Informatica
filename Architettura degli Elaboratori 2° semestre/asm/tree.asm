.data
tree:	.word n01
n01:	.word 8, n02, n03
n02: 	.word 5, n04, n05
n03:	.word 13, n06, 0
n04:	.word 3, 0, 0
n05:	.word 2, 0, 0
n06: 	.word -7, 0, 0

.text
	lw a0, tree
	jal somma
	li a7, 1
	ecall
	li a7, 10
	ecall
		
somma:	bne a0, zero, s_ric
	jalr zero, ra, 0
	
s_ric: 	addi sp, sp, -12
	sw ra, 0(sp)
	sw a0, 4(sp)		#indirizzo della radice -> stack 
	lw a0, 4(a0)
	jal somma	
				#in a0 la somma del sottoalbero SX
	sw a0, 8(sp)		#somma del sottoalbero sx -> stack
	lw a0, 4(sp)
	lw a0, 8(a0)
	jal somma
				#in a0 la somma del sottoalbero DX
	lw t0, 8(sp)
	add a0, a0, t0		#in a0 la somma di SA dx e sx
	lw t0, 4(sp)
	lw t0, 0(t0)
	add a0, a0, t0
	lw ra, 0(sp)
	addi sp, sp, 12
	jalr zero, ra, 0