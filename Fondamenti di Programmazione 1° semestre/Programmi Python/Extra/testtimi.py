# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:23:00 2019

@author: xJ0T3
"""

def estrai_parole(testo):

    nonalfa = [c for c in set(testo) if not c.isalpha]
    t = testo
    for c in set(nonalfa):
        t = t.replace(c," ")
    return t.split()
