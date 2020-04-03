"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

       Max TRA DUE NUMERI   
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else 
per la scrittura dell'algoritmo.
"""
def soluzione4(a,b):
    if a>=b:
        max = a
    else:
        max = b
    return max


# Test modulo
#print("Il risultato è " + str(soluzione4(3,5)))
#print(soluzione4(7,6))
#print(soluzione4(1,1))