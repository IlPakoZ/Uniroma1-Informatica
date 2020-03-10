# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:00:11 2019

@author: xJ0T3
"""

def sconto (prezzo, percentuale):
    return prezzo - prezzo*percentuale/100

prezzo = float(input("Inserisci il prezzo del prodotto (€): "))
percentuale = float(input("Inserisci lo scconto percentuale (%): "))

print(f"Il prezzo scontato è di {sconto(prezzo,percentuale)} €" )