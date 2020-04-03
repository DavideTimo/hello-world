"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            Sei una Vocale?
Scrivi una funzione a cui viene passato un carattere come parametro, e che ci dice se il carattere è o meno una vocale.
"""

def soluzione6(carattere):
        """questa è la doc-string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
        Qui definisco come è fatta la finestra principale"""
    vocali = "aeiou"   #creo lista di vocali
    if carattere in vocali:
        return True
    else:
        return False #altra modifica

    






#Test modulo
if __name__ == '__main__':
    print("Dando la a il risultato è " + str(soluzione6("a")))
    print("Dando la c il risultato è " + str(soluzione6("c")))