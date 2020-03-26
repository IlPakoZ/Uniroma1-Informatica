.data
d:	.word 4
m:	.word 5, 9, 0, 6
	.word 4, -3, 2, 4
	.word 9, 1,-2, 3
	.word -1, 3, 5, 7
.text
	la t0, m		#Address of the first element 
	li t1, 4
	lw s0, d 	#Width/Height of the square matrix
	addi s1, s0, 1	
	mul s1, s1, t1	#Address increment	
	li s2, 0 	#Current index
loop:	lw s3, 0(t0)    #Loads the element at the index
	add a0, a0, s3
	add t0, t0, s1
	addi s2, s2, 1
	blt s2, s1, loop
	li a7, 1
	ecall
	li a7, 10
	ecall