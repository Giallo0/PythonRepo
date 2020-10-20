'LESSON #7'
'''
    #1 Classi
    
    *La programmazione orientata ad oggetti (OOP) è
     un paradigma, quindi un altro modo di programmazione
     che vede l'utilizzo di creazione ed uso di oggetti.
    *Gli oggetti sono creati usando le classi (class)
     i quali quest'ultimi sono il punto focale dell'OOP.
    *La classe definisce le qualità (ovvero la pianta,
     descrizione o definizione) dell'oggetto.
    *Si può usare la stessa classe con una pianta
     per fare più oggetti differenti.
    *Le classi si creano usando la parola (class) seguito
     dal nome_oggetto : e il blocco, il quale contiene
     metodi della classe(che sono funzioni).
    *Il metodo __init__ è il metodo più importante
     delle classi.
    *Questo metodo viene richiamato quando un istanza(oggetto)
     di una classe viene creato.
    *Ogni metodo deve avere (self) come primo parametro.
    *Non c'è bisogno di includerlo quando richiamiamo il metodo.
    *All'interno di una definizione di un metodo,
     self si riferisce all'istanza che chiama il metodo.
    *L'istanza di una classe ha degli attributi, i quali sono
     pezzi di data associati tra di loro; (Gli attributi
     sono inseriti tra () dopo self).
    *Si può accedere all'attributo mettendo
     nome_instanza.valore_attributo .
    *In un metodo __init__, self.attributo può
     essere usato per settare il valore iniziale di un
     attributo di un'istanza.
    *Il metodo __init__ è chiamato la classe costruttore.
    *Le classi possono avere altri metodi definiti per
     aggiungere funzionalità.
    *Ogni metodo deve sempre avere self come primo parametro.
    *Per accedere a questi metodi si usa la stessa sintassi
     per gli attributi.
    *Le classi possono avere anche attributi, e sono
     creati assegnando varibili senza metterli nel
     corpo della classe.
    *Questi sono accessibili o da instanze della classe
     o dalla classe stessa.
    *Gli attributi della classe sono condivisi da tutte le
     istanze della classe.
    *Se si prova ad accedere ad un attributo di una classe
     inesistente, si avrà un errore (AttributeError), e
     succede anche quando si cerca di richiamare
     un metodo indefinito.
'''
print('LEZIONE #1')
class Gatto:
    def __init__(self, colore, zampe):
        self.colore = colore
        self.zampe = zampe

Felix = Gatto('Arancione',4)
Birba = Gatto('Grigio',4)
print(Felix.colore)
print(Birba.zampe)

class Cane:
    zampe = 4
    def __init__(self, nome, colore):
        self.nome = nome
        self.colore = colore
    def abbaio(self):
        print('Woof!')
        
fido = Cane('Fido','Marrone')
print(fido.nome)
print('Zampe:', fido.zampe)
print('Zampe:', Cane.zampe)

'''
    #2 Eredità (inheritance)
    
    *L'eredità è un modo che consente di condividere
     funzionalità tra le classi.
    *Esempio:
        Immaginiamo di avere diverse classi (Cane,Gatto,Coniglio)
        e tante altre. Sebbene potrebbero differire per
        qualche caratteristica (ad esempio solo il cane può avere
        il metodo abbaia), è probabile che ne abbiamo alti simili
        (come ad esempio tutti possono avere l'attributo colore o nome).
    *Queste somiglianze possono essere espresse facendoli ereditare tutti
     da una superclasse(superclass) Animale, il quale contiene tutte le funzionalità
     condivise.
    *Per ereditare una classe da un'altra, si mette il nome della superclasse
     tra le () dopo il nome della classe.
    *Una classe che eredita da un'altra classe si chiama subclasse(subclass).
    *Una classe che viene ereditata è chiamata superclasse(superclass).
    *Se una classe eredita da un'altra con gli stessi attributi o metodi, questa
     verrà sovrascritta.
    *L'eredità può essere anche indiretta.
    *Una classe può ereditare da un'altra, e questa classe può ereditare
     da un'altra classe.
    *La funzione (super) è un'utile funzione relativa all'ereditarietà
     che fa riferimento alla classe genitore.
    *Può essere usato per cercare il metodo con un
     certo nome nella superclasse di un oggetto.
'''
print('LEZIONE #2')
class Animale:
    def __init__(self,nome,colore):
        self.nome = nome
        self.colore = colore
