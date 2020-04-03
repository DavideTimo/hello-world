"""● Scrivere una funzione conta_caratteri(s) che ritorni un dizionario contenente il numero 
di occorrenze per ciascun carattere presente nella stringa s:
 conta_caratteri('aiuola') {'a':2, 'i':1, 'u':1, 'o':1, 'l':1} 
 
 ● Facoltativo: risolvere l'esercizio utilizzando i costrutti per il controllo delle eccezioni.
"""
def soluzione3(stringa):
    dizionario_conteggio = {}
    for carattere in stringa:
        if carattere in dizionario_conteggio:
            dizionario_conteggio[carattere] += 1     #ricordati che la sintassi diz[c] indica l'elemento del dizionario diz, key c!!!!
        else:
            dizionario_conteggio[carattere] = 1      #ricordati la sintassi del dizionariooooo !!!11!
    
    #NB devo far tornare una stringa per visualizzarla con la GUI
    a = ""
    for i in dizionario_conteggio:
        a = a + str(i) + ":" + str(dizionario_conteggio[i]) + " ; "
        
    return a







