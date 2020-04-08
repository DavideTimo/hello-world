"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            ****  Solamente per Soci  ****
Scrivi una funzione a cui vengono passati un valore e una lista di valori,
 e che ti dica in output se il valore passato è presente o meno nella lista.
"""

def soluzione16(val,lista):
    if val in lista:
        print( f"il valore {val} è compreso nella lista. Ed occupa il posto {lista.index(val)+1} !")
        return True
    else:
        return False

#Test modulo
if __name__ == '__main__':
    lista1=[1,2,3,4,5]
    val=4
    print(str(soluzione16(val,lista1)))