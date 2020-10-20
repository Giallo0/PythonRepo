'LESSON #8'
'''
    #1 Espressioni regolari
    
    *Le espressioni regolari sono un attrezzo potente
     per i vari tipi di manipolazione delle stringhe.
    *è un linguaggio specifico del dominio che è presente
     sotto forma di libreria nella maggior parte dei moderni
     linguaggi di programmazione.
    *Sono utili specialmente per due compiti:
        Verificare se le stringhe corrispondono ad un modello;
        Eseguire sostituzioni in una stringa.
    *Per accedere alla libreria delle espressioni regolari
     basta importare il modulo (re).
    *Per il pattern si usa mettere prima delle '' la (r)
     che sta per row string.
    *Ci sono varie metodi come:
        re.match -> Può essere utilizzato per determinare se c'è
                    una corrispondenza all'inizio di una stringa;
                    Se è presente, ritorna un oggetto che rappresenta
                    la corrispondenza altrimenti ritorna None.
        re.search -> Cerca la corrispondenza del pattern ovunque
                     nella stringa.
        re.findall -> Ritorna la lista di tutte le corrispondenze
                      trovate nella stringa.
        re.finditer -> Restituisce un iteratore, piuttosto che un elenco.
        re.sub -> Questo metodo rimpiazza tutte le occorenze del pattern
                  nella stringa; si forma cosi:
                      re.sub(pattern, repl, string, count=0)
                  dove pattern è il pattern da controllare
                  repl è la sostituzione al pattern
                  string è la stringa dove applicare il rimpiazzo
                  count permette di dire quante sostutuzini far avvenire.
    *Alcuni di questi metodi possono ritornare oggetti che danno dei dettagli
     sulle corrispondenze trovate.
    *I metodi che possono usare queste sotto-funzioni sono
     ad esempio il search e il finditer.
    *Questi metodi includono:
        group -> il quale ritorna la stringa pattern.
        start -> il quale ritorna la posizione iniziale
                 del corrisposto.
        end -> il quale ritorna la posizione finale
               del corrisposto.
        span -> il quale ritorna la posizione iniziale e finale
                del corrisposto come tuple.
'''
print('LEZIONE #1')
import re

pattern = r'spam'
if re.match(pattern, 'spamspamspam'):
    print('Match')
else:
    print('No match')
#match
if re.match(pattern, 'eggspamsausagespam'):
    print('Match')
else:
    print('No match')
#search
if re.search(pattern, 'eggspamsausagespam'):
    print('Match')
else:
    print('No match')
#findall
print(re.findall(pattern,'eggspamsausagespam'))
for match in re.finditer(pattern,'eggspamsausagespam'):
    print(match.start())
    print(match.end())

pattern = r'pam'
match = re.search(pattern,'eggspamsausagespam')
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
str = 'My name is David. Hi David.'
print(str)
pattern = r'David'
newstr = re.sub(pattern,'Amy',str)
print(newstr)

'''
    #2 Metacharacters
    
    *I metacaratteri sono ciò che rende le espressioni
     regolari più potenti dei normali metodi di stringa.
    *Permettono di creare espressioni regolari per
     reppresentare dei concetti come 'una o più ripetizioni di una vocale'.
    *L'esistenza dei metacaratteri pone un problema se si
     vuole creare una espressione regolare che corrisponda ad
     un metacarattere letterale, come '$'.
    *Come abbiamo visto si può sfuggire da questi metacaratteri
     mettendo una (\)prima del carattere, (come \' per l'apice).
    *Tuttavia possono causare dei problemi, poiché i backslash
     hanno anche una funzione di escape nelle stringhe normali.
    *Questo si risolve con le row string, ovvero mettendo
     una (r) prima delle '' di una stringa.
    *Ci sono diversi metacaratteri:
        . -> Questo corrisponde a tutti i caratteri,
                     diverso da una nuova riga.
        ^ -> Questo corrisponde all'inizio di una stringa.
        $ -> Questo corrisponde alla fine di una stringa.
'''
print('LEZIONE #2')
# .
print('============== . ==============')
pattern = r'gr.y'
if re.match(pattern, 'grey'):
    print('Match 1')
if re.match(pattern, 'gray'):
    print('Match 2')
if re.match(pattern, 'blue'):
    print('Match 3')
# ^
print('============== ^ ==============')
pattern = r'^gr.y'
if re.match(pattern, 'grey'):
    print('Match 1')
if re.match(pattern, 'gray'):
    print('Match 2')
if re.match(pattern, 'stingray'):
    print('Match 3')
# $
print('============== $ ==============')
pattern = r'gr.y$'
if re.match(pattern, 'grey'):
    print('Match 1')
if re.match(pattern, 'gray'):
    print('Match 2')
