"""Calcolare la somma dei primi X (input) numeri naturali (da 0 a max 500 incluso)"""

def soluzione2(X):
    if X<501:
        somma=0
        for I in range(X):
            
            somma+=I
        
        return str(somma)
    else:
        str(somma="Numero troppo alto")

"""Altrimenti utilizzare la formula di Gauss"""

