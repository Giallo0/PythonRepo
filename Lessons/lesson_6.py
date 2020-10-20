'LESSON #6'
'''
    #1 Programmazione funzionale
    
    *Consiste nella programmazione
     con l'utilizzo di funzioni.
    *La chiave di un programma funzionale
     è funzioni di ordine superiore
     (higher order functions).
    *Ovvero nel richiamare una funzione
     dentro un argomento di un'altra
     funzione.
    *Le funzioni possono essere pure e impure:
        pure -> Sono funzioni che non modificano le variabili
                ma le usano per avere un ritorno da usare
                tutte le volte che si vuole; In più
                il valore di ritorno dipende solo dai suoi
                argomenti.
        impure -> Sono funzioni che modificano lo stato
                  di una variabile esterna.
'''
print('LEZIONE #1')
def apply_twice(func,arg):
    return func(func(arg))
def add_five(x):
    return x + 5
print(apply_twice(add_five,10))
#pura
def pure_func(x,y):
    temp = x + 2*y
    return temp / (2*x + y)
#impura
some_list = []
def impure_func(arg):
    some_list.append(arg)
print(pure_func(3,4))
impure_func(4)
print(some_list)

'''
    #2 Lambdas
    
    *Il lambda è una funzione anonima, ovvero
     creata sul momento, senza nessun nome.
    *è utile quando ad esempio si deve passare
     una funzione come argomento.
    *L'unica caratteristica è che di solito sta
     su una riga quindi è una funzione molto piccola.
    *Il lambda è formato da la parte iniziale prima dei
     (:) dove vengono dichiarati gli argomenti,
     la seconda parte dove è presente il blocco codice
     ed infine la terza parte separata dalla prima
     dove si passano i valori agli argomenti.
    *Il lambda può essere assegnato ad una variabile e
     usata come una normale funzione.
'''
print('LEZIONE #2')
def my_func(f,arg):
    return f(arg)
my_func(lambda x: 2*x*x, 5)

#funzione
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))
#lambda
print((lambda x: x**2 + 5*x + 4)(-4))
print((lambda x,y: x**2 + 5*y +4) (-4,2))
double = lambda x: x * 2
print(double(7))

'''
    #3 map e filter
    
    *Operano sulle liste o su oggetti simili
     chiamati iterabili(iterables).
    *Il loro funzionamento è:
        map -> prende come argomenti una funzione e
               una iterabile (tipo lista) e ritorna
               una nuova iterabile con le operazioni
               della funzioni applicate per ogni argomento
               della lista.
        filter -> filtra un iterabile rimuovendo
                  oggetti che non soddisfano la
                  funzione booleana (ovvero
                  rimuove tutti quelli che ritornano
                  un False).
'''
print('LEZIONE #3')
def agg_cinque(x):
    return x + 5
num = [11,22,33,44,55]
result = list(map(agg_cinque,num))
print(result)
#Si può fare lo stesso utilizzando il lambda
num = [11,22,33,44,55]
result = list(map(lambda x: x+5, num))
print(result)

num = [11,22,33,44,55]
res = list(filter(lambda x: x%2 == 0, num))
print(res)

'''
    #4 Generatori
    
    *I generatori sono tipi di iterabili, come
     le liste e i tuples.
    *Diversamente dalle liste, non sono indicizzati
     e il contenuto può essere visualizzato
     attraverso un for loop.
    *Possono essere creati usando funzioni e (yield).
    *I generatori non hanno una restrizione di memoria,
     per questo sono infiniti.
    *Generatori di numero finito possono essere convertiti
     in liste passandolo come argomento alla funzione list.
'''
print('LEZIONE #4')
def countdown():
    i=5
    while i> 0:
        yield i
        i -=1
for i in countdown():
    print(i)

#def infinito():
#    while True:
#        yield 7
#for i in infinito():
#    print(i)
li = list(countdown())
print(li)

