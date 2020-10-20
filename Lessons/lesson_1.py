'LESSON #1'
'''
    #1 Stampa
    
    *Per stampare si usa il print.
    *Essendo un testo si usano le ''.
    *In python l'interruzione di riga non c'è.
'''
print('LEZIONE #1')
print('hello world')
print('my name is Mattia')

'''
    #2 Semplici operazioni
    
    *Le operazioni possono essere direttamente inserite all'interno di
     una print.
    *Le parentesi dicono quale operazione deve essere eseguita prima.
    *La divisione (/) risulta un numero decimale.
    *Le operazioni sono:
        Addizione:       +
        Sottrazione:     -
        Moltiplicazione: *
        Divisione:       /
    *La divisione per 0 fornisce un errore.
'''
print('LEZIONE #2')
print(5+6)
print(4-2*4)
print(12-(5+2))
print(12/6)
'print(4/0)'

'''
    #3 Numeri decimali (Floats)
    
    *Come prima, la divisione fornisce un numero decimale.
    *Per avere un numero decimale basta inserire o in una operazione
     o in una variabile un valore con virgola(.).
'''
print('LEZIONE #3')
print(5/6)
print(5.4+4)
print(2.2*1.2)

'''
    #4 Altre operazioni
    
    *Esistono anche altre operazioni.
    *Queste operazioni sono:
        Esponenziale: **
        Quoziente:    //
        Modulo:       %
'''
print('LEZIONE #4')
print(2**5)
print(144**(1/2))
print(20//6)
print(81//6)
print(20%6)
print(1.25%0.5)

'''
    #5 Stringhe (Strings)
    
    *Le stringhe si usano per scrivere frasi.
    *Si usano le '' per inserire all'interno una stringa.
    *Alcuni caratteri non possono essere inseriti perchè possono
     fare contrasto (come ad esempio le ').
    *In questo caso si usa la backslash (\) seguita dal carattere.
    *Per andare a capo in una frase, e quindi fare una multi riga,
     si usa (\n); oppure si usa (""") sia all'inizio che alla fine.
'''
print('LEZIONE #5')
print('Questo è python')
print('Python è molto bello')
print('La mamma disse \'come ti permetti\' e Luca si zittì')
print('Uno \nDue \nTre')
print("""Quattro
Cinque
Sei""")

'''
    #6 Operatori di stringhe
    
    *Ci sono operatori per le stringhe.
    *Le stringhe possono essere anche numeri ma preceduti e seguiti da (').
    *Questi sono:
        Concatenazione: +
        Multiplicazione: *
'''
print('LEZIONE #6')
print('Cassa' + 'Panca')
print('2' +'3')
print('cibo' *3)
print(4* '2')

'''
    #7 Variabili
    
    *Le variabili permettono di storare un valore
     assegnandogli un nome in modo da poterlo usare
     con un nome specifico per quel dato.
    *Per assegnare un valore ad una varibile si
     scrive il nome della variabile seguito da un (=) e
     il valore, che può essere stringa o numerico.
    *Come abbiamo visto, si possono concatenare anche una stringa
     con una variabile.
    *Si possono usare le variabili anche per fare delle operazioni
     numeriche.
    *Usate direttamente nel print, le variabili non conserveranno il
     valore finale.
    *Se si da un nuovo valore ad una variabile qualsiasi già esistente,
     questa perderà il valore precedente e acquisirà il nuovo valore.
    *I nomi delle variabili non possono iniziare con numeri.
    *I caratteri ammessi per il nome di una variabile sono:
        Lettere;
        Numeri (ma non iniziale);
        Underscores.
    *Se non seguono queste regole risulterà errore.
    *Si può usare (del) per eliminare una variabile.
    *Questa non può essere più richiamata a meno che non si
     riassegna un nuovo valore.
    *Se viene richiamata quando la variabile è stata eliminata
     causerà errore.
'''
print('LEZIONE #7')
utente = 'Mattia'
print('Benvenuto ' + utente)
x = 2
print(x)
print(x*2)
print(x)
y = 423.56
print(y)
y = 'Sono diventato una stringa'
print(y + '!')
a = 4
print(a)
'del a'
'print(a)'
a=6
print(a)
del a

'''
    #8 Input
    
    *L'input è l'inserimento o un comando da parte dell'utente.
    *Per avere un input si richiama la funzione (input).
    *Il risultato dell'input sarà una stringa.
    *La funzione (input) deve essere seguita da parentesi tonde
     il quale sarà un messaggio di input.
    *Come abbiamo già detto, il risultato di un input è una stringa.
    *Se vogliamo che il nostro input sia numerico dobbiamo fare il cast,
     ovvero convertire il valore da stringa a numerico.
    *Per fare il cast basta semplicemente mettere prima del input il formato
     cui vogliamo trasformare il valore.
    *Al contrario si può fare il cast da numerico intero a stringa con (str).
    *Questo serve per concatenare una stringa ad un valore numerico.
'''
print('LEZIONE #8')
print('scrivi:\n')
x = input()
print('Hai scritto:\n' + x)
y = input('Scrivi qualcosa:\n')
print('Hai scritto:\n' + y)
eta = int(input('Inserisci la tua età: '))
print(eta + 20)
print('La tua età è: ' + str(eta))

'''
    #9 Operatori in-place

    *Gli operatori in-place consentono di agevolare,
     quindi in modo conciso, operazioni di aumento esempio per i contatori.
    *Questi operatori in-place possono essere fatti con gli operatori normali
     e il modulo:
        Addizione:       +=
        Sottrazione:     -=
        Moltiplicazione: *=
        Divisione:       /=
        Modulo:          %=
    *Stessa cosa può essere usato per gli operatori di stringhe.
'''
print('LEZIONE #9')
x = 2
print(x)
x += 1
print(x)
y = 'Bella'
print(y)
y += 'Ciao'
print(y)
