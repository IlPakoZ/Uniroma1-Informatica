#TESTO:
#Scrivere uno script python che prende in input tre float a, b, c,
#e calcola e stampa l'espressione:
#         b^3*c^4
# a^2 +  ---------  -b + a*c
#            3a

import math

#input
a = float(input("Inserisci il valore di a: "))
b = float(input("Inserisci il valore di b: "))
c = float(input("Inserisci il valore di c: "))

#calcolo del risultato
risultato = math.pow(a,2)+ math.pow(b,3)*math.pow(c,4)/(3*a)-b+a*c

#output
print("L'espressione a^2 + (b^3*c^4)/3a -b + a*c vale: " + str(risultato))