class Lupo(Animale):
    def ululo(self):
        print('Auuuu!')
class Zanzara(Animale):
    def ronzare(self):
        print('zzzzzz!')
ciccio = Lupo('Ciccio','Grigio')
print(ciccio.colore)
ciccio.ululo()

class Cavallo:
    def __init__(self,nome,colore):
        self.nome = nome
        self.colore = colore
    def nitrire(self):
        print('HIHIHIIH!')
class Pony(Cavallo):
    def nitrire(self):
        print('hihei!')
Paolo = Pony('Paolo','Bianco')
print(Paolo.nome)
Paolo.nitrire()
Gianluca = Cavallo('Gianluca','Nero')
print(Gianluca.nome)
Gianluca.nitrire()

class A:
    def metodo(self):
        print('Metodo A')
class B(A):
    def altro_metodo(self):
        print('Metodo B')
class C(B):
    def terzo_metodo(self):
        print('Metodo C')
c = C()
c.metodo()
c.altro_metodo()
c.terzo_metodo()

class D:
    def spam(self):
        print(1)
class E(D):
    def spam(self):
        print(2)
        #suoer().spam() chima il metodo spam della superclasse
        super().spam()
E().spam()

'''
    #3 Metodi magici
    
    *I metodi magici sono metodi speciali i quali
     hanno la caratteristica di avere (__) sia
     all'inizio che alla fine del nome.
    *Sono anche conosciuti come dunders.
    *Un esempio già visto è (__init__) ma ce
     ne sono molti altri.
    *Sono usati per creare funzionalità che
     non è possibile rappresentarli con i normali
     metodi.
    *Un loro uso comune è il sovraccarico dell'operatore.
    *Ovvero definire operatori per classi personalizzate
     che consentono di utilizzare operatori come (+) e (*)
     su di essi.
    *Ci sono vari metodi magici:
        __init__ -> Come abbiamo visto, inizializza una nuova istanza
                    e viene chiamata la classe costruttore.
        __add__  -> Consente di definire un comportamento personalizzato
                    per l'operatore (+) nella classe; Aggiunge gli attributi
                    corrispondenti degli oggetti e restituisce un nuovo oggetto,
                    contenente il risultato.
        __sub__  -> (-)
        __mul__  -> (*)
        __truediv__ -> (/)
        __floordiv__ -> (//)
        __mod__ -> (%)
        __pow__ -> (**)
        __and -> (&)
        __xor__ -> (^)
        __or__ -> (|)
    *L'espressione (x+y) è tradotta in (x.__add__(y)) .
    *Questo funziona solo se il primo membro è implementato
     (ovvero è un oggetto), quindi possiamo avere oltre a
     (x.__add__(y)) anche (x.__add__(4)).
    *Questo è perchè è come se il programma riesce a riconoscere
     l'oggetto x.
    *Se abbiamo invece (4.__add__(x)) il programma non riconosce
     (4) perchè è un tipo integrato di python ma il programma
     non lo riconosce come oggetto, quindi andrà in errore.
    *Ecco che entra in gioco (r) metodo il quale si aggiunge
     una (r) prima del nome del metodo (tipo: __radd__).
    *Questo metodo consente di valutare prima se è possibile
     eseguire (4.__add__(x)) e in caso dovesse dare errore,
     python prova a fare (x.__radd__(4)) invece di andare in errore.
    *Questo medoto può essere usato per tutti i metodi precedenti
     (ovviamente tranne __init__).
    *Ci sono anche metodi magici per i confronti:
        __lt__ -> (<)less than
        __le__ -> (<=)less equal
        __eq__ -> (==)equal
        __ne__ -> (!=)not equal
        __gt__ -> (>)greater than
        __ge__ -> (>=)greater equal
    *Ci sono molti altri metodi magici per creare classi che
     si comportano come contenitori:
         __len__ -> per la lunghezza (len())
         __getitem__ -> per indicizzare
         __setitem__ -> per assegnare valori indicizzati
         __delitem__ -> per eliminare valori indicizzati
         __iter__ -> per interagire sugli oggetti (tipo for loop)
         __contains__ -> per (in)
    *Ci sono altri metodi come:
        __call__ -> per richiamare oggetti come funzioni
        __int__ -> cast in interi
        __str__ -> cast in stringhe
        __repr__ -> usato per rappresentare le istanze come stringa
'''
print('LEZIONE #3')
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self,altro):
        return Vector2D(self.x + altro.x,
                        self.y + altro.y)
