# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:07:33 2019

@author: xJ0T3
"""

SCONTO_MEDIO = 0.2
SCONTO_ALTO = 0.3

def spesa(costo, studenti):
    if studenti >= 10 and studenti <= 30:
        costo = costo - costo * SCONTO_MEDIO
    elif studenti > 30:
        costo = costo - costo * SCONTO_ALTO
    return costo * studenti

costo = float(input("Inserisci il costo del biglietto per studente: "))
numero_studenti = int(input("Inserisci il numero di studenti: "))

print(f"\nLa spesa totale è di {spesa(costo, numero_studenti)}€.")