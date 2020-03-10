# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:57:34 2019

@author: xJ0T3
"""

def conta(lista, estremoa, estremob):
    a = set(lista)
    result = set([])
    for x in a:
        if estremoa<=x<=estremob:
            result.add(x)
    return result


def conta2(lista, estremoa, estremob):
    s = set()
    insieme = set(lista)
    for el in range(estremoa,estremob+1):
        if el in insieme:
            s.add(el)
    return s

def conta3(lista, estremoa, estremob):
    insieme = set(lista)
    estremi = set(range(estremoa,estremob+1))
    return insieme.intersection(estremi)
