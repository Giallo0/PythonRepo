'LESSON #3'
'''
    #1 Funzioni
    
    *Le funzioni sono blocchi di codice che può essere usato
     più volte all'interno del programma.
    *Le funzioni sono anche i comandi che usiamo spesso
     come la print(), input() ecc.
    *Per definire una funzione si scrive (def) seguito dal
     nome della funzione e () dove all'interno delle ()
     possono essere inserite delle variabili che vengono
     passate dal programma alla funzione.
    *La funzione deve essere richiamata con nome funzione e ()
     e all'interno delle tonde le variabili se sono presenti.
    *Le funzioni possono essere richiamate solo dopo essere state definite.
    *Richiamare una funzione prima della dichiarazione risulterà errore.
'''
print('LEZIONE #1')
def fun():
    print('ciao')
    print('mondo')

fun()
def fun1(num):
    num1 = num * 10
    print(num1)
a = 20
fun1(a)

'''
    #2 Argomenti di una funzione
    
    *Le variabili all'interno delle () vengono chiamate
     argomenti di una funzione.
    *Per mettere più di un argomento si separano con una (,).
    *I nomi degli argomenti sono usati solo all'interno della funzione.
    *Al di fuori possono essere assegnati variabili di nome diverso
     ma non possono essere usati i nomi delle variabili che sono all'interno
     della funzione.
'''
print('LEZIONE #2')
def print_con_esclamazione(word):
    print(word + '!')
print_con_esclamazione('ciao')
print_con_esclamazione('mondo')
print_con_esclamazione('bello')
def print_sum(x,y):
    summ = x + y
    print(summ)
print_sum(4,19)

'''
    #3 Ritorno di una funzione (Return)
    
    *Alcune funzioni di tipo int o str possono ritornare un valore
     che può essere usato più tardi.
    *Queste funzioni vengono chiamate Procedure.
    *All'interno delle procedure risiede un return che contiene un
     valore che può essere assegnato ad una variabile al di fuori
     della procedura.
    *Una volta eseguito il return, ogni codice al di sotto del return non
     viene eseguito.
'''
print('LEZIONE #3')
def massimo(x,y):
    if(x>y):
        return x
    else:
        return y
print(massimo(5,7))
z = massimo(8,2)
print(z)

def somma(x,y):
    somma = x + y
    return somma
    print('Questo non viene stampato')
print(somma(5,4))

'''
    #4 Commenti
    
    *I commenti a singola riga sono fatti con (#).
    *I commenti a più righe sono fatti con 3 di(')
     sia all'inizio che alla fine.
'''
print('LEZIONE #4')
#questo è un commento singolo
'''
    questo è un commento
    a più righe
'''

'''
    #5 Funzione come oggetto
    
    *Una funzione può essere assegnata ad una variabile.
    *In questo modo quella funzione può essere richiamata
     anche usando il nome della variabile.
    *Una funzione può essere richimata anche all'interno
     di un'altra funzione.
'''
print('LEZIONE #5')
def moltipli(x,y):
    return x*y
a=4
b=8
operazione = moltipli
print(operazione(a,b))

def add(x,y):
    return x + y
def do_twice(func, x, y):
    return func(func(x,y), func(x,y))
a = 5
b=10
print(do_twice(add,a,b))

'''
    #6 Moduli
    
    *I moduli sono pezzi di codice che sono stati scritti da altre
     persone per facilitare il comune utilizzo di funzioni più
     complesse, come ad esempio la generazione di numeri
     random è stata resa più semplice con l'utilizzo di
     un solo codice (random).
    *Il modo basico e semplice dell'utilizzo di questi moduli
     avviene nominandolo in alto al codice con (import) nome_modulo.
    *Dopodichè si avrà la disponibilità delle funzioni al suo interno.
    *Per nominare una funzione: nome_modulo.var.
    *In questo caso viene importato il modulo random.
    *In questo modo posso utilizzare la funzione random.randint(), che mi
     permette di generare un numero casuale intero.
    *Se all'interno dell () non viene messo niente verrà generato un numero
     casuale infinito.
    *Se all'interno dell () vengono messi due numeri verrà generato un numero
     nel range.
    *Esiste anche un altro metodo di import che viene usato solo quando
     ci serve una sola funzione del metodo (se ce ne servono ad esempio due dello
     stesso modulo si può usare una ,).
    *In questo caso si dichiara il modulo in questo modo:
     from nome_modulo import var.
    *Quindi in questo caso si può importare solo la funzione (pi) (pigreco)
     del metodo (math).
    *Si può importare una funzione sotto un nome diverso usando (as) (nuovo_nome).
'''
print('LEZIONE #6')
import random
for i in range(5):
    valore = random.randint(1,6)
    print(valore)
from math import pi
print(pi)

from math import sqrt as radice_quadrata
print(radice_quadrata(144))

'''
    #7 Libreria standard e il pip
    
    *Ci sono vari tipi di moduli che si possono scrivere da noi stessi
     oppure installarli da risorse esterne o che sono già integrate
     in python.
    *Quest'ultimo tipo di moduli si chiamano standard library.
    *Si possono scaricare moduli da terze parti chiamate
     Python Package Index (PyPI).
    *Per scaricarli e installarli su python bisonga avere pip.
    *Grazie a pip e la linea di comando del pc si possono
     scaricare in modo efficente i moduli per python.
'''
print('LEZIONE #7')
