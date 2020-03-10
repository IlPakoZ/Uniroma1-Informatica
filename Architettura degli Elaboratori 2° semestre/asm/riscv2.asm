.data
	.word 4
	.word 4,6,7,8
.text
	lui t0, 0x10010
	lw t3, 0(t0) 
	addi t3, t3,-1
start:	lw t2, 4(t0)
	lw t1, 8(t0)
	bge t1, t2, prim
	beq x0, x0, seco
prim:	add t2, x0, t1	
seco:	addi t0, t0, 4
	addi t3, t3, -1
	bne t3, x0, start
	add a0, x0, t2
	addi a7, x0, 1
	ecall
	addi a7, x0, 10
	ecall
	