'''
    #5 Decoratori
    
    *I decoratori provvedono a un modo di modificare
     le funzioni usando altre funzioni.
    *è utile quando si ha bisogno di estendere le
     funzionalità di funzioni che non hai bisogno di modificare.
    *In poche parole, si usa quando abbiamo una funzione
     che non abbiamo bisogno di modificare, perchè potrebbe
     servirci in quel modo, ma quando dobbiamo modificarla
     possiamo inserirlo all'interno di un'altra funzione.
    *In questo modo non andremo ad intaccare la funzione
     utilizzata precedentemente alla modifica, ma l'avremmo
     modificata per i successivi utilizzi alla modifica.
    *Utilizzando la (@) seguita dal nome della funzione
     del decoratore, richiamando il nome della funzione
     del testo, si avrà la la modifica effettuata.
'''
print('LEZIONE #5')
#senza @
def decorator(func):
    def wrap():
        print('==========')
        func()
        print('==========')
    return wrap

def testo_stampa():
    print('ciao mondo')

testo_stampa = decorator(testo_stampa)
testo_stampa()
#con @
def decor(func):
    def wrap():
        print('===========')
        func()
        print('===========')
    return wrap

@decor
def print_text():
    print('Hello world')

print_text()

'''
    #6 Ricorsioni
    
    *Le ricorsioni sono un concetto molto importante
     nella programmazione.
    *La parte fondamentale delle ricorsioni è
     referenziare se stessa, ovvero una funzione
     richiama se stessa affinchè non si risolve un
     problema suddiviso in sottoproblemi dello stesso tipo.
    *Un esempio classico di funzioni ricorsive è la
     funzione fattoriale, il quale trova il prodotto
     di numeri positivi più piccoli di un certo numero.
    *Esempio 5! (5 fattoriale) = 5 * 4 * 3 * 2 * 1 (120).
    *Quindi in una funzione fattoriale sarebbe:
        5! = 5 * 4!, 4! = 4 * 3!, e cosi via
        quindi n! = n * (n-1)!
        fin quando 1! = 1.
    *In una funzione ricorsiva è importante stabilire il caso
     base, ovvero il caso che blocca la ricorsione e permette
     di risolvere i problemi precedenti.
    *Senza il caso base, si continuerebbe all'infinito (loop).
    *Una ricorsione può essere anche indiretta, ovvero una funzione
     può richiamarne un'altra e viceversa.
'''
print('LEZIONE #6')
def fattoriale(x):
    if x == 1:
        return 1
    else:
        return x * fattoriale(x-1)
print(fattoriale(5))

def e_pari(x):
    if(x==0):
        return True
    else:
        return e_dispari(x-1)
def e_dispari(x):
    return not e_pari(x)

print(e_dispari(17))
print(e_pari(23))

'''
    #7 Sets
    
    *I set sono strutture di dati simili alle liste o
     ai dizionari.
    *Sono creati con {} o con la funzione set.
    *Condividono alcune funzionalità delle liste
     come l'uso dell'(in) e (not in) per verificare la presenza di
     un valore all'interno.
    *Per creare un set vuoto si mettono le {}.
    *A differenza di un dizionario, all'interno delle
     {} vanno messi direttamente i valori senza chiave.
    *Differiscono dalle liste in diversi modi, ma come detto prima
     condividono alcune operazioni come (len).
    *Non hanno una indicizzazione, quindi sono anche senza chiave.
    *Non possono contenere elementi doppioni.
    *Quindi è più facile controllare se un elemento fa parte di un set
     piuttosto che di una lista.
    *Ci sono vari comandi per i set:
        add -> aggiunge un elemento al set e lo accoda alla
               fine.
        remove -> rimuove un elemento specifico dal set.
        pop -> rimuove il primo elemento.
    *In oltre il set ordina i valori dal più piccolo
     al più grande, e i numeri negativi li sposta a li
     sposterà alla destra sempre dal più piccolo
     al più grande.
    *Se al suo interno sono presenti doppioni,
     ne visualizzerà solo uno.
    *I set possono essere combinati con operazioni
     matematiche:
         unione (|) -> combina due set e ne forma uno contenente
                       elementi di entrambi (i doppioni una volta sola).
         intersezione (&) -> prende elementi che si trovano sia nel primo
                             che nel secondo set.
         differenza (-) -> prende elementi dal primo set che non ci sono
                           nel secondo.
         differenza simmetrica (^) -> prende elementi che non sono uguali
                                      in entrambi i set.
    *Abbiamo visto molti tipi di struttura dati:
        liste;
        dizionari;
        tuples;
        sets.
    *I dizionari possono essere usati:
        1 -> quando abbiamo bisogno di una associazione logica
             tra chiave:valore
        2 -> quando abbiamo bisogno di conservare un dato,
             basandoci su una chiave
        3 -> quando i nostri dati sono in continua modifica.
    *Usiamo gli altri tipi per:
        1 -> usiamo le liste se abbiamo un insieme di dati
             che non necessitano di un accesso randomico, e
             quando modifichiamo spesso i dati all'interno.
        2 -> usiamo i set se abbiamo bisogno di unicità
             per gli elementi.
        3 -> usiamo i tuples quando i nostri dati non cambiano;
             spesso i tuples sono usati insieme ai dizionari
             come chiavi essendo immutabili.
'''
print('LEZIONE #7')
num_set = {1,2,3,4,5}
word_set = set(['prosciutto','uova','salsiccia'])
print(3 in num_set)
print('prosciutto' not in word_set)
li = ['cacca','pupu','bebe']
word_set = set(li)
print(word_set)

