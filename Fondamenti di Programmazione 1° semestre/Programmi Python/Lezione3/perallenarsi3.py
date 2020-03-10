# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:17:26 2019

@author: xJ0T3
"""
COSTO_BIGLIETTO_MASCHI = 12
COSTO_BIGLIETTO_FEMMINE = 10

def spesa(maschi,femmine):
    return maschi * COSTO_BIGLIETTO_MASCHI + femmine * COSTO_BIGLIETTO_FEMMINE

maschi = int(input("Inserisci il numero di maschi: "))
femmine = int(input("Inserisci il numero di femmine: "))
print(f"Il costo totale è di {spesa(maschi,femmine)}€.")