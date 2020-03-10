#TESTO:
#Scrivere uno script python che prende in input tre float a, b, c,
#e calcola e stampa le due radici x dell'equazione: ax^2+bx+c = 0

import math

#input
a = float(input("Inserisci il valore di a: "))
b = float(input("Inserisci il valore di b: "))
c = float(input("Inserisci il valore di c: "))

#calcolo delle radici
risultato1 = (-b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
risultato2 = (-b - math.sqrt(math.pow(b,2)-4*a*c))/(2*a)

#stampa dei risultati
print("La prima radice vale " + str(risultato1) + ", la seconda vale " + str(risultato2) +".")
