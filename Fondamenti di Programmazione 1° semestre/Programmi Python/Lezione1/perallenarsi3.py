#Scrivere uno script python che prende in input due float a e b
#e calcola e stampa c, corrispondente all'ipotenusa del triangolo rettangolo
#avente per cateti due lati di lunghezza a e b, rispettivamente

import math

#input
a = float(input("Inserisci la base del triangolo rettangolo: "))
b = float(input("Inserisci l'altezza del triangolo rettangolo: "))

#calcolo e stampa
print("L'ipotenusa è: " + str(math.sqrt(a*a+b*b)))

#NOTA:
#math.sqrt è la funziona per la radice quadrata