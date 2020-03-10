#Fare il for in range 1,11 significa ripetere tutto ciò che è indentato dopo il for
#fino alla prima riga non indentata per 10 volte.
#ognuna di queste volte la x sarà diversa, e i suoi valori cambieranno da 1 a 10
#(l'estremo superiore del range viene ignorato)

for x in range(1,11):
	#calcolo il quadrato di x
    y = x * x
	#stampo x**x = y
    print(x, " ** ", x, end=' = ' + str(y) + "\n")

#NOTA:
#Qui la funzione print viene usata sfruttando il parametro end.
#Il parametro end specifica cosa va attaccato alla fine della stringa
#Di default equivale a "\n".
#
#Questo era solo un esempio di utilizzo del parametro end, ma generalmente
#il parametro end non si utilizza per stampare parte dell'output ma solo
#per stampare un separatore di fine stringa
#(es: un invio a capo, o un trattino in caso di più print sulla stessa riga)