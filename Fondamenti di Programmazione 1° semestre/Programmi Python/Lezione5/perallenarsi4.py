# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:37:54 2019

@author: xJ0T3
"""

def is_ordered(lista = []):
    newLista = sorted(lista)
    if (newLista == lista):
        return True
    return False