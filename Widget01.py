""" Questa è la doc_string del modulo(richiamabile con nomemodulo.__doc.
    Questo modulo definisce una finestra secondaria (un widget)"""

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox,
    QTextEdit, QGridLayout, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from Esercizio_01 import soluzione as soluzione1
from Esercizio_02 import soluzione2 as soluzione2
from Esercizio_03 import soluzione3 as soluzione3
import Config

stringa_server=""

class finestraPiccola(QWidget):         #visto che non devo utilizzare strumenti molto complessi posso usare un semplice QWidget invece di una QMainWindow
    def __init__(self,mainwindow):      #mando l'oggetto mainwindow nel costruttore per poi stokkarlo come attributo. Mi servirà per richiamarlo con il pulsante di back!!!!
        super().__init__()
        
        self.mainwindow=mainwindow
        self.descrittivo_finestra()   

    def descrittivo_finestra(self):
        left=300
        top=300
        width=350
        height=120
        
        self.setWindowTitle("Nucleotide in input (A,C,G,T)")
        self.setGeometry(left,top,width,height)
        
        #creo una label 
        self.label_nome=QLabel("inserire nucleotidi",self)
        self.label_nome.move(10,30)

        #creo una textbox (QLineEdit) dentro la finestra
        self.textbox=QLineEdit(self)
        self.textbox.move(150,20)
        self.textbox.resize(150,35)

        #creo un pulsante Invio dentro la finestra
        self.buttonInvio = QPushButton("Invia", self)
        self.buttonInvio.move(20,80)

        #creo un pulsante Indietro dentro la finestra
        self.buttonIndietro = QPushButton("Indietro", self)
        self.buttonIndietro.move(260,80)

        # collego il pulsante INVIO alla funzione on_click
        #quando il pulsante viene premuto viene richiamata la funzione Soluzione importata da Esercizio01
        self.buttonInvio.clicked.connect(self.on_click_Sol1)

        #collego pulante INDIETRO alla funzione on_click_back
        self.buttonIndietro.clicked.connect(self.on_click_back)

    @pyqtSlot()              #Python decorator
    def on_click_back(self):
        self.hide()
        self.mainwindow.show()

    @pyqtSlot()               #Python decorator
    def on_click_Sol1(self):
        """questo metodo di classe viene "attivato" appena viene premuto il pulsante.
           il cuore del metodo è contenuto in un altro modulo, che effettua il controllo e fornisce in output 
           il risultato voluto. Per poter richiamare la funzione definita nel modulo Esercizio_01, 
           ho dovuto fare l'import DENTRO il metodo di classe. Altrimenti non si sarebbero "visti".
        """
        
        textboxValue = list(self.textbox.text())
        risposta=soluzione1(textboxValue)
        QMessageBox.question(self, 'SvartJugend.com', "Nucleotidi complementari: " + str(risposta), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")      #qui resetto empty il testo all'interno della textbox (QLineEdit)
    
"""dichiaro una sottoclasse di finestraPiccola (riutilizzo del codice)"""

class finestraPiccola02(finestraPiccola):
    def __init__(self, mainwindow):
        finestraPiccola.__init__(self, mainwindow)   
        
        self.setWindowTitle("Somma dei numeri naturali")
        self.label_nome.setText("Calcolo dei primi X naturali. X=")
        
    def on_click_Sol1(self):    #method OVERRIDE. Sovrascrivo il metodo dell'oggetto padre
        """richiamo stavolta l'algoritmo soluzione 2"""      
        textboxValue = (int(self.textbox.text()) if self.textbox.text() != '' else 0)   #if statement inline: <expression1> if <condition> else <expression2>
        risposta = soluzione2(textboxValue)
        QMessageBox.question(self, 'SvartJugend.com', "Somma dei primi X numeri nat: " + str(risposta), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")      #qui resetto empty il testo all'interno della textbox (QLineEdit)

class finestraPiccola03(finestraPiccola):
    def __init__(self, mainwindow):
        finestraPiccola.__init__(self, mainwindow)  
        self.setWindowTitle("Calcola numero occorrenze di ciascun carattere")
        self.label_nome.setText("Digita stringa = ")
    
    def on_click_Sol1(self):        
        risposta = soluzione3(self.textbox.text())
        QMessageBox.question(self, 'SvartJugend.com', "Conteggio dei caratteri: " + str(risposta), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")      #qui resetto empty il testo all'interno della textbox (QLineEdit)

class finestraPiccola04(QWidget):
    def __init__(self):
        super().__init__()
       
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Test richiesta dati')

        testo_label = QLabel("Imputa stringa : ")
        self.stringa_edit = QLineEdit()

        #creo oggetto griglia
        grid = QGridLayout()
        #setto la griglia creata come layout della finestra
        self.setLayout(grid)
        # set spacing
        grid.setSpacing(5)
        #aggiungo alla griglia gli oggetti label e lineEdit
        grid.addWidget(testo_label,1,0)
        grid.addWidget(self.stringa_edit,1,1)  

        invio_pulsante = QPushButton("Invio",self)
        cancella_pulsante = QPushButton("Cancella",self)

        #creo un box orizzontale
        box_orizzontale = QHBoxLayout()
        box_orizzontale.addStretch()
        box_orizzontale.addWidget(invio_pulsante)
        box_orizzontale.addWidget(cancella_pulsante)

        #aggiungo il box orizzontale alla griglia di prima
        grid.addLayout(box_orizzontale, 2, 1, 1, 1) #Il secondo e il terzo argomento specificano la riga e la colonna in cui viene inserito il widget, mentre la terza e la quarta specificano l'intervallo di righe e di colonna.
        
        invio_pulsante.clicked.connect(self.invioClicked)
        cancella_pulsante.clicked.connect(self.cancellaClicked)

    def invioClicked(self):
        global stringa_server
        if self.stringa_edit.text() != "":
            stringa_server = self.stringa_edit.text()
            print(stringa_server)
            Config.stringaServer = str(stringa_server)
            self.hide
            

        else:
            pass
        
    def cancellaClicked(self):
        self.hide()
    """
    NB una volta premuto invio la stringa viene salvata in un attributo dell'oggetto "FinestraPiccola04"
    Questo attributo è self.stringa_server
    adesso però ho bisogno di poterlo spacciare in giro questo attributo, per renderlo leggibile anche ad
    altri moduli/oggetti.
    Quindi creo un metodo "GET" che se chiamato restituisce appunto il dato."""
    def get_string():
        return "{0}".format(self.stringa_server)


        