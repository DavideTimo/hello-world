"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            ****  Il linguaggio dei furfanti  ****
In Svezia, i bambini giocano spesso utilizzando un linguaggio un pó particolare, detto "rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo.
Ad esempio la parola "mangiare" diventa "momanongogiarore".
Scrivi una funzione in grado di tradurre una parola o frase passata tramite input() in "rövarspråket".
"""

def is_string(var):
    if type(var) == str:
        return True
    else:
        return False


def soluzione15(parola):
    if is_string(parola):
        nuovaparola=""
        vocali="aeiou"
        specialChar = [" ",",",".","?","!","'","%","," ]
        
        for lettera in parola:
            if lettera in vocali or lettera in specialChar:
                nuovaparola += lettera
            else:
                nuovaparola += lettera + "o" + lettera
        return nuovaparola


#Test modulo
if __name__ == '__main__':
    testo = input("/n Inserisci testo che desidere codificare: ")
    print("La codifica è : "+ str(soluzione15(testo)))

        

        
