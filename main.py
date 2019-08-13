import sys
from mainWin.MainWin import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MainWin()
    w.show()
    app.exec_()