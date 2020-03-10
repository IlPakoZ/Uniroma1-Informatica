# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:43:10 2019

@author: xJ0T3
"""

def sortThis(s):
    lista = s.split(",")
    lista.sort(key = lambda x: len(x.split(" ")),reverse = True)
    return lista