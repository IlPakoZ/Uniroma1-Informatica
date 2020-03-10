# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:35:17 2019

@author: xJ0T3
"""

def operazione(op1,op2, operatore):
    operatore = str.lower(operatore)
    if operatore == "addizione":
        return op1+op2
    elif operatore == "sottrazione":
        return op1-op2
    elif operatore == "moltiplicazione":
        return op1*op2
    elif operatore == "divisione":
        if op2 is not 0:
            return op1/op2
        return "operazione non valida"
    elif operatore == "potenza":
        if op1 != 0 and op2 != 0:
            return op1**op2
        else:
            return "operazione non valida"
    else:
        return "operazione non valida"
    
op1 = int(input("Inserisci il primo numero: "))
op2 = int(input("Inserisci il secondo numero: "))
operatore = input("Inserisci l'operatore (addizione, sottrazione, moltiplicazione, divisione, potenza): ")

print(f"Il risultato dell'operazione è: {operazione(op1,op2,operatore)}.")