somma = 0
i = 1
meno =  False
for i in range(1,10000000000,2):
    if not meno:
        somma += 1 /i
        meno = True
    else:
        somma -= 1/i
        meno = False
    
print(somma*4)
