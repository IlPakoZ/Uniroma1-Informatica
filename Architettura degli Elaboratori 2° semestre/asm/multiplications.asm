.data
	.word 200,34
.text
	lui t0, 0x10010
	lw t1, 0(t0)
	lw t2, 4(t0)
	bge t1, t2, t1gr 
	add a0, x0, t2
	add a1, x0, t1
	add a2, t2, x0
	addi a1, a1, -1
	jal ra, molt
	beq x0, x0, end
t1gr:   add a0, x0, t1
	add a1, x0, t2
	add a2, t1, x0
	addi a1, a1, -1
	jal ra, molt
end:	addi a7, x0, 1
	ecall
	addi a7, x0, 10
	ecall
molt:   add a0, a2, a0
        addi a1, a1, -1
        bne a1, x0, molt
        jalr x0, ra, 0
        