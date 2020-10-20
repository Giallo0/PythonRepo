import os
#*******************************************#
#          DEFINIZIONE FUNZIONI             #
#*******************************************#
def F0010_carica_alfabeto(dicti,r_dicti):
    f = open('Alphabet.mbg','r')
    for line in f:
        word = ''
        key = 0
        lett = ''
        for ch in line:
            if(ch != ':') and (ch != '\n'):
                word += ch
            elif(ch == ':'):
                key = int(word)
                word = ''
            else:
                lett = str(word)
                word = ''
        dicti[key] = lett
    tmp_list = list()
    for ch in dicti:
        tmp_list.append(dicti[ch])
    tmp_list = tmp_list[::-1]
    for cnt in range(1,27):
        r_dicti[cnt] = tmp_list[cnt-1]
    f.close()
#===========================================#   
def F0020_azione_utente():
    inp = 0
    while((inp < 1) or (inp > 4)):
        inp = int(input("""
SECRET MESSAGE

Opzioni:

1. Decifra messaggio
2. Crypta messaggio
3. Mostra testo criptato
4. Esci

Risposta: """))
        if((inp < 1) or (inp > 4)):
            print('Opzione inesistente')
    if(inp == 1):
        return 'Dec'
    elif(inp == 2):
        return 'Cry'
    elif(inp == 3):
        return 'Stc'
    elif(inp == 4):
        return 'Ext'
#===========================================#
def F0030_decifra_messaggio(dicti,r_dicti):
    path = 'Shared_Text.txt'
    f = open(path,'r')
    Text = f.read()
    f.close()

    space = ' '
    New_Text = ''
    for ch in Text:
        for cnu in range(len(r_dicti)):
            if(ch == r_dicti[cnu+1]):
                New_Text += dicti[cnu+1]
                break
            elif(ch == space):
                New_Text += space
                break
            else:
                continue
    return New_Text

#===========================================#
def F0040_crypta_messaggio(dicti,r_dicti):
    space = ' '
    Text = input('Scrivi:\n')
    Text = Text.lower()
    New_Text = ''
    for ch in Text:
        for cnu in range(len(dicti)):
            if(ch == dicti[cnu+1]):
                New_Text += r_dicti[cnu+1]
                break
            elif(ch == space):
                New_Text += space
                break
            else:
                continue
    print(New_Text)
    return New_Text

#===========================================#
def F0050_stampa_testo(New_Text):
    inp = 0
    while((inp < 1) or (inp > 2)):
        inp = int(input("""
Stampare il messaggio?

Opzioni:

1. Si
2. No

Risposta: """))
        if((inp < 1) or (inp > 2)):
            print('Opzione inesistente')
    if(inp == 1):
        path = 'Shared_Text.txt'
        f = open(path,'w')
        f.write(New_Text)
        f.close()
        return True
    elif(inp == 2):
        return False

#===========================================#
def F0060_mostra_testo_cry():
    path = 'Shared_Text.txt'
    f = open(path,'r')
    Text = f.read()
    f.close()
    return Text
#============= MAIN ========================#
def main():    
    Alphabet = {}
    r_Alphabet = {}
    F0010_carica_alfabeto(Alphabet,r_Alphabet)
    Azione = ''
    while(Azione != 'Ext'):
        Azione = F0020_azione_utente()
        if(Azione == 'Dec'):
            os.system('CLS')
            Nuovo_Testo = F0030_decifra_messaggio(Alphabet,r_Alphabet)
            os.system('CLS')
            if(Nuovo_Testo):
                print('Testo decifrato:\n\n')
                print(Nuovo_Testo)
            else:
                print('Testo decriptato:',False)
            input('...')
        elif(Azione == 'Cry'):
            os.system('CLS')
            Nuovo_Testo = F0040_crypta_messaggio(Alphabet,r_Alphabet)
            os.system('CLS')
            if(Nuovo_Testo):
                os.system('CLS')
                sts = F0050_stampa_testo(Nuovo_Testo)
                os.system('CLS')
                print('Testo stampato:', sts)
            else:
                print('Testo cryptato:',False)
            input('...')
        elif(Azione == 'Stc'):
            os.system('CLS')
            Nuovo_Testo = F0060_mostra_testo_cry()
            os.system('CLS')
            if(Nuovo_Testo):
                print('Testo all\'interno del file:\n\n')
                print(Nuovo_Testo)
            else:
                print('File letto:',False)
            input('...')
        os.system('CLS')
#============ CORPO =======================#
main()
