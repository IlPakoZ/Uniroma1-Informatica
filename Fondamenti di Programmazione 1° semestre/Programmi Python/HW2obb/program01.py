# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:29:20 2019

@author: Pako
"""

def es(lista1, lista2):
    
    #NB: lista1 è la lista contenente tutte le operazioni (s1,s2,e1,e2,... sono considerate "operazioni")
    #    lista2 invece contiene gli ID dei piloti in ordine di posizione dal primo all'ultimo
    
    lista2_len = len(lista2) #Ottieni la lunghezza di lista2
    lista1_len = len(lista1) #Ottieni la lunghezza di lista1
    first_element = lista2[0] #Memorizza il primo elemento della lista
    
    piloti_posizioni = {lista2[elt]:  [lista2[elt-1],lista2[elt+1]] for elt in range(1,lista2_len-1)} #crea il dizionario che ha come elementi l'elemento precedente e quello successivo
    piloti_posizioni[lista2[0]] = [None, lista2[1]] #setta il primo elemento del dizionario che ha come precedente None e come successivo il secondo elemento
    piloti_posizioni[lista2[-1]] = [lista2[-2],None] #setta l'ultimo elemento del dizionario che ha come precedente il penultimo e come successivo None
    
    first_element = calculate(first_element,lista1,lista1_len,piloti_posizioni) #esegui i calcoli
    
    newList = []
    while first_element != None: #finché non raggiungi l'ultimo elemento
        newList.append(first_element) #aggiungi a newList l'elemento
        first_element = piloti_posizioni[first_element][1] #passa all'elemento successivo
    return newList #restituisci newList

def calculate(first_element,lista1,lista1_len,piloti_posizioni): #calcola gli indici e restituisce il primo in classifica
    item = 0
    while item < lista1_len:                #per ogni operazione in lista1_len
        operation = lista1[item][0]         #setta come operazione da eseguire il primo carattere dell'elemento in indice "item" nella lista1
        elt = int(lista1[item][1:])         #setta come elemento su cui operare dal secondo carattere in poi dell'elemento  in indice "item" nella lista1
        first_element, item = chain(operation, lista1, piloti_posizioni, item+1, elt, first_element) #chiama il metodo "chain" che verifica se esistono "catene" di operazioni
    return first_element                    #restituisce il primo elemento

def chain(operation, lista1, piloti_posizioni, item, elt, first_element):
    prev_elt = elt                          #"prev_elt" memorizzerà l'elemento che in classifica precede elt. All'inizio, è uguale ad elt
    next_elt = elt                          #"next_elt" memorizzerà l'elemento che in classifica succede elt. All'inizio, è uguale ad elt
    backup_prev_elt = None                  #memorizza l'elemento successivo a "prev_elt"
    
    if operation == 's':                    #Se è una operazione di scambio...
        next_elt = piloti_posizioni[elt][1] #setta il pilota successivo come il pilota che succede elt in classifica
        while True:                         #Finché non incontra un break...
            next_pilot = "-1"               #Il pilota successivo su cui bisogna eseguire una operazione è "-1". E' importante che sia "-1" che non sia None perché, 
                                            #nel caso in cui anche "prev_elt" assumesse valore None, questi non verrebbero considerati lo stesso elemento più avanti nel programma.
                                            #E' anche importante che il "-1" sia di tipo stringa perché nel caso esistesse veramente un pilota con ID "-1", essendo convertito il valore in intero,
                                            #verrebbero considerati come due elementi diversi comunque
            
            next_op = None                  #L'operazione successiva da eseguire è None.
            try:
                next_op = lista1[item][0]   #L'operazione successiva da eseguire è l'elemento successivo nella lista1.
                                            #Viene preso l'elemento successivo perché, nella chiamata del metodo, l'argomento "item" viene passato incrementato di 1.
            except:
                                            #Se l'operazione non va a buon fine, vuol dire che lista1 è finita.
                pass                        #Pertanto next_pilot rimarrà con valore "-1" e verrà portata a termine l'operazione di scambio.
           
            backup_prev_elt = prev_elt      #Memorizza prev_elt
            prev_elt = piloti_posizioni[prev_elt][0] #Prende il pilota precedente al pilota precedente
            if operation == next_op:        #Se l'operazione originale corrisponde all'operazione successiva (quindi se anche l'operazione successiva è di scambio)... 
                next_pilot = int(lista1[item][1:]) #Il pilota successivo su cui bisogna eseguire un'operazione è il pilota scritto nella seconda parte dell'operazione
            
            if prev_elt == next_pilot:      #Se prev_elt, il pilota precedente, è uguale al pilota successivo su cui bisogna eseguire l'operazione...
                item+=1                     #Incrementa item, quindi esegui lo stesso procedimento eseguito fino ad ora
            else:                           #...altrimenti, i piloti differiscono e chiama l'operazione di scambio
                first_element = exchange(piloti_posizioni, backup_prev_elt, prev_elt, elt, next_elt, first_element)
                break
    else:                                   #... altrimenti deve essere un'operazione di eliminazione
        
        if prev_elt != None: prev_elt = piloti_posizioni[prev_elt][0] #Se prev_elt vale None, potrebbero crearsi problemi di Indice nella continuazione del codice, quindi vengono gestiti in modo diverso.
        if next_elt != None: next_elt = piloti_posizioni[next_elt][1] #Se next_elt vale None, potrebbero crearsi problemi di Indice nella continuazione del codice, quindi vengono gestiti in modo diverso.
        
        #NB: è importante che l'assegnazione iniziale di prev_elt e next_elt avvenga fuori dal ciclo perché il programma funzioni.
        #Infatti, oltre a comportare un dispendio di tempo (poiché le operazioni verrebbero eseguite ad ogni ciclo), causerebbe
        #una esecuzione anomala di queste operazioni ogni volta che prev_elt o next_elt rispettivamente sono diversi da None.
        #Il programma infatti, non ragiona nello stesso modo dei sorpassi: mentre i sorpassi possono avvenire soltanto in un verso,
        #eliminazioni a catena (ossia quando vengono eliminati elementi vicini) possono avvenire sia verso l'alto che verso il basso.
        #Mettere pertanto queste due assegnazioni nel ciclo significherebbe gestire in maniera diversa anche il controllo di ugualianza tra l'elemento successivo o l'elemento precedente con il pilota a cui si riferisce l'operazione successiva,
        #risultando così nella necessità di ulteriori if che avrebbero diminuito le prestazioni del programma.

        while True:                         #Finché non incontra un break...

            next_pilot = "-1"                #Il pilota successivo su cui bisogna eseguire una operazione è "-1". E' importante che sia "-1" che non sia None perché, 
                                            #nel caso in cui anche "prev_elt" assumesse valore None, questi non verrebbero considerati lo stesso elemento più avanti nel programma.
                                            #E' anche importante che il "-1" sia di tipo stringa perché nel caso esistesse veramente un pilota con ID "-1", essendo convertito il valore in intero,
                                            #verrebbero considerati come due elementi diversi comunque
            
            next_op = None                  #L'operazione successiva da eseguire è None.
            try:
                next_op = lista1[item][0]   #L'operazione successiva da eseguire è l'elemento successivo nella lista1.
                                            #Viene preso l'elemento successivo perché, nella chiamata del metodo, l'argomento "item" viene passato incrementato di 1.
            except:
                                            #Se l'operazione non va a buon fine, vuol dire che lista1 è finita.
                pass                        #Pertanto next_pilot rimarrà con valore "-1" e verrà portata a termine l'operazione di scambio.

            if operation == next_op:        #Se l'operazione originale corrisponde all'operazione successiva (quindi se anche l'operazione successiva è di eliminazione)... 
               next_pilot = int(lista1[item][1:]) #Il pilota successivo su cui bisogna eseguire un'operazione è il pilota scritto nella seconda parte dell'operazione
            
            if next_pilot == prev_elt:      #Se prev_elt, il pilota precedente, è uguale al pilota successivo su cui bisogna eseguire l'operazione...
                prev_elt = piloti_posizioni[prev_elt][0] #Prende il pilota precedente al pilota precedente
            elif next_pilot == next_elt:    #Se next_elt, il pilota successivo, è uguale al pilota successivo su cui bisogna eseguire l'operazione...
                next_elt = piloti_posizioni[next_elt][1] #Prende il pilota successivo al pilota successivo
            else:                           #... altrimenti esegui la rimozione
                first_element = remove(piloti_posizioni, prev_elt, next_elt, first_element)  
                break
            item+=1

    return first_element, item

def remove(piloti_posizioni, prev_elt, next_elt, first_element): #rimuove gli elementi
    if next_elt == None and prev_elt == None: 
        return None                         #Se sia next_elt che prev_elt sono None, vuol dire che la lista è vuota, quindi restituisce None
    try:
        piloti_posizioni[prev_elt][1] = next_elt 
    except:
        first_element = next_elt            #Se questa operazione fallisce, vuol dire che prev_elt = None, vuol dire che il precedente era il primo elemento, quindi il nuovo primo elemento sarà next_elt 
    try:
        piloti_posizioni[next_elt][0] = prev_elt 
    except:
        pass                                #Se questa operazione fallisce, vuol dire che next_elt = None, vuol dire che il precedente era l'ultimo elemento
    
    return first_element
        
def exchange(piloti_posizioni, backup_prev_elt, prev_elt, elt, next_elt, first_element):
    
    #NB: E' importante rendersi conto che prev_elt contiene sempre l'elemento che precede l'ultima ugualianza trovata tra prev_elt e next_pilot.
    #L'utilità di avere una variabile di backup (backup_prev_elt) sta nel fatto che viene memorizzato il pilota su cui è valida l'ultima ugualianza
    #in modo tale da eseguire lo scambio solo tra il pilota elt e il pilota backup_prev_elt, e modificare i valori degli indici di chi li precede e chi li succede.
    #Commentare queste operazioni non serve, basta farsi uno schema su come gli indici vengono scambiati per capire il procedimento usato.
    
    piloti_posizioni[backup_prev_elt][0] = next_elt 
    piloti_posizioni[elt][1] = piloti_posizioni[next_elt][1]
    try:
        piloti_posizioni[prev_elt][1] = next_elt 
    except:
        first_element = next_elt   #Se questa operazione fallisce, vuol dire che prev_elt = None. Questo significa che elt era il primo elemento. Poiché elt viene scambiato con next_elt, next_elt è il nuovo primo elemento.
    try:
        piloti_posizioni[piloti_posizioni[next_elt][1]][0] = elt
    except:
        pass                       #Se questa operazione fallisce, vuol dire che piloti_posizioni[next_elt][1] = None. Questo significa che next_elt era l'ultimo elemento. Poiché next_elt viene scambiato con elt, elt è il nuovo ultimo elemento. 
    piloti_posizioni[next_elt][0] = prev_elt    
    piloti_posizioni[next_elt][1] = backup_prev_elt
    return first_element
    