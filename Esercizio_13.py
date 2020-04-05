"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

            **** A ciascuno il suo  ****
Scrivi una funzione che, data in ingresso una lista A contenente parole, restituisce in output una lista B di interi 
che rappresentano la lunghezza delle parole contenute in A.
"""

def is_char(a):
    if type(a) == str:
        return True
    else:
        return False

def soluzione13(listaA):
    listaB=[]
    for parola in listaA:
        if is_char(parola):
            listaB.append(len(parola))
        else:
            print("Controlla la lista, deve essere composta soltanto da stringhe")
            break
    return listaB


#Test modulo
if __name__ == '__main__':
    A =["ciao", "pippo", "paperino", 4334, "pluto"]
    print(soluzione13(A))





        