primo = Vector2D(5, 7)
secondo = Vector2D(3, 9)
resultato = primo + secondo
print(resultato.x)
print(resultato.y)

class Stringhe_Speciali:
    def __init__(self, cont):
        self.cont = cont
    def __truediv__(self, altro):
        linea = '=' * len(str(altro.cont))
        return '\n'.join([str(self.cont), linea, str(altro.cont)])
spam = Stringhe_Speciali('spam')
hello = Stringhe_Speciali('hello world')
print(spam / hello)
cin = Stringhe_Speciali(5)
sei = Stringhe_Speciali(6)
print(cin / sei)

class Stringhe_Speciali2:
    def __init__(self, cont):
        self.cont = cont
    def __gt__(self, altro):
        for index in range(len(altro.cont)+1):
            result = altro.cont[:index] + '>' + self.cont
            result += '>' + altro.cont[index:]
            print(result)
spam = Stringhe_Speciali2('spam')
egg = Stringhe_Speciali2('egg')
spam > egg

import random
class VagueList:
    def __init__(self, cont):
        self.cont = cont
    def __getitem__(self, index):
        return self.cont[index + random.randint(-1,1)]
    def __len__(self):
        return random.randint(0,len(self.cont)*2)
vague_list = VagueList(['A','B','C','D','E'])
print(len(vague_list)) #Non mi stampa la lunghezza della lista ma mi genera un numero tra 0 e (3*2), dove
                       #3 è la lunghezza della lista
print(len(vague_list)) #Qua mi genera un'altro numero sempre compreso tra 0 e (3*2), e potrebbe essere lo stesso di prima
print(vague_list[2])   #Qua mi stampa una lettera a caso della lista. Quindi sarà lista[2+un numero a caso tra -1 e 1].
print(vague_list[2])   #Stessa cosa di sopra

'''
    #4 Ciclo di vita di un oggetto

    *Il ciclo di vita di un oggetto è composto dalla
     creazione, manipolazione e distruzione.
    *La prima fase del ciclo di vita di un oggetto è
     la definizione della classe a cui appartiene.
    *La seconda fase è l'istanziazione di una istanza,
     quando un __init__ è chiamata.
    *La memoria è allocata per conservare l'instanza.
    *Appena prima che accade questo, viene richiamato
     il metodo __new__ della classe.
    *Dopo questo, l'oggetto è pronto all'uso.
    *Quando un oggetto viene distrutto, la memoria
     allocata viene liberata, e può essere usata
     per altri scopi.
    *La distruzione di un oggetto avviene quando
     il suo conteggio di riferimenti arriva a 0.
    *Il conteggio dei riferimenti è il numero di
     variabili ed altri elementi che si riferiscono
     a un oggetto.
    *Se nessuno è riferito a lui (quindi ha il conteggio
     riferimenti a zero) nessuno può interagire
     con lui, quindi può essere eliminato in sicurezza.
    *In alcune situazioni, due o più oggetti possono
     essere riferiti solo tra di loro, e quindi possono
     essee eliminati.
    *La dichiarazione (del) riduce il conteggio dei
     riferimenti di un oggetto di uno, e questo
     conduce alla sua eliminazione.
    *Il metodo magico per (del) è __del__ .
    *Il processo di eliminazione di oggetti i quali
     non servono più è chiamato raccolta rifiuti.
    *Per riassumere, il conteggio dei riferimenti di un
     oggetto quando viene eleminato con (del), la sua
     relazione è riassegnata, o il suo riferimento esce
     dal campo di applicazione.
    *Quando il conteggio dei riferimenti raggiunge lo zero,
     Python lo elimina automaticamente.
'''
print('LEZIONE #4')
h = 42 #Creazione di un oggetto <42>
j = h  #Incremento del conteggio riferimenti di <42>
k = [h] #Incremento del conteggio riferimenti di <42>

