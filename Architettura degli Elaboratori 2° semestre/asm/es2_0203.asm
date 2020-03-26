.data 
    	.word 16
     	.word 5, -2, 1, 3, 7, 4, 2, 21, 12, 1 -1, 0, 0, 7, 9, 6
.text
	lui s0, 0x10010
	lw s1, 0(s0)		#s1 contains the number of remaining elements
	lw s3, 4(s0)		#s3 contains the max number
	addi s0, s0, 8 		#s0 contains the address
	addi s1, s1, -1
loop:	lw s2, 0(s0)		#s2 contains the current number
	bgt s2, s3, great
	b ngreat 
great:	mv s3, s2
ngreat:	addi s1, s1, -1	
	addi s0, s0, 4
	bne s1, zero, loop
	mv a0, s3
	li a7, 1
	ecall
	li a7, 10
	ecall
	