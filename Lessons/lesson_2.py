'LESSON #2'
'''
    #1 Booleans
    
    *Un altro tipo di variabile è il boolean.
    *Il boolean ha due valori: True (vero) o False (falso).
    *I confonti permettono di capire se è presente un uguaglianza o no
     e sono utili perchè possono generare delle variabili boolean.
    *Ci sono vari tipi di confronti:
        Uguaglianza:     ==
        Disuguaglianza:  !=
        Maggiore:        >
        Minore:          <
        Maggiore-Uguale: >=
        Minore-Uguale:   <=
'''
print('LEZIONE #1')
my_boolean = True
print(my_boolean)
print(2==3)
print('ciao' == 'ciao')
print(2!=3)
print(20>40)
print(4<21)
print(10>=10)
print(45<=42)

'''
    #2 Dichiarazione IF
    
    *(if) è una dichiarazione che consente di eseguire
     un certo codice solo se la condizione apportata
     risulta vera (True).
    *Al contrario, se la condizione risulta falsa (False)
     non viene eseguito il codice.
    *Gli (if) possono essere anche messi uno dentro l'altro.
'''
print('LEZIONE #2')
if(1>=10):
    print('Uno è maggiore-uguale a Dieci')
print('Fine if')
if(50>10):
    print('50 è maggiore di 10')
    if(50<20):
        print('50 è minore di 20')

'''
    #3 Dichiarazione ELSE
    
    *Quando un (if) risulta falso (False) può sopraggiungere
     la dichiarazione (else).
    *(else) può essere usata quando una condizione dell'(if)
     risulta falsa (false).
    *Ogni (if) può avere un solo (else).
    *Al posto di fare una lunga coda mettendo un (if)
     dentro un (else), si può usare direttamente (elif).
    *(elif) sarebbe un (else) con una condizione.
'''
print('LEZIONE #3')
if(1>=10):
    print('Uno è maggiore-uguale a Dieci')
else:
    print('Uno è minore di Dieci')
print('Fine if')
num = 3
if(num==1):
    print('Uno')
else:
    if(num==2):
        print('Due')
    else:
        if(num==3):
            print('Tre')
        else:
            print('Altro numero')
if(num==1):
    print('Uno')
elif(num==2):
    print('Due')
elif(num==3):
    print('Tre')
else:
    print('Altro numero')

'''
    #4 Logica booleana
    
    *La logica booleana viene usata per fare condizioni
     più complicate e possono stare tutti in una sola condizione.
    *Ci sono vari logiche booleane:
        and (Tutte le condizioni devono essere True);
        or (Almeno una condizione deve essere True);
        not (La negazione deve essere vera).
'''
print('LEZIONE #4')
print(1==1 and 2==2)
print(1==1 and 2==3)
print(1==1 or 2==2)
print(1==1 or 2==3)
print(not 1==1)
print(not 1>4)

'''
    #5 Liste
    
    *Le liste sono usati per storare oggetti.
    *Una lista si crea con un nome della lista, mettendo le [] e le , per separare
     gli oggetti.
    *Per richiamare gli oggetti si mette il nome della lista e tra [] il numero corrispondente
     alla posizione dell'oggetto all'interno della lista (si parte dallo 0).
    *Si possono creare delle liste vuote per poi riempirle più avanti.
    *Si possono creare anche delle matrici.
    *Le matrici sono liste all'interno di liste.
    *Per identificare un oggetto all'interno della lista interna si mettono due [][]
     dove nella prima si identifica la lista in cui è contenuto l'oggetto e nel
     secondo la posizione dell'oggetto.
    *Qualche tipo, come le stringhe, possono essere viste come liste di caratteri.
'''
print('LEZIONE #5')
numeri = ['Uno','Due','Tre']
print(numeri[0])
print(numeri[1])
print(numeri[2])
empty_list = []
print(empty_list)
num = 3
ogg = ['stringa',0,[1,2,num],4.56]
print(ogg[1])
print(ogg[2])
print(ogg[2][2])
print(ogg[3])
matr =[
        [1,2,3]
        ,['Uno','Due','Tre']
      ]
print(str(matr[0][1]) + ' = ' + matr[1][1])
st = 'ciao'
print(st[2])

