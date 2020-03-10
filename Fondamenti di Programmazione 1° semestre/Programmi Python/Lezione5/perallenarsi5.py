# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:44:07 2019

@author: xJ0T3
"""
import math

def lista_complementi_100(lista = []):
    complementi = []
    for x in lista:
        complementi.append(int(math.pow(100,math.ceil(math.log(x,100))) - x))
    return complementi

        
