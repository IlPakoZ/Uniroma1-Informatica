.data
	.word 90,100
.text
	lui t0, 0x10010
	lw t1, 0(t0)
	lw t2, 4(t0)
	addi sp, sp, -4
	sw t1, 0(sp)
	addi sp, sp, -4
	sw t2, 0(sp)
	lw t3, 0(sp)
	addi sp, sp, 4
	lw t4, 0(sp)
	addi sp, sp, 4
	add a0, x0, t3
	addi a7, x0, 1
	ecall
	add a0, x0, t4
	addi a7, x0, 1
	ecall
	addi a7, x0, 10
	ecall
	
	