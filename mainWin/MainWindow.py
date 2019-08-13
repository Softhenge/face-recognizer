# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 220, 341, 91))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectDatasetButton = QtWidgets.QPushButton(self.groupBox)
        self.selectDatasetButton.setObjectName("selectDatasetButton")
        self.horizontalLayout.addWidget(self.selectDatasetButton)
        self.datasetPathLabel = QtWidgets.QLabel(self.groupBox)
        self.datasetPathLabel.setText("")
        self.datasetPathLabel.setObjectName("datasetPathLabel")
        self.horizontalLayout.addWidget(self.datasetPathLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.generateEncodingsButton = QtWidgets.QPushButton(self.groupBox)
        self.generateEncodingsButton.setObjectName("generateEncodingsButton")
        self.horizontalLayout_2.addWidget(self.generateEncodingsButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 30, 120, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.hogRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.hogRadioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.hogRadioButton.setChecked(True)
        self.hogRadioButton.setObjectName("hogRadioButton")
        self.cnnRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.cnnRadioButton.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.cnnRadioButton.setObjectName("cnnRadioButton")
        self.cascadeRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.cascadeRadioButton.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.cascadeRadioButton.setObjectName("cascadeRadioButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 210, 171, 111))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.fromImageButton = QtWidgets.QPushButton(self.groupBox_3)
        self.fromImageButton.setGeometry(QtCore.QRect(10, 10, 151, 23))
        self.fromImageButton.setObjectName("fromImageButton")
        self.fromVideoFileButton = QtWidgets.QPushButton(self.groupBox_3)
        self.fromVideoFileButton.setGeometry(QtCore.QRect(10, 40, 151, 23))
        self.fromVideoFileButton.setObjectName("fromVideoFileButton")
        self.fromCamButton = QtWidgets.QPushButton(self.groupBox_3)
        self.fromCamButton.setGeometry(QtCore.QRect(10, 70, 151, 23))
        self.fromCamButton.setObjectName("fromCamButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(370, 10, 411, 181))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.numOfTimesToUpsampleSpinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.numOfTimesToUpsampleSpinBox.setMinimum(1)
        self.numOfTimesToUpsampleSpinBox.setMaximum(10)
        self.numOfTimesToUpsampleSpinBox.setObjectName("numOfTimesToUpsampleSpinBox")
        self.horizontalLayout_4.addWidget(self.numOfTimesToUpsampleSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.numOfJittersSmpiBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.numOfJittersSmpiBox.setMinimum(1)
        self.numOfJittersSmpiBox.setMaximum(10)
        self.numOfJittersSmpiBox.setProperty("value", 3)
        self.numOfJittersSmpiBox.setObjectName("numOfJittersSmpiBox")
        self.horizontalLayout_3.addWidget(self.numOfJittersSmpiBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.toleranceSpinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.toleranceSpinBox.setMaximum(100)
        self.toleranceSpinBox.setSingleStep(5)
        self.toleranceSpinBox.setProperty("value", 60)
        self.toleranceSpinBox.setObjectName("toleranceSpinBox")
        self.horizontalLayout_5.addWidget(self.toleranceSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.scaleFactor = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.scaleFactor.setDecimals(1)
        self.scaleFactor.setMinimum(1.1)
        self.scaleFactor.setMaximum(2.0)
        self.scaleFactor.setSingleStep(0.1)
        self.scaleFactor.setProperty("value", 1.1)
        self.scaleFactor.setObjectName("scaleFactor")
        self.horizontalLayout_6.addWidget(self.scaleFactor)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.minNeighboursSpinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.minNeighboursSpinBox.setMaximum(20)
        self.minNeighboursSpinBox.setProperty("value", 3)
        self.minNeighboursSpinBox.setObjectName("minNeighboursSpinBox")
        self.horizontalLayout_7.addWidget(self.minNeighboursSpinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.logsWidget = QtWidgets.QDockWidget(MainWindow)
        self.logsWidget.setMaximumSize(QtCore.QSize(524287, 300))
        self.logsWidget.setObjectName("logsWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.logsWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.logsWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognizer"))
        self.groupBox.setTitle(_translate("MainWindow", "Encoding generation"))
        self.selectDatasetButton.setText(_translate("MainWindow", "Select Dataset Folder"))
        self.generateEncodingsButton.setText(_translate("MainWindow", "Generate"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Detection Method"))
        self.hogRadioButton.setText(_translate("MainWindow", "HOG"))
        self.cnnRadioButton.setText(_translate("MainWindow", "CNN"))
        self.cascadeRadioButton.setText(_translate("MainWindow", "Cascade"))
        self.fromImageButton.setText(_translate("MainWindow", "Recognize From Image"))
        self.fromVideoFileButton.setText(_translate("MainWindow", "Recognize From Video File"))
        self.fromCamButton.setText(_translate("MainWindow", "Recognize From Video Cam"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Detection / Recognition parameters"))
        self.label.setText(_translate("MainWindow", "Number of times to upsample"))
        self.label_2.setText(_translate("MainWindow", "Number of jitters"))
        self.label_3.setText(_translate("MainWindow", "Tolerance"))
        self.label_4.setText(_translate("MainWindow", "Scale Factor (Cascade)"))
        self.label_5.setText(_translate("MainWindow", "Min Neighbors (Cascade)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
