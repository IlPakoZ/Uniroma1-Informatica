.data
n01: .word 8, n02
n02: .word 7, n03
n03: .word -9, n04
n04: .word 4, 0
lista: .word n01

.text

	lw a0, lista
	jal conta
	li a7, 1
	ecall 
	li a7, 10
	ecall
	
conta: 	addi t0, zero, 0
loop:	beq a0, zero, fine
	addi t0, t0, 1    #conta +1 nodo
	lw a0, 4(a0)
	beq zero, zero, loop
fine:	addi a0, t0, 0
	jalr zero, ra, 0
