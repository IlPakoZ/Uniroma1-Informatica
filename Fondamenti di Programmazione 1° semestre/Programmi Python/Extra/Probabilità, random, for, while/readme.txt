-------------------------------------------------------------------------------------

Author: IlPakoZ
Date: 04/08/2019
GitHub: https://github.com/IlPakoZ

----------------------------------- DESCRIZIONE -------------------------------------

Questo programma serve principalmente a calcolare le probabilità di un 
numero qualsiasi generato casualmente di essere generato un certo numero 
di volte di fila. 
Questa probabilità viene poi messa in relazione con il numero di iterazioni,
di numeri generati e del range di valori che questi numeri generati in modo
casuale possono assumere.

Attraverso le funzionalità del programma sono state effettuate delle 
misure e tabulate in un file Excel.

E' stata osservata una determinata correlazione tra il numero di valori
che soddisfano i requisiti della variabile filtro, la variabile filtro stessa,
le volte in cui il programma ripete la sua esecuzione (che chiameremo 
iterazioni), la quantità di numeri che si vuole generare e l'ampiezza dell'insieme
dei valori che essi possono acquisire.

--------------------------------- DICHIARAZIONI -------------------------------------

MAXIMUM_VALUE = 

				Definisce il numero di valori casuali generati dalla funzione 
			    (da 0 a "MAXIMUM_VALUE" - 1)
				
				ATTENZIONE: Si chiama MAXIMUM_VALUE perché indica il valore
				massimo che può assumere un numero generato casualmente dalla
				funzione "randint" del modulo "random". 
				Questa funzione infatti, accetta due parametri:
				- il primo, che indica il valore minimo che può assumere il numero
				generato;
				- il secondo, che indica il valore massimo che può assumere il numero
				generato.
				
				Pertanto, i numeri generati andranno da 0 a "MAXIMUM_VALUE" - 1.
				Si è deciso di iniziare a contare proprio da 0 per rendere più semplice
				e intuitiva la trasposizione dei valori nella lista "rand[]", usando
				quindi lo stesso sistema di indici di una lista o raccolta qualsiasi.
				
GENERATED_NUMBERS =

				Definisce il numero di numeri casuali compresi tra 0 e 
				"MAXIMUM_VALUE" -1 che saranno generati per ogni iterazione. 
				
				E' importante tenere a mente che un numero più alto assegnato
				a questa costante indica sì maggiore precisione nella misura, ma 
				anche un maggior dispendio di tempo nell'esecuzione del programma.
				
STRIKE_FILTER =

				Definisce il minimo numero di volte per le quali un certo numero deve 
				essere generato di seguito per poter esseere preso in considerazione.
				
				Un valore alto significa diminuire esponenzialmente le probabilità di
				generazione di sequenze che soddisfino i requisiti, pertanto bisogna
				fare attenzione al valore che si assegna alla costante.
				
				Per maggiori dettagli sulle probabilità di uscita di "STRIKE_FILTER"
				valori uguali di seguito in base al valore del filtro stesso, 
				consultare il file Excel e fare riferimento alla colonna "Fila (>=)".
				
PROGRAM_ITERATIONS = 

				Definisce il numero di volte per le quali l'esecuzione del programma 
				sarà ripetuta.
				
				Dato il fattore casuale della generazione, per avere un valore più
				affidabile e accurato possibile la generazione dei valori viene
				ripetuta più volte e viene poi fatta una media della somma dei valori
				ottenuti da ciascuna iterazione.

				Pertanto, un valore più alto assegnato a questa costante indica
				certamente una diminuzione dell'errore percentuale, ma anche
				un tempo di esecuzione "PROGRAM_ITERATIONS" volte superiore.
				