del h #Decremento del conteggio riferimenti di <42>
j = 100 #Decremento del conteggio riferimenti di <42>
k[0] = -1 #Decremento del conteggio riferimenti di <42>

'''
    #5 Dati nascosti

    *La parte chiave della programmazione orientata
     ad oggetti è l'incapsulamento, che implica il
     confezionamento di variabili e funzioni correlate
     in un unico oggetto di facile utilizzo - un'istanza di una classe.
    *Un concetto associato è il Data hiding(Dati nascosti), che
     dice che le implementazioni di una classe dovrebbero essere
     nascosti, e ci dovrebbe essere una interfaccia pulita per
     tutti quelli che vogliono usare la class.
    *In poche parole, non ci dovrebbero essere tutte le
     istruzioni di una classe all'interno di un programma
     facendo in modo che il display sia più pulito.
    *In python non ci sono modi per imporre che un metodo
     o un attributo sia strettamente privato.
    *I metodi e gli attributi debolmente privati ​​hanno
     un singolo carattere di sottolineatura all'inizio (_name).
    *Però questo non impedisce al codice esterno di usare
     il metodo o l'attributo, è solo un nome convenzionale
     per dire che quello fa parte solo di quella classe.
    *Il suo unico funzionamento è quello di quando si importa
     una classe con (from nome_modulo import *) questa non
     importerà le variabili con un singolo (_).
    *Per mettere metodi e attriburi più strettamente privati
     hanno all'inizio del nome(__).
    *Questo causa la mutilazione del nome, che significa che loro
     non possono essere accessibili dall'esterno.
    *Lo scopo di questo non è garantire che questi dati siano
     mantenuti privati, ma per evitare bug se ci sono sottoclassi
     che hanno metodi o attributi con gli stessi nomi.
    *Il nome mutilato di un metodo può essere accessibile dall'esterno,
     ma con un nome diverso.
    *Ad esempio il metodo __privmeth di una classe Spam può
     essere accessibile dall'esterno come _Spam__privmeth.
'''
print('LEZIONE #5')
class Queue:
    def __init__(self,contents):
        self._hiddenlist = list(contents)
    def push(self,value):
        self._hiddenlist.insert(0,value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return 'Queue({})'.format(self._hiddenlist)
queue = Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)
s = Spam()
s.print_egg()
print(s._Spam__egg)
#print(s.__egg)

'''
    #6 Metodi di classi e metodi statici

    *I metodi di un oggetto che abbiamo già visto vengono
     chiamati da una istanza di una classe, il quale
     è passata attraverso il parametro self di un metodo.
    *I metodi di una classe sono diversi (vengono chiamati
     da una classe, il quale è passato al parametro cls di un metodo).
    *Quindi i metodi di un oggetto hanno come primo parametro (self).
    *I metodi di una classe hanno come primo parametro (cls).
    *Un uso comune di questi sono i metodi di fabbrica, che
     istanzia una istanza di una classe, usando parametri diversi i quali
     sono solitamente passati dal costruttore di una classe.
    *I metodi di una classe sono marcati da un decoratore classmethod.
    *I metodi statici sono simili ai metodi di classi, eccetto
     per il fatto che loro non ricevono argomenti in più (tipo self o cls).
    *Sono identici alle funzioni normali che appartengono
     alle classi.
    *Sono marcati dal decoratore staticmethod.
'''
print('LEZIONE #6')
class Rettangolo:
    def __init__(self, largh, altez):
        self.largh = largh
        self.altez = altez
    def calcola_area(self):
        return self.largh * self.altez
    @classmethod
    def new_quadrato(cls, lungh_lato):
        return cls(lungh_lato, lungh_lato)
quadrato = Rettangolo.new_quadrato(5)
print('Larghezza:',quadrato.largh,'\nAltezza:',quadrato.altez)
print('Area:',quadrato.calcola_area())
rettangolo = Rettangolo(5,2)
print('Larghezza:',rettangolo.largh,'\nAltezza:',rettangolo.altez)
print('Area:',rettangolo.calcola_area())
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    @staticmethod
    def validate_topping(topping):
        if(topping == 'Ananas'):
            raise ValueError('Non ci va l\'ananas!!')
        else:
            return True
