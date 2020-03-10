# -*- coding: utf-8 -*-
''' 
    In un immagine a sfondo nero  e' disegnata  una griglia  
    dove  alcuni segmenti che ne connettono i nodi in orizzontale 
    o in verticale sono stati cancellati (i nodi della griglia sono in 
    verde mentre i segmenti sono in rosso).
    La dimensione del lato dei quadrati della griglia non è data.

    Si veda ad esempio la figura foto_1.png.
    Progettare la funzione es1(fimm, k) che prende in input l'indirizzo 
    dell'immagine contenente la griglia ed un intero k e restituisce un intero. 
    L'intero restituito e' il numero di 
    quadrati rossi (con pixel verdi) di lato k (steps della griglia) che sono presenti nell'immagine.
    Ad esempio  es1(foto_1.png,2) deve restituire 2 (i due quadrati rossi presenti nella 
    sottogriglia hanno il vertice in alto a sinistra con coordinate (3,0) e 
    (4,2) nelle coordinate della griglia, rispettivamente)

    Per caricare e salvare  file PNG si possono usare load e save della libreria immagini allegata.

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)

'''
import immagini

def es1(fimm,k):
    
    img = immagini.load(fimm)                                           #Contiene l'immagine caricata
    width = len(img[0])                                                 #Contiene la larghezza dell'immagine
    height = len(img)                                                   #Contiene l'altezza dell'immagine
    gap = 0                                                             #Contiene quanti pixel di gap ci sono tra un punto della griglia e l'altro
    right_boundary_index = None                                         #Contiene la posizione in cui si trova l'ultimo pixel della griglia a destra
    bottom_boundary_index = None                                        #Contiene la posizione in cui si trova l'ultimo pixel della griglia in basso
    x_starting_index = None                                             #Contiene la posizione in cui si trova l'indice x del primo pixel
    y_starting_index = None                                             #Contiene la posizione in cui si trova l'indice y del primo pixel
    
    y_index, x_index, x_starting_index, y_starting_index = first_grid_node(img,height,width) 

    if x_starting_index == None:                                        #Se il primo pixel della griglia non è stato trovato...
        return 0                                                        #...allora la griglia è vuota, restituisci 0

    right_boundary_index, gap = get_gap(img, x_index, y_index, x_starting_index, y_starting_index, width, height)

    if not gap:                                                         #Se il gap non è stato ancora trovato
        if k:                                                           #Se k è un numero diverso da 0
            return 0                                                    #...allora restituisci zero
        else:                                       
            return 1                                                    #...altrimenti restituisci uno
        
    if not right_boundary_index == x_starting_index:                    #Se la griglia NON è larga uno...:                                           
        right_boundary_index = get_right_boundary(img, x_starting_index, y_starting_index, width, gap)  #Ottiieni l'ultimo pixel destro della griglia  
    
    bottom_boundary_index = get_bottom_boundary(img, x_starting_index, y_starting_index, height, gap)   #Ottieni l'ultimo pixel inferiore della griglia
    ins = get_possible_x_segments(img, x_starting_index, y_starting_index, right_boundary_index, bottom_boundary_index, gap, k) #Ottiene la lista dei possibili quadrati
    if not len(ins):                                                    #Se l'insieme è vuoto...
        return 0                                                         #...allora restituisci 0
    if len(ins) > ((right_boundary_index-x_starting_index)//gap-k) * ((bottom_boundary_index-y_starting_index)//gap) // 8:    #Se ci sono parecchi possibili quadrati allora utilizza un metodo alternativo e in questo caso più rapido
        ins_y = get_possible_y_segments(img, x_starting_index, y_starting_index, right_boundary_index, bottom_boundary_index, gap, k)   #Insieme          
        return count_intersection(ins,ins_y,k)                          #Restituisce il numero dei quadrati
    return count_squares(img, ins,x_starting_index, y_starting_index, gap,k)    #Restituisce il numero dei quadrati
    
def count_intersection(ins_x,ins_y,dim):
    count = 0                                                           #Inizializza il contatore a zero
    for el in ins_y:                                                    #Per ogni segmento nell'insieme y
        if (el[1],el[0],el[0]+dim) in ins_x:                            #Se esiste la sua altezza nell'insieme x
            count+=1                                                    #Conta +1
    return count
    

def count_squares(img, ins, x_starting_index, y_starting_index, gap, dim):
    count = 0                                                           #Setta il contatore a zero
    for el in ins:                                                      #Per ogni segmento dell'insieme
        y = el[0]                                                       #Ottieni la coordinata y del piano in cui si trova
        x = el[1]                                                       #Ottieni la x in cui inizia
        
        if not get_square_by_segments(img,x,y,x_starting_index,y_starting_index,dim,gap):    #Se invece la variabile non è cambiata, vuol dire che i segmenti sono stati trovati e i segmenti formano un quadrato
            count+=1                                                    #Conta un quadrato in più
                
    return count

def get_square_by_segments(img,x,y,x_starting_index,y_starting_index,dim,gap):
    for _x in range(x*gap + x_starting_index, (x+dim)*gap + x_starting_index+1,dim*gap):    #Controlla tra la prima e l'ultima riga    
        for _y in range(y*gap + y_starting_index,(y+dim)*gap + y_starting_index,gap):       #Per ogni pixel tra quelli non ancora verificati
            if not img[_y+1][_x] == (255,0,0):                          #Se il colore non è rosso
                return True            
    return False                                                        #Conta un quadrato in più
    
def get_possible_x_segments(img, x_starting_index, y_starting_index, right_boundary_index, bottom_boundary_index, gap, dim):  
    ins = set()                                                         #Crea un insieme che conterrà tuple di valori
    count = 0                                                           #Conta a partire da 0
    for y in range(y_starting_index, bottom_boundary_index+1, gap):     #Ci spostiamo verticalmente per ogni pixel della griglia
        starting_x = x_starting_index                                   #Imposta l'indice da cui inizia a contare all'indice iniziale
        for x in range(x_starting_index, right_boundary_index+1, gap):  #Ci spostiamo verticalmente per ogni pixel orizzontale della griglia
            if is_red(img,x+1,y):                                       #Se il pixel a destra del nodo è rosso...
                count+=1
            else:    
                count = 0                                               #Se non è rosso, allora resetta il contatore (finisce lo strike di indici)
                starting_x = x+gap 
            if count == dim:                                            #Se sono stati collegati dim nodi di seguito
                ins.add(((y-y_starting_index)//gap,(starting_x-x_starting_index)//gap,(x-x_starting_index)//gap + 1))   #Aggiungi una tupla contenente la componente y dove è stato trovato il segmento, la componente x da cui parte e quella in cui finisce                                    
                count -= 1                                              #Decrementa di uno il contatore, riprendi a contare dal punto in cui sei arrivato
                starting_x = starting_x+gap                             #Il nuovo punto di partenza è quello precedente più il gap tra un pixel e l'altro
        count = 0                                                       #Resetta il contatore
         
    return {x for x in ins if (x[0]+dim, x[1], x[2]) in ins}            #Mantieni i segmenti nell'insieme solo se, a "dim" di distanza per ogni segmento, c'è un altro segmento                                                     #Restituisce l'insieme


def is_red(img,x,y):
    try:
        if img[y][x] == (255,0,0):                                       #Se il pixel a destra del nodo è rosso...
            return True                                                 #Restituisci True
    except IndexError:
        pass
    return False                                                        #Altrimenti restituisci False
    
def get_possible_y_segments(img, x_starting_index, y_starting_index, right_boundary_index, bottom_boundary_index, gap, dim):  
    ins = set()                                                         #Crea un insieme che conterrà tuple di valori
    count = 0                                                           #Conta a partire da 0
    
    for x in range(x_starting_index, right_boundary_index+1, gap):      #Ci spostiamo verticalmente per ogni pixel della griglia
        starting_y = y_starting_index                                   #Imposta l'indice da cui inizia a contare all'indice iniziale
        for y in range(y_starting_index, bottom_boundary_index+1, gap): #Ci spostiamo verticalmente per ogni pixel orizzontale della griglia
            if is_red(img,x,y+1):                                       #Se il pixel in basso del nodo è rosso...
                count+=1                                                #...allora conta che la lunghezza del segmento trovata è 1 in più a quella precedente
            else:
                count = 0                                               #Se non è rosso, allora resetta il contatore (finisce lo strike di indici)
                starting_y = y+gap                                      #Il nuovo indice da cui iniziare a contare è quello successivo
  
            if count == dim:                                            #Se sono stati collegati dim nodi di seguito
                ins.add(((x-x_starting_index)//gap,(starting_y-y_starting_index)//gap,(y-y_starting_index)//gap + 1))  #Aggiungi una tupla contenente la componente x dove è stato trovato il segmento, la componente y da cui parte e quella in cui finisce                                   
                count -= 1                                              #Decrementa di uno il contatore, riprendi a contare dal punto in cui sei arrivato
                starting_y = starting_y+gap                             #Il nuovo punto di partenza è quello precedente più il gap tra un pixel e l'altro
        count = 0                                                       #Resetta il contatore

    return {x for x in ins if (x[0]+dim, x[1], x[2]) in ins}          #Mantieni i segmenti nell'insieme solo se, a "dim" di distanza per ogni segmento, c'è un altro segmento

def get_right_boundary(img, x_starting_index, y_starting_index, width, gap):
    for x in range(x_starting_index, width, gap):                       #Per ogni pixel orizzontale della griglia...
        if not img[y_starting_index][x] == (0,255,0):                   #Se il pixel non è più verde...
            return x-gap                                                #Ho trovato la posizione del primo pixel da destra, puoi restituire il valore
    return width-1                                                      #...allora è perché è l'ultimo pixel orizzontale dell'immagine, quindi impostalo come la larghezza dell'immagine -1 


def get_bottom_boundary(img, x_starting_index, y_starting_index, height, gap):
    for y in range(y_starting_index, height, gap):                      #Per ogni pixel verticale della griglia
        if not img[y][x_starting_index] == (0,255,0):                   #Se il pixel non è più verde...
            return y-gap                                                #Ho trovato la posizione dell'ultimo pixel verticalmente, puoi uscire dal ciclo
    return height -1                                                    #...allora è perché è l'ultimo pixel verticale dell'immagine, quindi impostalo come l'altezza dell'immagine -1
    

def get_gap(img, x_index, y_index, x_starting_index, y_starting_index, width, height):
    gap = get_gap_horizontally(img, x_index, x_starting_index, y_starting_index, width)
    
    if not gap:                                                         #Se il gap non è stato trovato...
        right_boundary_index = x_starting_index                         #...allora la griglia è larga 1 pixel.
        gap = get_gap_vertically(img, y_index, x_starting_index, y_starting_index, height)  #Prova ad ottenere il gap verticalmente
        return right_boundary_index, gap
    return None, gap


def get_gap_horizontally(img, x_index, x_starting_index, y_starting_index, width):    
    for x in range(x_index, width):                                     #Finché l'indice x è minore della larghezza dell'immagine
        if img[y_starting_index][x] == (0,255,0):                       #Se il pixel in quella posizione è verde (è un punto della griglia)...
            return x - x_starting_index                                 #...allora il gap tra un pixel e l'altro della griglia è pari alla differenza tra i loro indici
    return 0


def get_gap_vertically(img, y_index, x_starting_index, y_starting_index, height):
    for y in range(y_index,height):                                     #Finchè l'indice y è minore dell'altezza dell'immagine
        if img[y][x_starting_index] == (0,255,0):                       #Se il pixel in quella posizione è verde (è un punto della griglia)...
            return y - y_starting_index                                 #...allora il gap tra un pixel e l'altro della griglia è pari alla differenza tra i loro indici, questa volta però verticalmente
    return 0


def first_grid_node(img,height,width):
        
    for y_index in range(0,height):                                     #Per tutta l'altezza dell'immagine...
        for x_index in range(0,width):                                  #Per tutta la larghezza dell'immagine...
            if img[y_index][x_index] == (0,255,0):                      #Se il pixel in quella posizione è verde (è un punto della griglia)...
                x_starting_index = x_index                              #Memorizza l'indice x del primo pixel della griglia
                y_starting_index = y_index                              #Memorizza l'indice y del primo pixel della griglia
                return y_index, x_index+1, x_starting_index, y_starting_index  #Incrementa l'indice x in modo da prendere il pixel che si trova subito dopo
    return None, None, None, None        


if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test