if re.match(pattern, 'grea'):
    print('Match 3')

'''
    #3 Classi di caratteri
    
    *Le classi di caratteri forniscono un modo per
     abbinare solo uno di uno specifico insieme di caratteri.
    *Una classe di caratteri è creata mettendo i caratteri
     da abbinare dentro [] .
    *Ad esempio se mettiamo r'[aeiou]' e si fa una search,
     ricerca se all'interno della stringa è presente
     almeno uno tra i caratteri presenti nella stringa.
    *Le classi di carattere possono inoltre abbinare un range
     di caratteri, come ad esempio:
        [a-z] -> abbina tutti i caratteri alfabetici minuscoli.
        [G-P] -> abbina tutti i caratteri alfabetici da
                 G a P maiuscoli.
        [0-9] -> abbina ogni cifra.
    *Possono essere inclusi anche più di una classe, come:
        [A-Za-z] -> abbina una lettera sia maiuscola che minuscola.
    *Se viene messo (^) all'inizio della classe di caratteri
     verrà invertito il pattern (quindi ad esempio [^A-Z]
     esclude tutti i caratteri maiuscoli).
    *Non avrà nessun uso se non viene messo all'inizio della classe di
     caratteri.
'''
print('LEZIONE #3')
print('==============   ==============')
pattern = r'[aeiou]'
if re.search(pattern, 'grey'):
    print('Match 1')
if re.search(pattern, 'qwertyuiop'):
    print('Match 2')
if re.search(pattern, 'rhythm myths'):
    print('Match 3')
print('==============   ==============')
#in questo caso devono essere presenti due caratteri
#maiuscoli seguiti da una cifra
pattern = r'[A-Z][A-Z][0-9]'
if re.search(pattern, 'LS8'):
    print('Match 1')
if re.search(pattern, 'feFE9h6w'):
    print('Match 2')
if re.search(pattern, '1ab'):
    print('Match 3')
print('==============   ==============')
pattern = r'[^A-Z]'
if re.search(pattern, 'questo è tranquillo'):
    print('Match 1')
if re.search(pattern, 'AbCdEfG123'):
    print('Match 2')
if re.search(pattern, 'QUESTOECOMPLETAMENTEMUTO'):
    print('Match 3')

'''
    #4 Altri metacharacters
    
    *Ci sono altri metacharacters che specificano
     il numero di ripetizioni.
    *Vengono messi prima di un carattere, una classe o
     un gruppo di caratteri tra parentesi.
    *Tra questi ci sono:
        * -> sta per 'zero o più ripetizioni'.
        + -> sta per 'uno o più ripetizioni'.
        ? -> sta per 'zero o una ripetizione'.
        {x,y} -> rappresentano il numero di ripetizioni
              tra i due numeri messi all'interno
              (es {1,5} tra 1 e 5 ripetizioni).
'''
print('LEZIONE #4')
print('============== * ==============')
pattern = r'egg(spam)*' # in questo caso, la strigna deve iniziare con 'egg' e
                        # deve essere seguito da zero o più 'spam'
if re.match(pattern, 'egg'):
    print('Match 1')
if re.match(pattern, 'eggspamspamegg'):
    print('Match 2')
if re.match(pattern, 'spam'):
    print('Match 3')
print('============== + ==============')
pattern = r'g+' # in questo caso, la strigna deve avere all'inizio 
                # una o più 'g'
if re.match(pattern, 'g'):
    print('Match 1')
if re.match(pattern, 'ggggggggggg'):
    print('Match 2')
if re.match(pattern, 'abc'):
    print('Match 3')
print('============== ? ==============')
pattern = r'ice(-)?cream' # in questo caso, la strigna deve avere all'inizio 
                          # una o più 'g'
if re.match(pattern, 'ice-cream'):
    print('Match 1')
if re.match(pattern, 'icecream'):
    print('Match 2')
if re.match(pattern, 'ice--cream'):
    print('Match 3')
print('============== {} ==============')
pattern = r'9{1,3}$' 
if re.match(pattern, '9'):
    print('Match 1')
if re.match(pattern, '999'):
    print('Match 2')
if re.match(pattern, '9999'):
    print('Match 3')
print('==============   ==============')

