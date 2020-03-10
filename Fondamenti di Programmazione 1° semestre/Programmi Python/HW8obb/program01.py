
'''
    Data una matrice di caratteri ed una word, diciamo che la  word e' presente
    nella matrice se e' possibile ottenerla collezionando i caratteri
    che si incontrano con una serie di spostamenti tra celle adiacenti.
    I soli spostamenti permessi sono:
    a) da una cella alla cella adiacente a destra (D)
    b) da una cella alla cella in basso (B)
    la word, se presente nella matrice, e'  individuata dalle coordinate
    di riga e colonna della cella da cui si parte e dalla stringa di 'D' e 'B'
    che denota la sequenza di spostamenti da effettuare per collezionare i suoi caratteri.

    Si consideri ad esempio la matrice

      ANTANDBER
      LNOANRLNT
      EIOSGEARO
      SSUNALSIC
      AANDEOAAO

    in questa matrice:
    'ANGELO' e' presente ed e' individuata da (1,3) e 'DGDGG'
    'ANDREA' e' presente ed e' individuata da (0,3) e 'DDGGD'
    'ENRICO' e' presente ed e' individuata da (0,7) e 'GGGDG'
    'ALESSANDRO', 'ANTONIO' e 'ALBERTO' sono parole non presenti.

    Abbiamo una matrice ed una lista di parole e vogliamo sapere quali sono presenti
    nella matrice e quali no.

    Progettare una funzione es1(ftesto) che preso l'indirizzo di un file
    di testo in cui e' registrata la matrice e la lista di parole da ricercare e
    restituisce una lista.
    Nella lista restituita all'i-esimo posto troviamo:
    - -1 se la word non e' presente nella matrice.
    - la posizione dell'i-esima word della lista nella matrice
      (vale a dire la terna (riga,colonna,s) con (riga,colonna) coordinate iniziali
      della cella d'inizio degli spostamenti ed s stringa che denota gli spostamenti).
      Nel caso la word sia presente piu' volte nella matrice deve essere restituita
      la posizione piu' in alto  a sinistra in cui compare e nel caso compaia
      piu' volte a partire dalla stessa casella delle diverse stringhe che
      la individuano va presa quella che precede le altre lessicograficamente.

    Ad esempio, Per la matrice vista  sopra e la lista
    ['ALBERTO','ALESSANDRO','ANDREA', 'ANGELO', 'ANTONIO', 'ENRICO']
    la funzione es1 restituira' la lista
    [-1,-1,(0,3, 'DDGGD'),(1,3, 'DGDGG'),-1,(0,7, 'GGGDG')]

    Il file ftesto  contiene  la matrice  e, di seguito  l'elenco delle parole.
    Una serie di 1 o piu'  linee vuote precede la reppresentazione della matrice,
    separa il diagramma dall'elenco delle parole e segue l'elenco delle parole.
    La matrice  e' registrata per righe (una riga per linea e in linee consecutive) gli
    elementi di ciascuna riga sono adiacenti a formare una stringa.
    La lista delle parole occupa  invece linee consecutive con  una o piu' parole o
    separate da spazi per ciascuna linea.
    Per un esempio si veda il file esempio_Disney.pdf

    NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test

    NOTA: almeno una delle funzioni realizzate DEVE essere ricorsiva, ad esempio
    potete scandire la matrice iterativamente e le lettere della word cercata ricorsivamente.

    NON usate nessuna libreria.
'''

def get_matrix(tot_testo):


    phase = 0
    index = 0
    matrix = []
    for row in tot_testo:
        element = row.strip()
        res, phase = execute_operation(element, phase, matrix)
        if res:
            break
        index += 1

    count = {c for l in matrix for c in l}
    return matrix, count, index

def execute_operation(element, phase, matrix):
    if element and phase < 2:
        matrix.append(element)
        phase = 1
        return False, phase
    elif phase == 1 and not element:
        phase = 2
        return False, phase
    elif phase == 2 and element:
        return True, phase
    return False, phase


def es1(ftesto):
    # inserite qui il vostro codice

    with open(ftesto, "r") as f:
        tot_testo = f.readlines()
    
    matrix, count, index = get_matrix(tot_testo)
    real_words = [x for x in ((" ".join(tot_testo[index:])).split())]
    words = {x: (None, None, None) for x in real_words}

    words_by_init = get_init_words(words, count)
    search_for_words(matrix, words, words_by_init)

    return [-1 if words[x] == (None, None, None) else words[x] for x in real_words]


def search_for_words(matrix, words, words_by_init):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] in words_by_init:
                check_for_words(y, x, words_by_init, matrix, words)
                if not words_by_init:
                    return 


def check_for_words(y, x, words_by_init, matrix, words):

    el = matrix[y][x]
    to_remove = set()
    for word in words_by_init[el]:
        res = recursive_check(y, x, matrix, word, 1, "")
        if res[0]:
            to_remove.add(word)
            words[word] = (y, x, res[1])
    if to_remove:
        words_by_init[el] = [x for x in words_by_init[el] if x not in to_remove]
    if not words_by_init[el]:
        del words_by_init[el]


def get_init_words(words, count):

    result = {}
    for word in words:
        char_check(word, words, count, result)
    return result


def char_check(word, words, count, result):
    for _ in word:
        if _ not in count:
            words[word] = -1
            return
    try:
        result[word[0]].append(word)
    except KeyError:
        result[word[0]] = [word]


def recursive_check(y, x, matrix, word, index, path):
    if index == len(word):
        return True, path

    el = word[index]
    try:
        to_be = matrix[y][x+1]
        if to_be == el:
            res = recursive_check(y, x+1, matrix, word, index+1, path + "D")
            if res[0]:
                return res
    except IndexError:
        pass
    try:
        to_be = matrix[y+1][x]
        if to_be == el:
            return recursive_check(y+1, x, matrix, word, index+1, path + "G")
    except IndexError:
        pass
    return [False]


if __name__ == '__main__':
    es1("big_100x40.txt")
    pass
    # inserite qui i vostri test
