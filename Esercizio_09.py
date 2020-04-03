"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            **** Reverser ****
Scrivi una funzione a cui passerai come parametro una stringa e ti restituirà una 
versione della stessa stringa al contrario (ad esempio "abcd" diventa "dcba".
"""

def soluzione9(stringa1):
    """questa è la doc-string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
    """
    indice = len(stringa1) - 1
    reverseString = ""  #inizializzo una stringa vuota

    # Modo utilizando ciclo for
    #for n in range(indice,0,-1):
        #reverseString += stringa1[n]

    while indice >= 0:
        reverseString += stringa1[indice]
        indice -= 1

    return reverseString






# test modulo
if __name__ == '__main__':
    a = "Ciao"
    rint("L'inverso di " + a + " è " + soluzione9(a))