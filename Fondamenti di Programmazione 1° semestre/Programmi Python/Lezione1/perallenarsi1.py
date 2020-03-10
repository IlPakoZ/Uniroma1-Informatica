#TESTO:
#Scrivere uno script python che prende in input un numero float,
#ne calcola la radice cubica e la stampa a video
import math

a = float(input("Inserisci un numero reale: "))

print("La radice cubica di " + str(a) + " è: " + str(math.pow(a,1/3)))

#NOTA:
#Qui è stata usata la funzione math.pow, la cui funzione è fare la potenza del primo argomento con il secondo
#Utilizzare math.pow(a,b) è del tutto equivalente a fare a**b

#NOTA 2:
#Fare la radice x-esima di un numero equivale ad elevarlo a 1/x
#es: radice cubica = 1/3