'''
    #5 Gruppi
    
    *Un gruppo può essere creato mettendo tra ()
     un'espressione regolare.
    *Questo significa che un gruppo può essere
     dato come argomento a metacaratteri come (*) o (?).
    *Il contenuto dei gruppo in un abbinamento può essere
     accessibile usando la funzione group.
    *Richiamando group(0) o group() ritornerà tutte
     le corrispondenze.
    *Richiamando group(n), dove n è maggiore di 0,
     ritorna il gruppo n partendo da sinistra.
    *Richiamando groups() ritorna tutti i gruppi
     partendo dal primo.
    *Ci sono diversi tipi di gruppi speciali.
    *Due utili sono:
        named group -> (gruppo denominato) hanno il formato
                       (?P<name>...), dove name è il nome del gruppo,
                       e ... il contenuto; Funzionano nello stesso modo
                       dei gruppi normali, eccetto che sono accessibili
                       usando group(name).
        non-capturing groups -> (gruppi di non acquisizione) hanno il
                                formato (?:...) dove ... è il contenuto.
                                Non sono accessibili dal metodo group,
                                quindi possono essere aggiunti ad una
                                espressione regolare già esistente senza
                                rompere la numerazione.
    *Altro metacarattere:
        | -> Sta per 'or', quindi ad esempio
             (rosso|blu) abbina o rosso o blu.
'''
print('LEZIONE #5')
pattern = r'egg(spam)*'
if re.match(pattern, 'egg'):
    print('Match 1')
if re.match(pattern, 'eggspamspamspamegg'):
    print('Match 2')
if re.match(pattern, 'spam'):
    print('Match 3')
print('==============   ==============')
pattern = r'a(bc)(de)(f(g)h)i'
match = re.match(pattern, 'abcdefghijklmnop')
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
print('==============   ==============')
pattern = r'(?P<primo>abc)(?:def)(ghi)'
match = re.match(pattern, 'abcdefghi')
if match:
    print(match.group('primo'))
    print(match.groups())
print('============== | ==============')
pattern = r'gr(a|e)y'
if re.match(pattern, 'gray'):
    print('Match 1')
if re.match(pattern, 'grey'):
    print('Match 2')
if re.match(pattern, 'griy'):
    print('Match 3')
print('==============   ==============')

'''
    #6 Sequenze speciali
    
    *Ci sono varie sequenze speciali che si possono
     usare nelle espressioni regolari.
    *Sono scritte con una (\) seguito da un'altro carattere.
    *Un uso utile delle sequenze speciali è un (\) con un numero
     tra 1 e 99, (esempio \1 o \17).
    *Questo abbina l'espressione al gruppo del numero
     (esempio se ho [abc] [def] \2 abbina solo quelle del secondo gruppo
     ovvero def).
    *Altre sequenze speciali sono:
        \d -> abbina cifre (equivalente a [0-9]).
        \s -> abbina spazi bianchi (equivalente a [\t\n\r\f\v]).
        \w -> abbina caratteri delle parole (equivalente a [a-zA-Z0-9_])
              anche lettere con accenti.
        \D -> Tutto tranne cifre.
        \S -> Tutto tranne spazi bianchi.
        \W -> Tutto tranne caratteri delle parole.
        \A -> Abbina la parte iniziale di una stringa.
        \Z -> Abbina la parte finale di una stringa.
        \b -> Abbina una stringa vuota tra caratteri \w e \W,
              o caratteri \w e l'inizio o la fine di una stringa.
        \B -> Abbina una strigna vuota ovunque sia.
'''
print('LEZIONE #6')
pattern = r'(.+) \1' # si riferisce alla sottoespressione del primo
                     #gruppo, che è l'espressione corrispondente stessa
if re.match(pattern, 'word word'):
    print('Match 1')
if re.match(pattern, '?! ?!'):
    print('Match 2')
if re.match(pattern, 'abc cde'):
    print('Match 3')
print('==============   ==============')
pattern = r'(\D+\d)'
if re.match(pattern, 'Hi 999!'):
    print('Match 1')
if re.match(pattern, '1, 23, 456!'):
    print('Match 2')
if re.match(pattern, ' ! $?'):
    print('Match 3')
print('==============   ==============')
pattern = r'(\b(cat)\b)'
if re.search(pattern, 'The cat sat!'):
    print('Match 1')
if re.search(pattern, 'We s>cat<tered?'):
    print('Match 2')
if re.search(pattern, 'We scattered'):
    print('Match 3')

'''
    #7 Estrazione email
    
    *Dimostrazione dell'uso delle espressioni regolari.
    *Si crea un programma che estrae la mail
     da una stringa.
    *L'obbiettivo è quello di estrarre la
     sottostringa 'info@mail.com' dalla stringa
     str.
    *Una mail basica consiste in una parola e
     potrebbe contenere punti o trattini;
     seguiti poi dalla @ e il nome dominio
     (composto dal nome, un punto e il nome suffisso del dominio).
    *(\.) si mette la \ prima del (.) per dire che quello non è
     un carattere ma un punto vero e proprio.
'''
print('LEZIONE #7')
str = 'Per favore contatta info@mail.com per assistenza'
pattern = r'([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)'

match = re.search(pattern, str)
if(match):
    print(match.group())
