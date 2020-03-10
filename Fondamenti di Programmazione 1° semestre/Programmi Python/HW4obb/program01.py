
''' 
    Abbiamo n stringhe di caratteri.  
    All'interno delle stringhe  e' nascosta una parola segreta come sottostringa di 
    caratteri consecutivi. 
    Sappiamo con certezza che la parola si ripete uguale esattamente una volta in ciascuna 
    stringa ma non sappiamo dove. 
    Della parola conosciamo la lunghezza M e sappiamo che non ci sono altre sottostringhe 
    di lunghezza M che si ripetono una sola volta in tutte le stringhe. 
    Vogliamo sapere per ogni stringa  la posizione dove compare il primo carattere 
    della parola nascosta.
    Ad esempio per le 6 stringhe con parola nascosta di lunghezza 3:
    
    moneta
    maratoneta
    pitone
    onesto
    storione
    sonetto
    
    la parola nascosta è 'one' e le posizioni sono nell'ordine: 1, 5, 3, 0, 5, 1
    

    
    Progettare una funzione es1(ftesto) che prende in input  un file contenente la lunghezza 
    della parola nascosta e le n stringhe di caratteri e restituisce una lista di n interi.
    L'intero in  posizione i della lista e' la posizione dove compare il primo carattere 
    della parola nascosta nella stringa i. 
    
    Le informazioni nel file ftesto sono organizzate nel seguente modo:
    - la prima riga contiene la lunghezza della parola nascosta (un intero).
    - seguono poi le stringhe di caratteri, ciascuna stringa occupa una o piu' 
    righe consecutive del file ed e' separata dalla stringa seguente da una linea vuota.
    Ogni riga del file termina con un' andata a capo.
    Vedi ad esempio il file ft1.txt che codifica l'istanza vista prima.
    
    es('ft1.txt') deve restituire la lista [1,5,3,0,5,1]    
   

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8 
    (ad esempio editatelo dentro Spyder)
   
'''

def es1(ftesto):
    lungh = 0                               #Contiene la lunghezza della sottostringa segreta
    lista = []                              #Contiene la lista di stringhe
    st = ""                                 #Contiene la stringa che viene letta
    minlength = -1                          #Memorizza la lunghezza della stringa più corta
    minst = None                            #Memorizza la stringa più corta
    with open(ftesto) as file:              #Apre il file di testo
        lungh = int(file.readline())        #Imposta la lunghezza della sottostringa segreta
        for line in file:                   #Per ogni linea nel file
            line = line.strip()             #Toglie i \n e gli spazi dalla string  
            st,minst,minlength = check_line(minlength, minst, st, line, lista) #Aggiorna i valori di "st", "minlength" e "minst"
    if st:                                  #Se la stringa non è vuota...
        lista.append(st)                    #Aggiungila, perché l'ultima stringa non viene aggiunta se non c'è un accapo alla fine.
        minst,minlength = check_if_min(st,minst,minlength) #Aggiorna i valori di "minst" e "minlength" se la lunghezza della stringa corrente è minore della lunghezza della stringa più corta 

    return find_indexes(get_key(minst,minlength,list(set(lista)),lungh),lista)  #Chiama le funzioni get_key e find_indexes e restituisci il risultato
                                            #Trasfomrare la lista in set e poi di nuovo in lista serve ad elimnare gli elementi uguali presenti più di una volta e velocizzare parecchio il processo di ricerca della chiave

def check_line(minlength, minst, st, line, lista): #Sceglie che operazione eseguire in base a se la stringa è vuota o no
    if not line:                    #Se la stringa è vuota...
        lista.append(st)            #Vuol dire che ha raggiunto un accapo, quindi la aggiunge alla lista
        minst,minlength = check_if_min(st,minst,minlength) #Aggiorna i valori di "minst" e "minlength" se la lunghezza della stringa corrente è minore della lunghezza della stringa più corta 
        st = ""                     #Svuota la stringa       
    else:                           #... altrimenti ...
        st += line                  #Questa parte di linea fa parte di un'altra stringa, quindi aggiungila
    return st,minst,minlength 


def check_if_min(st, minst, minlength):     #Controlla se la stringa corrente è più corta della stringa più corta memorizzata
    lenst = len(st)                         #Ottiene la lunghezza della stringa corrente
    if lenst < minlength or minlength == -1:#Se la lunghezza della stringa corrente è minore della lunghezza della stringa più corta o è il primo elemento che viene analizzato (nel caso la lista abbia solo un elemento)...
        minlength = lenst                   #Imposta la nuova lunghezza della stringa più corta con la lunghezza corrente
        minst = st                          #Imposta la stringa più corta con la stringa corrente
    return minst, minlength                 #Restituisce la stringa più corta con la relativa lunghezza
                  

def find_indexes(key,lista):                #Trova gli indici in cui si trova la chiave
    return [i.index(key) for i in lista]    #Restituisce gli indici in cui si trova la chiave per ogni elemento nella lista


def count_occurrences(line,lungh):      #Conta quante volte appare ogni sottostringa nell'elemento
    occourrences = {}                   #Crea un dizionario che memorizza quante volte certe sottostringhe sono presenti in uno specifico elemento della lista
    str_length = len(line)              #Ottiene la lunghezza dell'elemento
    for i in range(str_length-lungh+1): #Per ogni sottostringa nell'elemento che va dalla posizione i a i + la lunghezza della sottostringa -1...
        to_compare = line[i:i+lungh]    #L'elemento da confrontare è una di queste sottostringhe
        try:                            #Prova...
            occourrences[to_compare]+=1 #Aggiungi 1 al nnumero di volte che la sottostringa appare nella stringa
        except:                         #Se c'è un errore (di indice), vuol dire che l'elemento non era presente nel dizionario e il suo valore è None, e quindi...
            occourrences[to_compare]= 1 #Imposta a 1 il numero di volte che la sottostringa appare nella stringa
    
    return {x for x in occourrences.keys() if occourrences[x] == 1} #Restituisce l'insieme di tutte le sottostringhe che appaiono una volta nell'elemento
    

def get_key(minst,minlength,lista,lungh):   #Trova la parola segreta
    compare = {minst[i:i+lungh] for i in range(minlength-lungh+1)} #Trasforma l'elemento più corto in un insieme di sottostringhe di lunghezza pari alla parola segreta
    for line in lista:                      #Per ogni elemento della lista       
        compare = set.intersection(compare, count_occurrences(line,lungh)) #Fai l'intersezione tra "compare" e le sottostringhe appena calcolate che appaiono solo una volta nella stringa, e usa questo insieme come nuovo insieme di confronto  
        if len(compare) == 1:               #Se in compare c'è solo un elemento ...
            break                           #Allora la parola segreta è stata trovata e puoi uscire dal ciclo
    
    return compare.pop()                    #Restituisci la parola segreta
        
    
    
if __name__ == '__main__':
    # inserisci qui i tuoi test
    pass