ingredienti = ['Pomodoro','Mozzarella','Cipolla','Prosciutti']
if all(Pizza.validate_topping(i) for i in ingredienti):
    pizza = Pizza(ingredienti)

'''
    #7 Proprietà

    *Le proprietà provvede un modo per personalizzare
     l'accesso ad un'istanza degli attributi.
    *Viene creato mettendo un decoratore property
     prima del metodo, il che significa quando
     un attributo di una istanza con gli stessi nomi del
     metodo è acceduto, il metodo sarà chiamato subito.
    *Un comune utilizzo delle proprietà è per fare
     attributi solo da leggere (read-only).
    *Nelle proprietà possono essere inoltre
     definite le funzioni setter/getter.
    *La funzione setter setta il corrispondente
     valore della proprietà.
    *La funzione getter prende il valore.
    *Per definire un setter, si usa il decor
     con lo stesso nome della proprietà seguito
     da un (.setter).
    *Stessa applicazione per il getter.
'''
print('LEZIONE #7')
class Panino:
    def __init__(self, toppings):
        self.toppings = toppings
    @property
    def ananas_consentita(self):
        return False
panino = Panino(['formaggio','mozzarello'])
print(panino.ananas_consentita)
#panino.ananas_consentita = True
class Piadina:
    def __init__(self, toppings):
        self._ananas_consentita = toppings
    @property
    def ananas_consentita(self):
        return self._ananas_consentita
    @ananas_consentita.setter
    def ananas_consentita(self, value):
        if value:
            password = input('Inserisci password: ')
            if password == 'pass':
                self._anans_consentita = value
            else:
                raise ValueError('Attenzione!Intruso!')
piadina = Piadina(['Formaggio','Prosciutto'])
print(piadina.ananas_consentita)
piadina.ananas_consentita = True
print(piadina.ananas_consentita)

'''
    #8 Un semplice Gioco

    *La programmazione orientata ad oggetti
     è utile quando si deve gestire differenti oggetti
     e le loro relazioni.
    *è molto utile quando ad esempio si sviluppano
     giochi con diversi personaggi e caratteristiche.
    *Diamo un occhio ad un esempio il quale mostra
     come le classi sono usati nello sviluppo del gioco.
    *Il gioco da sviluppare è un vecchio gioco d'avventura
     basato sul testo.
    *La classe Goblin eredita dalla classe GameObjects.
    *Viene creata inoltre una classe examine, il quale
     ritorna la descrizione dell'oggetto.
    *Il codice viene implementato aggiungendo dettagli alla
     classe Goblin e permette di combattere contro i goblin.
'''
print('LEZIONE #8')
class GameObject:
    class_name = ''
    desc = ''
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self
    def get_desc(self):
        return self.class_name + '\n' + self.desc
class Goblin(GameObject):
    def __init__(self,name):
        self.class_name = 'goblin'
        self._desc = 'Una creatura misteriosa'
        self.health = 3
        super().__init__(name)
    @property
    def desc(self):
        if(self.health >= 3):
            return self._desc
        elif(self.health == 2):
            health_line = 'Ha una ferita al ginocchio.'
        elif(self.health == 1):
            health_line = 'Il suo braccio sinistro è stato tagliato!'
        elif(self.health <= 0):
            health_line = 'è morto.'
        return self._desc + '\n' + health_line
    @desc.setter
    def desc(self, value):
        self._desc = value

goblin = Goblin('Gobbly')

def hit(noun):
    if(noun in GameObject.objects):
        thing = GameObject.objects[noun]
        if(type(thing) == Goblin):
            thing.health = thing.health - 1
            if(thing.health <= 0):
                msg = 'Hai ucciso il goblin!'
            else:
                msg = 'Hai colpito il {}'.format(thing.class_name)
    else:
        msg = 'Non c\'è nessun {} qui.'.format(noun)
    return msg
def examine(noun):
    if(noun in GameObject.objects):
        return GameObject.objects[noun].get_desc()
    else:
        return 'Non ci sono {} qui'.format(noun)
def get_input():
    command = input(': ').split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print('Verbo sconosciuto {}'.format(verb_word))
        return
    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb('Nulla'))
def say(noun):
    return 'Hai detto: "{}"'.format(noun)

verb_dict = {
    'say': say,
    'examine':examine,
    'hit':hit,
}
while True:
    get_input()
