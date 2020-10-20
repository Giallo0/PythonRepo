'LESSON #5'
'''
    #1 None
    
    *L'oggetto None è usato per rappresentare
     l'assenza di valore.
    *Simile al null in altri programmi.
    *None è il 'non valore' di ritorno
     di una funzione che non ritorna niente.
'''
print('LEZIONE #1')
print(None)
def func():
    print('ciao')
var = func()
print(var)

'''
    #2  Dizionario
    
    *I dizionari sono strutture di dati
     usati per mappare arbitrariamente i
     valori con una chiave.
    *I dizionari possono essere richiamati
     allo stesso modo delle liste con
     il nome e la chiave tra [].
    *Per valorizzare un dizionario si mettono
     {} e all'interno chiave:valore.
    *La separazione tra le chiavi avviene con (,).
    *Un dizionario può contenere ogni tipo di dato.
    *Un dizionario vuoto è definito con {}.
'''
print('LEZIONE #2')
eta = {'Luca':19, 'Paolo':25, 'Mario':15}
print(eta['Paolo'])
print(eta['Luca'])
colori = {
             'red':[255,0,0]
            ,'green':[0,255,0]
            ,'blue':[0,0,255]
         }
print(colori['red'])
print(colori['blue'][2])

'''
    #3  Funzioni del dizionario
    
    *Come le liste si possono riassegnare
     i valori, specificando la chiave e
     mettere il nuovo valore.
    *Per i dizionari si può aggiungere anche un nuovo valore
     con una nuova chiave non esistente.
    *Per determinare se è presente una chiave all'interno
     di un dizionario si può usare (in) e (not in).
    *Un altro metodo utile per i dizionari è il (get).
    *Il get permette di cercare la chiave e di stampare
     il valore.
    *Se non trova la chiave stampa di default None,
     oppure si può inserire come secondo argomento
     un messaggio.
'''
print('LEZIONE #3')
dic = {1:1, 2:4, 3:'error', 4:16}
print(dic)
dic[3] = 9
dic[8] = 64
print(dic)
print(1 in dic)
print(16 in dic)
print(4 not in dic)
print(dic.get(4))
print(dic.get(7))
print(dic.get(13231, 'non nel dizionario'))

'''
    #4 Tuples
    
    *Tuples è simile alle liste ma
     la differenza è che non possono
     essere cambiati i valori.
    *I Tuples si formano mettendo le ()
     al posto delle [] come nelle liste.
    *Si possono anche creare senza ()
     ma separando semplicemente le variabili con (,).
    *Un Tuples vuoto si forma con ().
'''
print('LEZIONE #4')
parole = ('casa','albero','due')
print(parole[2])
parole2 = 'asso','fermo','cibo'
parole3 = ()
print(parole2[0])

'''
    #5 list slices

    *Si usa per prelevare un pezzo di dati
     da una lista.
    *In poche parole, avendo una lista con tot
     valori si possono prendere una certa quantità di dati
     inserendo le posizioni da a.
    *Si indicizza mettendo tra [] la posizione di partenza (compreso)
     seguito da (:) e seguito da la posizione di arrivo (non compreso).
    *Se viene ommesso il primo valore, si parte dall'inizio
     fino alla posizione indicata.
    *Se viene ommesso il secondo valore, si parte dalla posizione indicata
     fino alla fine.
    *list slices può essere eseguito anche su Tuples.
    *list slices può avere anche un terzo argomento.
    *Questo rappresenta lo step di lettura.
    *Se si usa un numero negativo nel secondo argomento
     toglierà valori dalla fine.
    *Quindi partirà dalla posizione indicata fino
     alla posizione finale meno il valore indicato.
    *Se Sia il primo che il secondo argomento sono negativi
     allora si partirà dalla fine (il primo argomento deve essere
     più piccolo del secondo, quindi ad esempio -5 e -1).
    *Se il terzo argomento è negativo, stamperà i valori
     dalla fine verso l'inizio (però si devono invertire il
     primo e il secondo argomento se positivi).
    
'''
print('LEZIONE #5')
num = [4,5,1,6,3,7,2,7,2,35]
print(num[2:6])
print(num[0:1])
print(num[:5])
print(num[6:])
val = (2,5,7,21,2,1,7,3)
print(val[4:7])
print(val[::2])
print(val[1:6:2])
print(val[1:-2])
print(val[-5:-1])
print(val[6:2:-1])
print('Mattia'[::-1])

