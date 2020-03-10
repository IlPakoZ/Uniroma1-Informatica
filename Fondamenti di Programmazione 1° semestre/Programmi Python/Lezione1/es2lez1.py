#TESTO: Scrivere un programma che preso in input il raggio di un cerchio
#ne calcoli e ne stampi l'area e la circonferenza

import math

#input del raggio
raggio = float(input("Inserisci il raggio del cerchio: "))

#calcolo area e circonferenza a partire dal raggio che mi è stato dato in input
circonferenza = raggio*2*math.pi
area = raggio**2*math.pi

#stampo i risultati che ho calcolato
print("La circonferenza del cerchio è: " + str(circonferenza))
print("L'area del cerchio è: " + str(area))

#NOTA1:
#l'istruzione import, importa il  modulo math,
#per utilizzare funzioni o variabili del modulo math una volta importato in questo modo
#basta scrivere: nome_modulo.nome_della_cosa_da_utilizzare
#(es: math.pi per il pi greco)

#NOTA 2:
#come nello scorso esercizio era stato utilizzato int() per convertire il valore dell'input
#in un numero intero, in questo esercizio è stato utilizzato float() per convertire il
#valore dell'input in un numero a virgola mobile.

#NOTA 3:
# ** è l'operatore di elevazione a potenza, quindi scrivere a**b significa a elevato alla b

#NOTA 4:
#Così com'è necessario convertire una stringa di input in un numero è anche necessario convertire
#un numero in una stringa per poterlo poi concatenare ad una stringa con l'utilizzo dell'operatore +
#la funzione print può anche essere usata passando più parametri per evitare di dover fare queste
#conversioni es: print("Ciao, questo è un numero:",numero)