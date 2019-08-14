from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from dialogs.urldialog import Ui_URLDialog

class URLDialog(QDialog):
    okClickedSignal = pyqtSignal(['QString'])

    def __init__(self, mainForm):
        super().__init__()
        self.ui = Ui_URLDialog()
        self.ui.setupUi(self)
        self.mainForm = mainForm
        self.connect_all()

    def connect_all(self):
        self.ui.okButton.clicked.connect(self.okClicked)
        self.ui.cancelButton.clicked.connect(self.cancelClicked)
        self.okClickedSignal.connect(self.mainForm.urlSet)

    def okClicked(self):
        text = self.ui.textEdit.toPlainText()
        if (text):
            self.okClickedSignal.emit(text)
            self.close()

    def cancelClicked(self):
        self.close()