'''
    #6 Liste di comprensione
    
    *Sono metodi validi per generare velocemente
     una lista con delle regole.
    *Può essere implementato un if per rinforzare
     la condizione per la creazione della lista.
    *Quando il range è troppo elevato si verifica un
     errore di (out of memory) ovvero si stanno
     elaborando troppi numeri più di quanto
     la memoria può fare.
'''
print('LEZIONE #6')
radici_cubiche = [i**3 for i in range(5)]
print(radici_cubiche)
num_pari = [i*5 for i in range(10) if i**5 % 2 == 0]
print(num_pari)
#pari = [i*2 for i in range(10**100)]

'''
    #7 Formattazione stringhe
    
    *Per combinare una stringa con una non-stringa
     si può usare il cast.
    *Oppure c'è un altro metodo, il format.
    *Si forma mettendo all'interno della stringa
     i numeri degli argomenti messi dentro il format.
    *Può funzionare anche mettendo il nome della variabile.
'''
print('LEZIONE #7')
num = [4, 5, 6]
msg = 'Numeri: {0} {1} {2}'.format(num[0], num[1], num[2])
print(msg)
msg = '{x} != {y}'.format(x=4, y=7)
print(msg)

'''
    #8 Funzioni utili
    
    *Python contiene molte funzioni e metodi utili.
    *Tra queste ci sono:
        join -> consente di inserire tra più stringhe un'altra stringa
        replace -> consente di rimpiazzare una stringa o un carattere
                   con un'altro (stringa_vecchia, stringa_nuova).
        startswith -> determina se una stringa inizia per una stringa determinata.
        endswith -> determina se una stringa finisce per una stringa determinata.
        lower ->  mette tutti i caratteri in minuscolo.
        upper -> mette tutti i caratteri in maiuscolo.
        split -> è il contrario del join, divide la stringa con un certo separatore.
    *Ci sono anche funzioni numeriche.
    *Tra i quali:
        max -> trova il massimo di una lista di numeri.
        min -> trova il minimo di una lista di numeri.
        abs -> trova la distanza assoluta dal numero allo 0.
        round -> arrotonda il numero da un numero decimale
                 a un numero più vicino intero.
                 Se si mette il secondo argomento farà vedere il
                 numero decimale tanto quanto vale l'argomento.
        sum -> trova la somma di una lista di numeri.
    *Ci sono funzioni anche per le liste.
    *Tra i quali:
        all -> Prende come argomento la lista e ritorna vero (True)
               se tutti gli argomenti hanno rispettato la condizione.
        any -> Prende come argomento la lista e ritorna vero (True)
               se nessun argomento ha rispettato la condizione.
        enumerate -> enumera gli oggetti all'interno della lista.
'''
print('LEZIONE #8')
#join
print(', '.join(['luca','ciccio','mario']))
li = ['pino','matto','rino']
print('; '.join(li))
st = 'vai a cagare'
print(st)
#replace
st = st.replace('cagare','fanculo')
print(st)
st = st.replace('a','_')
print(st)
#startswith e endswith
print('Questa è una domanda'.startswith('Questa'))
print('Questa è una domanda'.endswith('fine'))
#upper e lower
print(st.upper())
print(st.lower())
#split
print('cicca, mamma, sesamo, luca'.split(', '))
#min
print(min(1,5,4,6,7,0,9,2,6))
#max
print(max(1,5,4,6,7,0,9,2,6))
#abs
print(abs(41))
print(abs(-13))
#round
print(round(35.543))
print(round(35.543,2))
#sum
print(sum([1,5,4,6,7,0,9,2,6]))
#all, any ed enumerate
num = [55,44,33,22,11]
if all([i>5 for i in num]):
    print('tutti i numeri maggiori di 5')
if any([i % 2 == 0 for i in num]):
    print('nessun numero pari')
for v in enumerate(num):
    print(v)

'''
    #9 Analizzatore di testo
    
    *Si può analizzare un testo andando da un semplice
     controllo di quante spunta un carattere al suo interno
     a fornire una percentuale di quanto occupa quel
     carattere all'interno del file.
'''
print('LEZIONE #9')
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

with open('Content/file4.txt') as f:
    text = f.read()
    
text_fix = text.replace(' ','')
text_fix = text_fix.replace('\n','')
for char in 'abcdefghijklmnopqrstuvwxyz':
    perc = 100 * count_char(text, char)/len(text_fix)
    print('{0} - {1}%'.format(char,round(perc,2)))
