    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende come argomento una stringa contenente una serie di parole (sequenze di caratteri separate da spazi bianchi, tabulazioni o a capo) e un intero e ritorna il numero di parole presenti nella stringa che hanno una lunghezza esattamente pari all'intero preso come argomento
"""

def conta_parole(stringa, lunghezza):
    conta = 0
    lista = stringa.split()
    for x in lista:
        if len(x) == lunghezza:
            conta+=1
    return conta
#    scrivere qui il codice
