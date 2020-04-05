"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            **** Generatore di Istogrammi ****
Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, 
usando asterischi per disegnarlo. Ad esempio, data la lista [3,7,9,5] deve produrre questo grafico:

***

*******

*********

*****

"""

def is_int(val):
    if type(val) == int:
        return True
    else:
        if float(val).is_integer():
            return True
        else:
            return False





def soluzione12(lista):
    """questa è la doc-string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
    """
    
    for n in lista:
        if not is_int(n):
            print("Controllare la lista passata. Devono esserci solo interi")
            break
        else:
            print("*" * n) #super trick con le stringhe

            #stringOut = ""
            #for i in range(n):
                #stringOut += "*"          
            #print(stringOut)
        


#Test modulo
if __name__ == '__main__':
    l = [1,2,3,4]
    soluzione12(l)
    



        


