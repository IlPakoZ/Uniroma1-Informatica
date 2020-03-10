# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:18:16 2019

@author: xJ0T3
"""

def check_date(g,m,a):
    if (m < 1 or m > 12):
        return False
    if (m<8 and m%2 == 1) or (m>7 and m%2 == 0):
        if(g>31):
            return False
    else:
        if(m == 2):
            if(a%4 == 0):    
                if(g>29):
                    return False
            else:
                if(g>28):
                    return False
        else:
            if(g>30):
                return False
    return True
            
            
    