import random                                                       #importa il modulo "random"

iterations = 0                                                      #conta per quante volte si è ripetuto il programma
MAXIMUM_VALUE = 50                                                  #definisce il numero di valori generati dalla funzione (da 0 a "MAXIMUM_VALUE" - 1)
GENERATED_NUMBERS = 1000000                                         #definisce il numero di numeri casuali compresi tra 0 e "MAXIMUM_VALUE" -1 che saranno generati
STRIKE_FILTER = 4                                                   #definisce il minimo numero di volte per le quali un certo numero deve essere generato di seguito per soddisfare i requisiti
PROGRAM_ITERATIONS = 100                                            #definisce il numero di volte per le quali l'esecuzione del programma sarà ripetuta
DEBUG_MODE = False                                                  #flag per attivare o disattivare la DEBUG_MODE per sviluppatori, che mostra a schermo la stampa dei numeri trovati

                                                                    #ATTENZIONE!! L'USO DELLA DEBUG MODE RALLENTA NOTEVOLMENTE L'ESECUZIONE DEL PROGRAMMA!!
                                                                    #USARE A PROPRIO RISCHIO E PERICOLO!!

                                                                    #SI NOTI CHE UN NUMERO DI ITERAZIONI MAGGIORE PORTA AD UN ERRORE PERCENTUALE PIU' BASSO.
                                                                    #AL CONTRARIO, UNO STRIKE_FILTER PIU' ALTO PORTA AD UN AUMENTO ESPONENZIALE DELL'ERRORE.

def count():                                                        #definiamo il metodo count 

    rand = []                                                       #lista che conterrà i numeri generati casualmente
    countStrike = 1                                                 #imposta "countStrike" a 1 (lunghezza successione di due numeri uguali di fila)
    last_number = -1                                                #imposta "last_number" (il numero generato per ultimo) a -1 per evitare problemi di conteggio
    strikes = 0                                                     #imposta "strikes" a 0 (conterrà il numero di volte in cui c'è stata la generazione di almeno "STRIKE_FILTER" numeri naturali di fila
    
    for x in range(0,MAXIMUM_VALUE):                                #per ogni numero da 0 a "MAXIMUM_VALUE" ("MAXIMUM_VALUE" volte) ...
        rand.append(0)                                              #aggiungi un nuovo record nella lista e assegnagli valore zero
        
    for i in range(0,GENERATED_NUMBERS):                            #per ogni numero da 0 a "GENERATED_NUMBERS" ("GENERATED_NUMBERS" volte) ...
        generated_number = random.randint(0,MAXIMUM_VALUE-1)        #chiama la funzione "randint" del modulo "random" (genera un numero casuale da 0 a "MAXIMUM_VALUE"-1)
        if last_number == generated_number:                         #se "last_number" è uguale a "generated_number" (se il numero precedente è uguale a quello appena generato) ...
            countStrike += 1                                        #incrementa "countStrike" (allora sono stati generati "countStrike" numeri uguali di fila)
        else:                                                       #alrimenti ...
            countStrike = 1                                         #riportalo al valore di default (la successione di numeri uguali si rompe)

        if countStrike >= STRIKE_FILTER:                            #se "countStrike" è maggiore o uguale ad un certo numero ...
            if DEBUG_MODE:
                print("Il numero ", last_number, " è uscito ", countStrike ," volte di fila!")  #stampa a schermo la notifica
            strikes += 1                                            #aggiunge 1 alla variabile "strikes" (poiché il requisito è stato soddisfatto)
        last_number = generated_number                              #aggiorna la variabile "last_number" con "generated_number" (il numero precedente viene aggiornato)
        rand[generated_number] += 1                                 #aggiunge 1 al valore che nella lista corrisponde alla quantità di volte

    i = 0                                                           #inizializza la variabile indice "i"
    for x in rand:                                                  #per ogni elemento "x" presente nella lista "rand"
        if DEBUG_MODE:
            print(i, " è uscito ", x, " volte")                     #scrive per quante volte è stato generato il numero "i" ("x" volte)
        i+=1                                                        #aggiunge 1 alla variabile "i" (passa al numero successivo)

    return strikes                                                  #restituisce il valore "strikes"

sum = 0                                                             #inizializzo la variabile "sum" a 0 (conterrà la somma dei valori restituiti dalla funzione "count()")

while iterations < PROGRAM_ITERATIONS:                              #numero di volte per il quale verrà ripetuto il programma
    if DEBUG_MODE:
        print()                                                     #stampa una riga vuota (per creare spazio)
        print("Tentativo " , (iterations+1), end=" --------\n\n")   #stampa numero dell'iterazione corrente (\n serve per andare a capo)

    sum += count()                                                  #chiama il metodo (funzione) conta e somma il risultato alla variabile "sum", che lo conterrà
    if DEBUG_MODE:
        print("Fine tentativo " , (iterations+1), ".", sep='')      #fine della ripetizione
        print()                                                     #stampa una riga vuota (per creare spazio)
    iterations+=1                                                   #incrementa "iterations" (si passa alla prossima iterazione)

print("La media di numeri generati per almeno", STRIKE_FILTER, "volte di seguito è di", (sum/PROGRAM_ITERATIONS), "numeri a iterazione, ossia", sum/(PROGRAM_ITERATIONS*GENERATED_NUMBERS), "volte per numero.")

    



    
