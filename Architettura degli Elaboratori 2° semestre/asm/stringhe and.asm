.data
	.asciz "Pari."
	.asciz "Dispari."
.text
	addi a7, zero, 5
	ecall
	andi t0, a0, 1
	beq t0, zero, e1
	lui a0, 0x10010
	addi a0, a0, 6
	addi a7, zero, 4
	ecall
	addi a7, zero, 10
	ecall	
e1: 	lui a0, 0x10010
	addi a7, zero, 4
	ecall
	addi a7, zero, 10
	ecall