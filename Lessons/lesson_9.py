'LESSON #9'
'''
    #1 Lo Zen di Python
    
    *Per essere un buon programmatore
     di python è importante anche scrivere
     codici puliti e facili da comprendere.
    *Un modo per farlo è quello di seguire
     lo Zen di Python, ovvero una guida
     per sapere programmare bene e al meglio
     in python.
    *Per accedere a tale guida, basta
     importare la libreria 'this'.
    *Ci sono alcune linee i quali hanno bisogno
     di spiegazioni:
        'Esplicito è meglio di implicito' -> è meglio precisare esattamente cosa
                                              sta facendo il codice.
        'Piatto è meglio che annidato' -> Ovvero è meglio avere
                                           un codice senza liste dentro ad altre liste
                                           ecc.
        'Gli errori non passano inosservati' -> Quando avviene un errore, è meglio
                                                visualizzare che tipo di errore è,
                                                invece di ignorarlo.
    *Ci sono 20 principi nello Zen di Python, ma solo 19 linee.
    *La ventesima è una questione di opinione.
'''
print('LEZIONE #1')
import this

'''
    #2 PEP
    
    *Python Enhancement Proposals (PEP).
    *Sono suggerimenti per migliorare il linguaggio,
     creati da sviluppatori esperti di python.
    *PEP 8 è uno stile di guida sull'argomento
     della scrittura di codice leggibile.
    *Contiene un numero di linea guida
     riferite al nome della variabile, riassunte:
         I moduli dovrebbero avere un nome corto e tutto minuscolo.
         I nomi delle classi dovrebbero essere a stile cammello
                ovvero le prime lettere maiuscole senza _.
         Molti nomi di variabili e funzioni dovrebbero essere tutte minuscole
                con _ se necessario.
         Le costanti (variabili i quali non cambiano mai il valore) dovrebbero
                essere tutte maiuscole con _ se necessario.
         I nomi che sarebbero in conflitto con le parole chiave di Python
                (come class o if) dovrebbero avere un trattino basso finale.
         Dopo gli operatori e dopo le virgole è raccomandato l'uso dello spazio.
         Le linee non dovrebbero essere più lunghe di 80 caratteri.
         'from module import *' dovrebbe essere evitato.
         Dovrebbe esserci solo una condizione per linea.
    *Queste sono linee guida che ognuno può decidere se seguire o meno.
    *Certamente risulterebbe un codice più pulito e chiaro da leggere.
    *Inoltre seguire questa guida può valorizzare la qualità del codice.
'''
print('LEZIONE #2')

'''
    #3 Di più sugli argomenti delle funzioni
    
    *Python permette di avere funzioni con un numero
     variabile di argomenti.
    *Usando *args come parametro di una funzione, abilita
     di passare un numero di argomenti variabile alla funzione.
    *Gli argomenti sono poi accessibili come Tuple args
     nel corpo della funzione.
    *Il parametro *args viene messo dopo tutti gli altri parametri.
    *args è solo una convenzione, può essere sostituito con un altro nome.
    *I parametri nominati possono avere un valore di default
     facendoli diventare opzionali.
    *Questi vengono messi dopo tutti i parametri senza un valore di default.
    *Nel caso l'argomento viene passato, il valore di default viene ignorato,
     altrimenti si userà quello se non viene passato niente.
    *(**kwargs) permette di gestire argomenti con nome che
     non si ha definito in anticipo.
    *Ritorna un dizionario dove la chiave è il nome dell'argomento e
     come valore il valore dell'argomento.
'''
print('LEZIONE #3')
def function(named_arg, *args):
    print(named_arg)
    print(args)
function(1,2,3,4,5)

def function2(x, y, food = 'spam'):
    print(food)
function2(1,2)
function2(3,4,'egg')

def my_func(x, y = 7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)
my_func(2, 3, 4, 5, 6, a = 7, b = 8)

'''
    #4 Spacchettamento del Tuple
    
    *Lo spacchettamento del Tuple permette di assegnare
     ogni oggetto nell'iterabile a una variabile.
    *Una variabile che è preceduta da un (*) prende tutti i
     valori dell'iterabile partendo da quello dopo
     l'ultimo assegnato ad uno precedente fino a quello
     prima di uno già assegnato ad un'altro.
'''
print('LEZIONE #4')
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
print('===========================')
a, b = b, a
print(a)
print(b)
print(c)
print('===========================')
a, b, *c, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)

'''
    #5 Operatore ternario

    *Le espressioni con condizioni forniscono le
     funzionalità della dichiarazione if il quale
     usa meno codice.
    *Non dovrebbero essere usate molto, perchè
     riducono la leggibilità, ma sono molto utili
     per assegnare valori alle variabili.
    *Le espressioni con condizioni sono conosciuti
     anche per l'applicazione di operatori ternari.
    *L'operatore ternario controlla la condizione e
     ritorna il valore corrispondente.
'''
print('LEZIONE #5')
a = 7
b = 1 if a >= 5 else 42
print(b)
status = 1
msg = 'Logout' if status == 1 else 'Login'

