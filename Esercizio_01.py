"""Scrivere un programma che: 
● prenda una stringa in input da tastiera, rappresentante un nucleotide (A,C,G,T) 
● stampi a video il nucleotide complementare   
Assicurarsi che il programma funzioni correttamente sia con input maiuscolo che minuscolo."""

def soluzione(textboxValue):
    print(textboxValue)                #printo solo per comodità supervisione quando faccio il debug
    risposta=[]
    for nucleotide in textboxValue:
        nucleotide=str(nucleotide).capitalize()   #It returns a copy of the string with only its first character capitalized (maiuscolo)
        if nucleotide=="A":
            risposta.append("T")
        elif nucleotide=="C":
            risposta.append("G")
        elif nucleotide=="G":
            risposta.append("C")
        elif nucleotide=="T":
            risposta.append("A")
        else:
            risposta=str(risposta)
            risposta="Immesso nucleotidi errati in input"
            break

    return risposta

"""
Soluzione migliore che utilizza un dizionario al posto dell'IF:

def soluzione(textboxValue):
    print(textboxValue)                    #printo solo per supervisione
    risposta=[]
    comptavola = {"A" : "T", "C" : "G", "G" : "C", "T" : "A"}
    nucleotidi = textboxValue.upper()         #The method upper() returns a copy of the string in which all case-based characters have been uppercased.
    try:
        risposta = str([ comptavola[n] for n in nucleotidi ])     #list comprehnsion, dove ogni elemento della lista viene preso dal dizionario
"""
