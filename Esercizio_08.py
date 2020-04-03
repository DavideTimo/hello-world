"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            **** Moltiplicatore inarrestabile ****
Scrivi una funzione "moltiplicatrice" che moltiplica tra loro tutti gli elementi di una lista di numeri.
"""

def soluzione8(lista):
    """questa è la doc-string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
    """
    risultato = 1 #inizializzo variabile risultato (sennò ci da errore)
    for n in lista:
        if n == 0:
            risultato = 0
            break  #visto che devo fare una moltiplicazione, se trovo un valore di n=0, il risultato sarà zero e smetto di iterare
        try: 
            intero = int(n)
        except ValueError:
            pass
        else:
            risultato *= intero
    
    return risultato





#Test modulo
if __name__ == '__main__':

    l = [1,2,3,2]
    print("La somma di questa lista (1,2,3,4) fa: " + str(soluzione8(l)))

    s= [1,2,2,"c",2] #provo a sommare una lista con dentro un char per errore, per vedere se gestisce le eccezioni
    print("La somma di questa lista (1,2,3,c) fa: " + str(soluzione8(s)))

    s= [1,2,2,"c","2"] #provo a sommare una lista con dentro dei char per errore, per vedere se gestisce le eccezioni
    print("La somma di questa lista (1,2,3,c) fa: " + str(soluzione8(s)))