def lunghezza_parole(frase):
    lista = []
    for parola in frase.split(' '):
        lista.append(len(parola))

    return lista

