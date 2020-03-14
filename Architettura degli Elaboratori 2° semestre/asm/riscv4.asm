.data
	.word 60,80
.text
	lui t1, 0x10010
	lw t2, 0(t1)
	lw t3, 4(t1)
	sub t4, t3, t2
	bge t4, x0, fine 
nega:	sub t4, x0, t4 
fine:	sw t4, 8(t1)
	addi a7, a0, 10
	ecall
	