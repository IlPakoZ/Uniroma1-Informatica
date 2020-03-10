# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:28:12 2019

@author: xJ0T3
"""

#lista = [0,1,2,3,4,5,6,7,8,9]

def elementi_pari_indici(lista):
    lista2 = []
    for i in range(0,len(lista),2):
        lista2.append(lista[i])
    return lista2
    
def elementi_pari(lista):
    lista2 = []
    for elemento in lista:
        if int(elemento) % 2 == 0:
            lista2.append(elemento)
    return lista2

def somma_lista(lista):
    somma = 0
    for elemento in lista:
        somma+= int(elemento)
    return somma

risposta = "si"
lista = []
while (str.lower(risposta)=="si" ):
    elemento = input("Inserisci un elemento: ")
    lista.append(elemento)
    risposta = input("Scrivi 'si' per inserire un altro elemento: ")
    
print(f"La somma dei valori della lista è {somma_lista(lista)}.")
print(f"La nuova lista è (numeri pari): {elementi_pari(lista)}.")
print(f"La nuova lista è (indici pari): {elementi_pari_indici(lista)}.")


