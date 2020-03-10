# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 10:29:49 2019

@author: xJ0T3
"""

def dizionari(s):
    x = s.split()
    d = {}
    
    for element in x:
        i = len(element)
        if(i in set(d.keys())):
            d[i]+=1
        else:
            d[i]=1
        
    print(d)
    
dizionari("questa è una prova scema")