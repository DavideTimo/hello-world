"""
Questa è la doc_string del modulo. Questa descrizione è richiamabile con nomemodulo.__doc.

                Max tra Tre Numeri
Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!
"""
def soluzione5(a,b,c):

    if a >= b and a >= c:
        max = a
    elif b >= a and b >= c:
        max = b
    elif c >= a and c >= b:
        max = c

    return max



#Test modulo
if __name__ == '__main__':
    print("Dando i numeri 3,4,5 il risultato è " + str(soluzione5(3,4,5)))
    print("Dando i numeri 9,7,4 il risultato è " + str(soluzione5(9,7,4)))
    print("Dando i numeri 3,10,5 il risultato è " + str(soluzione5(3,10,5)))