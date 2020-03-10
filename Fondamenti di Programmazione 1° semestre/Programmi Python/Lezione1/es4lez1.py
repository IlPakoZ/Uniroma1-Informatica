#TESTO:
#Scrivere un programma che presi in input base e altezza di un rettangolo
#Ne stampi perimetro ed area

#input di base ed altezza
A = int(input("Inserisci la base del rettangolo: "));
B = int(input("Inserisci l'altezza del rettangolo: "));

#calcolo del perimetro e dell'area
perimetro = 2*(A + B)
area = A*B

#stampa dei risultati
print("Il perimetro del rettangolo è: " + str(perimetro));
print("L'area del rettangolo è: " + str(area));
