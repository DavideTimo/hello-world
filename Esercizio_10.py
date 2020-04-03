"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            **** Palindromo... o non Palindromo? ****
Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo(parole che si leggono 
uguali anche al contrario) oppure meno.
"""

from Esercizio_09 import soluzione9

def soluzione10(stringa1):
    """questa è la doc-string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
    """
    invert_stringa = soluzione9(stringa1)
    print("Invertita è: " + invert_stringa)
    if invert_stringa == stringa1:
        return True  #modifica per secondo commmit
    else:
        return False






#Test modulo
if __name__ == '__main__':
    print("aea è palindroma? : " + str(soluzione10("aea")))
    
    
    
