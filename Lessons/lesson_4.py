'LESSON #4'
'''
    #1 Eccezioni 
    
    *Le eccezioni avvengono quando si presenta
     un errore che stoppa il programma.
    *Ad esempio quando si divide un numero per 0.
    *Comuni eccezioni sono:
        ImportError: errore in un import
        IndexError:  un indice con un valore fuori range
        NameError:   una variabile mai dichiarata
        SyntaxError: il codice non può essere analizzato correttamente
        TypeError:   una funzione viene chiamata su un valore di un tipo inappropriato
        ValueError:  una funzione viene chiamata su un valore di un tipo corretto
                     ma con un valore inappropriato.
'''
print('LEZIONE #1')
#print(4/0)

'''
    #2 Maneggiare le Eccezioni
    
    *Per maneggiare le eccezioni, si può chiamare un codice
     il try/except.
    *Il blocco try contiene il codice che potrebbe avere una eccezione.
    *Se l'eccezione si verifica, il codice dentro il try si blocca
     e viene eseguito il codice all'interno del blocco except.
    *Se non si verifica nessuna eccezione, il blocco in except non
     viene eseguito.
    *Un try può avere molteplici e differenti blocchi except.
    *Più except possono essere inseriti all'interno di una singola ()
     separati da una (,).
    *Questo quando più except possono avere lo stesso messaggio di errore.
    *Quando nell'except non viene specificato l'errore, allora
     viene eseguita quando si verifica qualsiasi tipo di errore.
'''
print('LEZIONE #2')
try:
    print(7/0)
    print('operazione eseguita')
except ZeroDivisionError:
    print('è avvenuto un errore')
    print('è stato diviso un numero per 0')
try:
    variabile = 10
    print(variabile + 'hello')
    print(variabile /2)
except ZeroDivisionError:
    print('diviso per 0')
except (ValueError, TypeError):
    print('avvenuto un errore')

try:
    word = 'spam'
    print(word / 0)
except:
    print('errore')

'''
    #3 finally
    
    *Per garantire l'esecuzione del programma non importa
     per quale errore si verifichi si può usare finally.
    *finally viene messo alla fine del try/except.
'''
print('LEZIONE #3')
try:
    print('hello')
    print(1/0)
except ZeroDivisionError:
    print('Diviso per 0')
finally:
    print('Il codice viene eseguito non importa cosa')

'''
    #4 raise
    
    *Si possono aumentare usando raise.
    *L'eccezione può essere sollevata con argomenti
     che forniscono dettagli su di loro.
    *Nel blocco except, raise senza argomenti
     può servire per sapere che errore è avvenuto.
'''
print('LEZIONE #4')
num = input(':')
if(float(num)<0):
    raise ValueError('Negativo!')
else:
    print('positivo')
try:
    num = 5/1
except:
    print('errore')
    raise
'''
    #5 Asserzioni
    
    *Le asserzioni sono controlli che vengono eseguiti per
     testare un espressione o un dato prima di eseguire
     un'altro codice.
    *Quando un'espressione viene testata, e risulta falsa,
     viene sollevata un eccezione.
    *Le asserzioni vengono eseguite mediante l'utilizzo
     della funzione (assert).
    *Le assert possono avere anche un secondo argomento
     ovvero il messaggio di errore.
'''
print('LEZIONE #5')
print(1)
assert 2+2==4
print(2)
#assert 1+1==3
print(3)
temp = -10
#assert(temp >=0 ), 'Più freddo di zero'

'''
    #6 Apertura files
    
    *Si possono aprire dei file per poterli leggere e scrivere.
    *I file di testo sono i più facili da manipolare.
    *Prima di editare un file bisogna aprirlo, usando
     la funzione open.
    *L'argomento di open() è il path(percorso) del file.
    *Se il file si trova nello stesso percorso del codice
     basta scrivere il nome.
    *Una volta aperto il file bisogna specificare in che modo
     si vuole usarlo all'interno del codice.
    *Basta mettere come secondo argomento dell'open tra '':
        r -> apre il file in modalità lettura (read)
        w -> apre il file in modalità scrittura (write).
             Il file verrà riscritto, quindi si perderà tutto
             ciò che c'era dentro.
        a -> apre il file in modalità aggancia (append).
             Verrà accodato al file un nuovo contenuto alla
             fine del file.
        b -> Si aggiunge a fianco ad una modalità di apertura
             per aprire un file binario quindi un file non
             testuale.
        + -> Si aggiunge a finaco ad una modalità di apertura
             per aprire un file in entrambe le modalità per
             avere un accesso extra.
    *Una volta aperto un file e fatto tutte le elaborazioni
     bisogna chiuderlo con il comando nome_file.close().
'''
print('LEZIONE #6')
#f = open('../Content/file1', 'w')
#f.close()

'''
    #7 Lettura file
    
    *Per poter leggere il contenuto di un file bisogna
     usare il metodo read.
    *read permette di leggere tutto il contenuto del
     file.
    *Si può specificare il numero di byte da far leggere
     al read passandoglielo come argomento.
    *Una volta che il file è stato letto tutto,
     se si prova a leggere di nuovo si starà provando
     a leggere la fine del file.
    *Questo perchè il puntatore sta puntando la fine del file.
    *Un altro metodo di lettura è la lettura per righe (readlines()).
    *Oppure si può usare un ciclo for per leggere le righe.
'''
print('LEZIONE #7')
f = open('../Content/file1.txt', 'r')
txt = f.read(10)
print(txt)
txt = f.read(3)
print(txt)
txt = f.read()
print(txt)
f.close()
f=open('../Content/file2.txt', 'r')
print(f.readlines())
f.close()
f=open('../Content/file2.txt', 'r')
for line in f:
    print(line)
f.close()

'''
    #8 Scrittura file
    
    *Per poter scrivere su un file bisogna
     usare il metodo write il quale
     scriverà stringhe sul file.
    *Con il metodo di apertura 'w' se il file
     non esiste, viene creato.
    *Se il file esiste già, verrà cancellato
     il contenuto e riscritto quello nuovo.
    *Il metodo write ritorna il numero di bytes
     che sono stati scritti sul file.
'''
print('LEZIONE #8')
f = open('../Content/file3.txt', 'w')
print(f.write('Questa è una stringa di testo'))
f.close()
f = open('../Content/file3.txt', 'r')
print(f.read())
f.close()

'''
    #9 Lavorare con i file
    
    *è buona norma evitare di sprecare risorse
     assicurandosi che i file vengano sempre
     chiusi dopo essere stati utilizzati.
    *Per farlo si può usare il try/finally.
    *Mettendo il close del file nel blocco finally
     il file verrà chiuso anche in presenza di errori.
    *Un'altro modo è quello di usare la dichiarazione (with).
    *with permette di creare una variabile temporanea in cui
     è accessibile solo nel blocco with.
    *Il file verrà chiuso alla fine del blocco with automaticamente
     anche in presenza di errori.
'''
print('LEZIONE #9')
try:
    f = open('../Content/file2.txt')
    print(f.read())
finally:
    f.close()
with open('../Content/file2.txt') as f:
    print(f.read())
