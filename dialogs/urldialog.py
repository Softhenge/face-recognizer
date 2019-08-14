# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'urldialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_URLDialog(object):
    def setupUi(self, URLDialog):
        URLDialog.setObjectName("URLDialog")
        URLDialog.resize(375, 86)
        self.horizontalLayoutWidget = QtWidgets.QWidget(URLDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 351, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(URLDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(230, 60, 141, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)

        self.retranslateUi(URLDialog)
        QtCore.QMetaObject.connectSlotsByName(URLDialog)

    def retranslateUi(self, URLDialog):
        _translate = QtCore.QCoreApplication.translate
        URLDialog.setWindowTitle(_translate("URLDialog", "Live Camera Setup"))
        self.label.setText(_translate("URLDialog", "Camera URL:"))
        self.okButton.setText(_translate("URLDialog", "OK"))
        self.cancelButton.setText(_translate("URLDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    URLDialog = QtWidgets.QDialog()
    ui = Ui_URLDialog()
    ui.setupUi(URLDialog)
    URLDialog.show()
    sys.exit(app.exec_())