num = {1,2,1,3,1,4,5,-5,6}
print(num)
num.add(-4)
print(num)
num.remove(3)
print(num)
num.pop()
print(num)

primo = {1,2,3,4,5,6}
secondo = {4,5,6,7,8,9}
print(primo | secondo)
print(primo & secondo)
print(primo - secondo)
print(secondo - primo)
print(primo ^ secondo)

'''
    #8 itertools
    
    *Il modulo itertools è una libreria standard
     che contiene diverse funzioni che sono
     utili alla programmazione.
    *Tra queste ci sono:
        count -> conta fino all'infinito partendo da un
                 valore definito.
        cycle -> Ripete fino all'infinito gli elementi
                 di un iterabile (o stringa). Viene passato
                 come argomento l'iterabile.
        repeat -> ripete un oggetto, infinite o un certo
                  numero specificato di volte; (gli si passano
                  due argomenti rispettivamente: il valore da
                  ripetere e il numero di ripetizioni);
                  i valori vanno messi in una lista.
    *Ci sono altre funzioni simili a (map) e (filter) che
     operano sugli iterabili.
    *Tra queste ci sono:
        takewhile -> prende gli elementi dagli iterabili i quali
                     da una condizione risultano True.
        chain -> combinano diversi iterabili dentro una sola.
        accumulate -> ritorna un eseguimento totale dei valori
                      in un iterabile; in poche parole,
                      genera dei numeri che vanno messi in una lista;
                      questi numeri partono da 0 e i successivi
                      verranno generati seguendo questa logica:
                          n = 0
                          n = n+1
                          n = n+2
                          n = n+3
                          ecc.
                      vengono generati tanti numeri quanto vale il
                      range messo come argomento all'accumulate.
                      Se il range a due argomenti (range(x,y))
                      allora sarà:
                          n = x
                          n = n+(x+1)
                          n = n+(x+2)
                          n = n+(x+3)
                          ecc.
                      fino a che non si arriva alla quantità di valori
                      z ovvero: z = (y-x)
    *Ci sono anche diverse funzioni combinatrici tra cui:
        product -> Permette di accoppiare tutte le possibili
                   combinazioni tra una lista e un range di numeri
                   o di stringhe o un'altra lista.
        permutation -> Permette di eseguire tutte le possibili
                       combinazioni tra gli elementi di una lista.
'''
print('LEZIONE #8')
from itertools import count,cycle,repeat
#count
for i in count(3):
    print(i)
    if (i >=11):
        break
print('===================')
#cycle
res = cycle([2,5,1])
cnt = 0
for i in res:
    print(i)
    cnt += 1
    if(cnt>=10):
        break
print('===================')
#repeat
rip = list(repeat(11,5))
print(rip)
print('===================')
from itertools import takewhile,chain,accumulate
#accumulate
del num
del li
num = list(accumulate(range(10)))
print(num)
li = list(accumulate(range(3,10)))
print(li)
print('===================')
#takewhile
print(list(takewhile(lambda x:x<=6,num)))
print('===================')
#chain
li1 = [2,5,7,1,3,6]
li2 = [6,3,6,8]
li3 = list(chain(li1,li2))
print(li3)
print('===================')
from itertools import product,permutations
#product
lettere = ('A','B')
lettere3 = ('C','D')
print(list(product(lettere, range(3))))
print(list(product(lettere, lettere3)))
print('===================')
#permutations
lettere2 = ('A','B','C')
print(list(permutations(lettere)))
print(list(permutations(lettere2)))
