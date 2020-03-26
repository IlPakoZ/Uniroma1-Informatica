.text
	li a7, 5
	ecall
	mv x4, a0
	li a7, 5
	ecall
	mv x5, a0
	add x6, x5, x4
	mv a0, x6
	li a7, 1
	ecall
	li a7, 10
	ecall