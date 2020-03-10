# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:17:02 2019

@author: xJ0T3
"""



def recursive():
    sei_stupido = input("Questa affermazione è falsa (s/n): ")
    if sei_stupido == "s":
        print("Questa affermazione non è falsa, perché dicendo sì stai ammettendo che l'affermazione dice il vero.")
        recursive()
    elif sei_stupido == "n":
        print("Questa affermazione non può essere vera, perché dicendo che è vera, stai ammettendo che l'affermazione è falsa.")
        recursive()
    elif sei_stupido == "?":
        print("Questa è una affermazione quantistica, questo significa che è sia vera che falsa finché non la misuri.")
    
    
recursive()