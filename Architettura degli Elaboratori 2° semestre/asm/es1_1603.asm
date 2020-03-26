.data
p:	.asciz "Pari."
d:	.asciz "Dispari."
.text
	addi a7, zero, 5
	ecall
	andi t0, a0, 1
	beq t0, zero, pari
	la a0, d
	b fine
pari:	la a0, p
fine:	addi a7, zero, 4
	ecall
	addi a7, zero, 10
	ecall