'''
    #6 Di più sul else

    *La condizione else è usata comunemente nell'if,
     ma può essere usata anche nel for o while loop,
     il quale da un significato diverso.
    *L'else nel for o while loop viene chiamato
     quando il codice finisce normalmente, senza che un
     break interrompa la condizione e causa una uscita.
    *La condizione else può essere usato anche nel try/except.
    *In questo caso, il codice viene eseguito solo se non
     avvengono errori nel try.
'''
print('LEZIONE #6')
for i in range(10):
    if i == 999:
        break
else:
    print('ininterrotto 1')

for i in range(10):
    if i == 5:
        break
else:
    print('ininterrotto 2')

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

'''
    #7 __main__

    *La maggior parte del codice python è un modulo da importare,
     o uno script che fa qualcosa.
    *Alcune volte è utile creare un file che può essere sia importato
     come modulo ed eseguito come script.
    *Per fare ciò, si mette un codice script dentro
     if __name__ == '__main__' .
    *Questo assicura che non verrà eseguito se il file viene importato.
    *Quando l'interprete Python legge un file sorgente, esegue tutto il codice che trova nel file.
    *Prima di eseguire il codice, definisce alcune variabili speciali.
    *Se l'interprete Python esegue quel modulo come programma principale,
     imposta la variabile speciale __name__ in modo che abbia un valore '__main__'.
    *Se questo file viene importato da un altro modulo, __name__ verrà impostato sul nome del modulo.
    *Se si salva il file (come ad esempio sololearn.py) e si importa questo da un'altro modulo script,
     si usa il nome sololearn.
'''
print('LEZIONE #7')
def function():
    print('Questo è una funzione di un modulo')
if __name__ == '__main__':
    print('Questo è uno script')

'''
    #8 Principali librerie di terze parti

    *Ci sono molte principali librerie di terze parti,
     che ovvero non sono integrate in python:
         Django -> Potenzia i siti web inclusi Instagram e Disqus.
                   Ha molte caratteristiche utili.
         CherryPy -> Altro popolare web framework.
         Flask -> Altro popolare web framework.
         BeatifulSoup -> Utile per raschiare dati dai siti web,
                         e conduce ad un miglior risultato se si crea
                         il proprio raschiatorer con espressioni regolari.
         Matplotlib -> Permette di creare grafici basati sui dati in Python.
         NumPy -> Permette di usare array multidimensionali più veloci
                  delle native soluzioni Python; contiene anche funzioni
                  per eseguire operazioni matematiche.
         SciPy -> Contiene numerose estensioni per funzionalità di NumPy.
         Panda3D -> Per sviluppare giochi in 3D.
         Pygame -> Per sviluppare giochi in 2D.
'''
print('LEZIONE #8')

'''
    #9 Packaging

    *Il termine packaging si riferisce nel mettere dei moduli
     che si ha scritto in un formato standard, in questo modo
     altri programmatori possono installarlo e usarlo facilmente.
    *Questo coinvolge l'uso di moduli come setuptools e distutils.
    *Ci sono due step:
        1 step -> è quello di organizzare i file esistenti correttamente;
                  posiziona tutti i file che vuoi mettere in una libreria
                  nella stessa directory principale; questa directory dovrebbe
                  contenere un file chiamato __init__.py, il quale può essere vuoto
                  ma basta che sia presente nella directory; questa directory
                  va messa all'interno di un'altra directory contenente il
                  readme e la licenza, così come anche il file setup.py .
        2 step -> è quello di scrivere il file setup.py; questo contiene
                  le informazioni necessarie per assemblare il pacchetto
                  in questo modo può essere caricato su PyPI e installato
                  con pip; dopo la creazione del setup.py, caricarlo su
                  PyPI, o usare i la linea comando per creare una distribuzione
                  binaria (un installer eseguibile); Per costruire una distribuzione
                  sorgente, si usa la linea comando per navigare alla directory
                  contenente setup.py ed eseguirlo con il comando
                  'python setup.py sdist'; eseguire 'python setup.py bdist' o,
                  su windows, 'python setup.py bdist_wininst' per costruire
                  una distribuzione binaria; usare 'python setup.py register',
                  seguito da 'python setup.py upload' per caricare il pacchetto;
                  infine installare il pacchetto con 'python setup.py install'.
'''
print('LEZIONE #9')

'''
    #10 Packaging per utenti

    *Molti utenti non hanno python installato nel computer.
    *Per questo è utile impacchettare gli script come
     file eseguibili per le relative piattaforme, come
     Windows o Mac.
    *Per Windows, ci sono molti attrezzi per convertire lo script in eseguibile.
    *Per esempio, py2exe, può essere usato per impacchettare script di Python,
     con le librerie che ha bisogno, dentro un solo eseguibile.
    *PyInstaller e cx_Freeze servono allo stesso scopo.
    *Per Mac, si usa py2app, PyInstaller o cx_Freeze.
'''
print('LEZIONE #10')
