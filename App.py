import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import finestraPrincipale
from Widget01 import finestraPiccola04

#anche qui un commentino ci sta
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = finestraPrincipale()
    
    ex.show()
    sys.exit(app.exec_())



    