DEBUG_MODE = 
				
				Flag per attivare o disattivare la DEBUG MODE per sviluppatori, 
				che mostra a schermo la stampa dei numeri trovati.
				
				La DEBUG MODE, aggiunta nell'ultima versione del programma,
				prima non era implementata. 
				
				Questo significa che, ogni volta che si voleva eseguire il programma
				venivano stampati sullo schermo in tempo reale i valori che
				erano generati per almeno "STRIKE_FILTER" volte di seguito con il
				rispettivo contatore.
				
				Con la DEBUG MODE, se impostata su False (come di default), questa
				feature può essere disattivata.
				
				In più, la DEBUG MODE permette di visualizzare per quante volte
				ogni numero da 0 a "MAXIMUM_VALUE" - 1 viene generato casualmente,
				per permettere un ulteriore studio statistico.
				
				Però, questa continua stampa di output sullo schermo è un'operazione
				molto lenta e che rallenta SIGNIFICATIVAMENTE l'esecuzione del
				programma.
				
				Pertanto, mentre prima per disattivare la stampa di questi valori extra
				occorreva commentare manualmente il codice indesiderato, adesso basta 
				semplicemente porre la costante "DEBUG_MODE" a "False" (viceversa,
				a "True" per attivarla".
				
				ATTENZIONE!!
				L'USO DELLA DEBUG MODE RALLENTA NOTEVOLMENTE L'ESECUZIONE DEL PROGRAMMA.
				USARE A ROPRIO RISCHIO E PERICOLO!
				
iterations = 

				"iterations" è una variabile che conta in quale iterazione il programma
				si trova in tempo reale (ossia per quante volte il programma ha ripetuto
				la sua esecuzione fino a quel momento).
				
				Quando il valore della variabile diventa uguale a "PROGRAM_ITERATIONS",
				il programma si trova alla sua ultima iterazione ed esegue il suo
				payload per l'ultima volta prima di fermarsi e stampare i risultati.
				
count() =
				
				"count()" è il nome di una funzione che non accetta parametri e 
				restituisce il valore di "strikes".
				
				Una funzione è una porzione di codice che esegue determinate operazioni
				e restituisce un risultato. 
				Richiamando una funzione non si fa altro che richiamare il codice al suo
				interno.
				Una funzione può essere richiamata più volte semplicemente scrivendo 
				il nome della funzione e ponendo tra parentesi i parametri specificati
				durante la sua definizione.
				
				L' "if" statement pone una condizione ed esegue le operazioni soltanto 
				se la condizione specificata dopo la parola chiave "if" restituisce vero.
				In caso contrario, si passa all'esecuzione delle istruzioni racchiuse in 
				"elif" (se specificata e le condizioni che lo seguono sono vere) ed else 
				(se specificata).
				
				"countStrike" è una variabile che conta il numero di numeri con lo
				stesso valore generati di fila in tempo reale, e che viene resettata a
				1 ogni volta che il numero nell'ultima generazione è differente dal 
				numero precedente.
				
				Il numero della precedente generazione viene conservato in "last_number",
				e di default è impostato a -1 per segnalare che non esiste alcun numero
				precedente (perché si tratta della prima generazione).
				
				Dalla seconda generazione in poi, il valore generato (posto in
				"generated_number") viene confrontato con il valore precedente:
				- se i due valori sono uguali, vuol dire che lo stesso numero
				è uscito per due volte di fila, quindi incrementa "countStrike";
				- se i due valori sono differenti, "countStrike" viene reimpostato
				a uno. 
				
				In qualunque caso, il numero precedente diventa "generated_number" e 
				viene posto in "last_number" così che nela prossima generazione 
				il programma confronterà il nuovo valore generato con il corretto
				precedente.
				
				Questa serie di operazioni si ripete durante tutto il programma.				
				
				Si controlla poi che il valore di "countStrike" sia MAGGIORE o UGUALE
				al valore di "STRIKE_FILTER" (si sta quindi controllando se i numeri 
				sono usciti per abbastanza volte di fila per essere conteggiati).
				
				IMPORTANTE: Porre molta attenzione al MAGGIORE o UGUALE.
				Questo infatti significa che, se "STRIKE_FILTER" è impostato a 2
				e un numero viene generato per 3 volte di seguito, la condizione
				sarà verificata comunque.
				
				Per trovare le probabilità di generare per un numero fisso di volte 
				un numero qualsiasi di seguito, basta togliere dalla condizione il MAGGIORE
				e aggiungere un ulteriore "=" per impostare la condizione di uguaglianza 
				o in alternativa fare dei semplici calcoli sul file Excel.
				
				Per esempio, per trovare la probabilità di un numero di uscire ESATTAMENTE
				due volte di fila, basta sottrarre alle probabilità di un numero di uscire
				almeno due volte di fila quelle di uscire almeno tre volte di fila.
				
				Infine, "strikes" conterrà il numero di volte in cui la condizione 
				è stata soddisfatta e ci permetterà infine di calcolare le probabilità.
				

---------------------------------- OSSERVAZIONI -------------------------------------

Si osserva che, come già specificato, numeri generati, range, il numero di valori che devono
essere estratti di fila sono tutte variabili collegate tra loro attraverso una formula.

La formula ricavata è questa: GENERATED_NUMBERS / (MAXIMUM_VALUE ^ (STRIKE_FILTER-1))
(generazioni per iterazione).

Questo avviene perché, attraverso il principio moltiplicativo della combinatoria,
le probabilità di uscita del primo numero sono il 100%, perché il numero può
essere un numero qualsiasi, mentre il secondo numero ha 1 fratto il numero di numeri generabili 
di possibilità di essere uguale al primo. Il terzo numero, a sua volta, ha 1 fratto il numero
di numeri generabili di possibilità di essere uguale al secondo e così via.

La formula ricavata è pertanto quella specificata sopra.

E' possibile notare che le difficoltà di trovare un tot di numeri di seguito aumentano
esponenzialmente proprio per la natura stessa della formula, a parità di numeri generabili e
del dominio di valori che essi possono assumere. 

E' possibile anche osservare che un errore relativo più alto è dovuto ad una scarsa quantità di
iterazioni in relazione al numero di numeri di fila da misurare.
Una soluzione potrebbe essere quella di aumentare i campi "GENERATED_NUMBERS" o "ITERATIONS",
ma questo rallenterebbe di molto l'esecuzione del programma.
