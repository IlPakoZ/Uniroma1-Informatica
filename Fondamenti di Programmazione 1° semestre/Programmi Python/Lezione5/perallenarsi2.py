# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:45:29 2019

@author: xJ0T3
"""

def diff_pari_dispari(lista = []):
    somma_pari = 0
    somma_dispari = 0
    
    for x in lista:
        if x % 2 == 0:
            somma_pari+=x
        else:
            somma_dispari+=x
    """
    for i in range(0,len(lista)):
        x = lista[i]
        if x % 2 == 0:
            somma_pari+=x
        else:
            somma_dispari+=x
       """        
    return somma_pari-somma_dispari
        
    