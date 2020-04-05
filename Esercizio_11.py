"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            **** Scriviamo la nostra versione di len() ****
Scrivi una funzione che manda in print la lunghezza di una stringa o lista passata come parametro.
In sostanza, seppur presente, provate a scrivere la vostra versione della funzione len()!
"""

def soluzione11(list_or_string):
    """questa è la doc-string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
    """
    lunghezza = 0
    for n in list_or_string:
        lunghezza += 1
    return lunghezza


#Test modulo
if __name__ == '__main__':
    print("La lunghezza di aea è : " + str(soluzione11("aea")))
    print("La lunghezza di null è : " + str(soluzione11("")))



