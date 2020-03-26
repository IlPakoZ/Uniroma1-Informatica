.data
	m1: .asciz "Pari."
	m2: .asciz "Dispari."
.text
	addi a7, zero, 5
	ecall
	andi t0, a0, 1
	beq t0, zero, e1
	la a0, m2
	addi a7, zero, 4
	ecall
	addi a7, zero, 10
	ecall	
e1: 	la a0, m1
	addi a7, zero, 4
	ecall
	addi a7, zero, 10
	ecall