"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            **** Il Maggiore tra tutti!  ****
Scrivi un programma che, passata come parametro una lista di interi, 
fornisce in output il maggiore tra i numeri contenuti nella lista.
"""

def is_int(var):
    if type(var) == int or type(var) == float:
        return True
    else:
        return False

def soluzione14(listaInt):
    maggiore = listaInt[0]
    for n in listaInt: #controllo che nella lista ci siano solo dei numeri
        if not is_int(n):
            print("Controlla che tutti gli elementi della lista siano numeri")
            break
        else:
            if n >= maggiore:
                maggiore = n
    
    return maggiore
        
#Test modulo
if __name__ == '__main__':
    lista1 = [9,1,2,4,3,7,"a"]
    print("Trova maggiore di (1,2,4,3) " + str(soluzione14(lista1)))
        

