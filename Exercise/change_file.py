def open_file_r(p):
    try:
        f = open(p,'r')
        txt = f.read()
    except:
        print('è stato scontrato un errore')
    finally:
        f.close()
    return txt
def open_file_w(p,txt):
    try:
        f = open(p,'w')
        f.write(txt)
    except:
        print('è stato scontrato un errore')
    finally:
        f.close()
    return True
def main():
    path_r = input('Inserisci la path del file da leggere: ')
    text = open_file_r(path_r)
    path_w = input('Inserisci la path del file da scrivere: ')
    ris = open_file_w(path_w,text)
    print('File creato e scritto: ' + str(ris))
main()
input()
