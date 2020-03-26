.data
lista: .word m01
m01: .word 1, m02
m02: .word 1, m03
m03: .word 1, m04
m04: .word 1, m05
m05: .word 1, m06
m06: .word 1, m07
m07: .word 1, 0

.text 
	lw a0, lista
	jal conta
	li a7, 1
	ecall
	li a7, 10
	ecall
	
conta: 	bne a0, zero, ric
	li a0, 0
	jalr zero, ra, 0
ric:   addi sp, sp, -4
	sw ra,0(sp)
	lw a0, 4(a0)
	jal conta
	addi a0, a0, 1
	lw ra, 0(sp)
	addi sp, sp, 4
	jalr zero, ra, 0