'''
    #6 Operazioni di liste
    
    *Nelle liste possono essere cambiati alcuni valori.
    *Si indicizza il valore e si assegna un valore diverso.
    *Possono assumere le stesse operazioni delle stringhe,
     quindi:
         Concatenazione:  +
         Multiplicazione: *
    *Per controllare se un oggetto è all'interno della lista si usa
     la funzione (in).
    *Restituisce un valore booleano.
    *Per controllare se un oggetto non è all'interno della lista si usa
     la funzione (not) e (in).
    *Restituisce un valore booleano.
'''
print('LEZIONE #6')
num = [3,6,6,1,7]
print(num)
num[2] = 2
print(num)
print(num +[4,2,6])
print(num * 3)
print(1 in num)
print(0 in num)
print(not 4 in num)
print(not 6 in num)

'''
    #7 Funzioni di liste
    
    *Ci sono delle funzioni che possono essere usate sulle liste.
    *Queste funzioni sono:
        append(oggetto) (Aggiunge un valore in fondo alla lista)
        len(lista) (Restituisce il valore di quanti oggetti ci sono all'interno della lista)
        insert(posizione, oggetto) (Aggiunge un valore nella posizione specificata all'interno della lista)
        index(oggetto) (Restituisce la posizione all'interno della lista dell'oggetto specificato)
'''
print('LEZIONE #7')
num = [1,2,3]
print(num)
num.append(4)
print(num)
print(len(num))
num.insert(1,5)
print(num)
print(num.index(2))

'''
    #8 Ciclo while
    
    *Il ciclo while è usato per ripetere un blocco di codice più volte.
    *Il while ha una condizione che finchè rimane vera (True) ripete
     il blocco di codice che risiede all'interno.
    *Quando la condizione diventa falsa (False), esce dal ciclo.
    *Si possono usare più condizioni insieme.
    *Per fermare un ciclo while prima si usa (break).
    *Per fermarsi ad un certo punto per saltare un giro di ciclo per continuare con il
     prossimo si usa (continue).
    *Si usa il while quando non si sà il numero di iterazioni (giri) preciso.
'''
print('LEZIONE #8')
i=0
print('Inizio ciclo')
while(i<=5):
    print(i)
    i +=1
print('Ciclo finito')
num = 1
while(num<=10):
    if(num%2==0):
        print(str(num) + ' è pari')
    else:
        print(str(num) + ' è dispari')
    num +=1
num = 1
while True:
    print(num)
    if(num >=5):
        print('stop')
        break
    num +=1
print('finito')
num = 0
while num<=5:
    num += 1
    if(num==3):
        print('skip 3')
        continue
    print(num)

'''
    #9 Ciclo for
    
    *Il ciclo for è usato per ripetere un blocco di codice più volte.
    *Il for ha una condizione che si ripete come un contatore e quando
     questo contatore arriva a diventare falso (False) il ciclo finisce.
    *Si usa variabile (in) nome lista -> In questo modo la variabile assume
     man mano ogni valore della lista.
    *Il for si può usare per contare dei caratteri in una stringa.
    *Si usa il for quando si sà il numero di iterazioni (giri) preciso.
'''
print('LEZIONE #9')
parole = ['ciao','mondo','prosciutto']
for word in parole:
    print(word + '!')
cnt = 0
word = 'Buon pomeriggio'
print(word)
for char in word:
    if(char == 'o'):
        cnt += 1
print(cnt)

'''
    #10 range
    
    *Il range è una funzione che permette di generare dei numeri
     partendo da 0 fino al numero indicato tra ().
    *Si può usare la funzione list() per indicare che quella variabile
     è una nuova lista.
    *Se la funzione range ha un solo argomento (un solo valore dentro le () ),
     allora genererà dei numeri partendo da 0 fino al numero indicato.
    *Se la funzione range ha due argomenti, allora genererà dei numeri partendo
     dal primo numero fino al secondo numero (non incluso).
    *Se la funzione range ha tre argomenti, il terzo argomento indica l'intervallo
     della sequenza prodotta (step).
    *Il range può essere usato insieme al for per ripetere il ciclo tot di volte.
'''
print('LEZIONE #10')
num = list(range(10))
print(num)
num1 = list(range(10,20))
print(num1)
num2 = list(range(20,30,2))
print(num2)
for cnt in range(5):
    print('ciao')
