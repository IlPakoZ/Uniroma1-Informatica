#TESTO:
#Scrivere un programma che prende due numeri da input utente e ne stampa la somma

#Input dei due numeri
A=int(input("Inserisci il valore di A: "))
B=int(input("Inserisci il valore di B: "))

#stampa della somma
print(A+B)

#NOTA:
#la funzione input permette di stampare la stringa che gli viene passata
#e di far inserire all'utente un valore.
#
#Purtroppo non capisce in automatico il tipo di dato in input, perciò restituisce sempre una stringa
#per convertire il valore di input in un numero si può usare la funzione int(valore_non_numerico)
#che trasforma in un valore numerico una stringa (es: "123" => 123)