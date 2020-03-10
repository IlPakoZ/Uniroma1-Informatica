#TESTO:
#scrivere due funzioni per calcolare le radici di un equazione di secondo grado

import math

#funzione per la radice con il +
def radice1():  
    return (-b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    
#funzione per la radice con il -
def radice2():
    return (-b - math.sqrt(math.pow(b,2)-4*a*c))/(2*a)

#prova per testare che le funzioni  
a = float(input("Inserisci il valore di a: "))
b = float(input("Inserisci il valore di b: "))
c = float(input("Inserisci il valore di c: "))

print("La prima radice vale ", radice1())
print("La seconda radice vale ", radice2())


