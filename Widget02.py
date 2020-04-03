#!/usr/bin/python3
# -*- coding: utf-8 -*-



import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
    QTextEdit, QGridLayout, QApplication)
from PyQt5.QtGui import (QFont, QIcon)    


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.finestra_bassa()
        
        
    def finestra_bassa(self):
        
        self.setWindowTitle('Test richiesta dati')
        self.setWindowIcon(QIcon("Testpng.png"))
        
        #definisco le label
        label_nome = QLabel("Nome : ")
        label_cognome = QLabel("Cognome : ")
        label_ident = QLabel('Id : ')
        
        #definisco le linee editabile (dove l'user digita i propri dati)
        nome_edit = QLineEdit()
        cognome_edit = QLineEdit()
        identita_edit = QLineEdit()
        
        #creo un oggetto grid layout e invoco il metodo setSpacing con argomento 10
        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(10)
        
        grid.addWidget(label_nome,1,0)
        grid.addWidget(nome_edit,1,1)
        """grid.addWidget(label_cognome,2,0)
        grid.addWidget(cognome_edit,2,1)
        grid.addWidget(label_ident,3,0)
        grid.addWidget(identita_edit,3,1)"""
        
        
        #aggiunta pulsanti "Invio" e "cancella"
        
        #creo le istanze di due widget pulsanti
        invio_pulsante = QPushButton("Invio",self)
        invio_pulsante.clicked.connect(self.buttonClicked)
        cancella_pulsante = QPushButton("Cancella",self)
        cancella_pulsante.clicked.connect(self.buttonClicked)  
        
        box_orizzontale = QHBoxLayout()
        
        box_orizzontale.addStretch()
        box_orizzontale.addWidget(invio_pulsante)
        box_orizzontale.addWidget(cancella_pulsante)
        
        grid.addLayout(box_orizzontale, 2, 1, 1, 1) 

        
    def buttonClicked(self):
        print(' Hello ')        
       
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())