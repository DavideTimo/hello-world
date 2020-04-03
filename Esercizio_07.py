"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

                 Sommatrice Inarrestabile
Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.
"""


def soluzione7(lista):
    """questa è la doc string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
    """
    sum = 0
    for n in lista:
        try:
            sum += n
        except TypeError as err:
            print("C'è stato un errore : " + str(err))
    
    return sum





#Test modulo
if __name__ == '__main__':

    l = [1,2,3,4]
    print("La somma di questa lista (1,2,3,4) fa: " + str(soluzione7(l)))

    s= [1,2,3,"c"] #provo a sommare una lista con dentro un char per errore, per vedere se gestisce le eccezioni
    print("La somma di questa lista (1,2,3,c) fa: " + str(soluzione7(s)))