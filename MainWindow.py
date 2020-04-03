""" Questa è la doc_string del modulo(richiamabile con nomemodulo.__doc.
    Questo modulo genera la Main page da cui si avrà accesso ai vari esercizi svolti"""

import sys
from PyQt5.QtWidgets import QLabel, QAction, QMainWindow, QPushButton, QAction, QLineEdit, QMessageBox, QMenu, QApplication, qApp, QWidget, QToolTip, QTextEdit, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.Qt import QMenu

from Widget01 import finestraPiccola, finestraPiccola02, finestraPiccola03, finestraPiccola04
import Config

class finestraPrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stringaServer=Config.stringaServer
        self.descrittivo_finestraMain()

    def descrittivo_finestraMain(self):
        """questa è la doc string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
        Qui definisco come è fatta la finestra principale"""
        
        # creo una statusbar (nella mainwindow in basso) che mostra la scritta "Caricamento completato..."
        self.statusBar().showMessage("Caricamento completato - Ver.0.1.180714")

        # creo una barra dei menu (in alto nella mainwindow)
        barraMenu = self.menuBar()
        # aggiungo alla barra dei menu creata sopra la prima voce: "File"
        fileMenu = barraMenu.addMenu("&File")

        # alla voce File creata sopra aggiungo una sotto voce "Nuovo". 
        # queste sottovoci vengono chiamate QAction (azioni della barra del menu).
        Azione_Nuovo = QAction("Indirizzo",self)
        fileMenu.addAction(Azione_Nuovo)  #aggiungo alla barra dei menu creata prima l'azione appena creta

        # ora voglio aggiungere una voce che sia un "sotto menu". 
        # Quindi creo prima di tutto un QMenu
        serverString_subMenu  = QMenu("Stringa Server", self)
        # creo un'azione che andrò poi a legare stavolta al sottomenu
        importAct = QAction("Import mail",self)
        # aggiungo l'azione creata sopra al sottomenu
        serverString_subMenu.addAction(importAct)

        # aggiungo il sottomenu al menu principale creato prima.
        fileMenu.addMenu(serverString_subMenu)

        # creo anche la voce (azione) esci e la aggiungo nel sottomenu
        esciAct = QAction(QIcon("exit.png"), "&Esci", self)   #NB alla voce esci ho associato anche un'icona (png presente nella cartella)
        esciAct.setShortcut("Ctrl+Q")
        esciAct.setStatusTip("Exit Application")
        fileMenu.addAction(esciAct)                         #NB l'ordine in cui vengono aggiunti gli oggetti nel menu è poi l'ordine delle voci


        # ora definisco cosa fanno le voci (azioni) nella barra dei menu
        Azione_Nuovo.triggered.connect(self.on_click5)
        esciAct.triggered.connect(qApp.quit)
        
        # **** parametri della finestra  ****
        left=300
        top=300
        width=300
        height=300

        self.setWindowTitle("Test a caso")
        self.setGeometry(left,top,width,height)

        #pulsante esercizio 1
        self.button=QPushButton("Esercizio 1",self)
        self.button.move(20,40)
        self.button.clicked.connect(self.on_click)

        #pulsante esercizio 2
        self.button2=QPushButton("Esercizio 2",self)
        self.button2.move(20,80)
        self.button2.clicked.connect(self.on_click2)

        #pulsante esercizio 3
        self.button3=QPushButton("Esercizio 3",self)
        self.button3.move(20,120)
        self.button3.clicked.connect(self.on_click3)

        #pulsante cambio finestra
        self.button4=QPushButton("Opzioni",self)
        self.button4.move(20,160)
        self.button4.clicked.connect(self.on_click4)

        self.serverstring = QLineEdit(self)
        self.serverstring.move(20,200)
        self.serverstring.text = self.stringaServer
   
    def closeEvent(self, event):  
        #funzione che fa apparire un message box per essere sicuri di voler uscire dall'app       
        reply = QMessageBox.question(self, 'Closing program',
        "Are you sure to quit?", QMessageBox.Yes | 
        QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def on_click(self):
        """questa è la doc string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
        Qui definisco cosa accade quando viene premuto il pulsante esercizio 1
        la finestra main si chiude, viene creato un nuovo oggetto widget di nome finestra e viene visualizzato"""
        self.hide()
        self.finestra=finestraPiccola(self)
        self.finestra.show()

    def on_click2(self):
        """questa è la doc string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
        Qui definisco cosa accade quando viene premuto il pulsante esercizio 1
        la finestra main si chiude, viene creato un nuovo oggetto widget di nome finestra e viene visualizzato.
        Stavolta viene utilizzata la classe finestraPiccola02 definita in un suo modulo. La classe è una sottoclasse
        della prima. In questo modo ho sperimentato l'ereditarietà e riutilizzo del codice (NON ho creato una 
        finestra da zero ridefinendo tutti gli attributi"""
        self.hide()
        self.finestra=finestraPiccola02(self)
        self.finestra.show()

    def on_click3(self):
        """questa è la doc string della funzione, richiamabile con nomemodulo.nomefunzione.__doc__
        Qui definisco cosa accade quando viene premuto il pulsante esercizio 1
        la finestra main si chiude, viene creato un nuovo oggetto widget di nome finestra e viene visualizzato.
        Stavolta viene utilizzata la classe finestraPiccola03 definita in un suo modulo. La classe è una sottoclasse
        della prima. In questo modo ho sperimentato l'ereditarietà e riutilizzo del codice (NON ho creato una 
        finestra da zero ridefinendo tutti gli attributi"""
        self.hide()
        self.finestra=finestraPiccola03(self)
        self.finestra.show()

    def on_click4(self):
        """
        questa funzione di test serve a modificare gli attributi dell'oggetto mainwindow
        già creato. Infatti non voglio crearne uno nuovo ma usare lo stesso oggetto con gli attributi 
        modificati
        """
        self.button.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.hide()
        
    def on_click5(self):
        finestra5 = finestraPiccola04()
        finestra5.show
        

    @property
    def x(self):
        return self.stringaServer

    @x.setter
    def x(self, stringa):
        self.serverstring.text = stringa
         


