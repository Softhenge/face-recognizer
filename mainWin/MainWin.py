import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mainWin.MainWindow import Ui_MainWindow
from dialogs.GetUrlDialog import URLDialog

import threading

from Logger import *
from compute_encodings import *
from recognize_from_video import *

class MainWin(QMainWindow):
    datasetSelected = pyqtSignal()
    # urlSet = pyqtSlot()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connectAll()
        self.plainTextEdit = QPlainTextEdit()
        self.ui.logsWidget.setWidget(self.plainTextEdit)
        Logger.logWidget = self.plainTextEdit
        self.datasetPath = ''
        self.url = ""

    def connectAll(self):
        self.ui.selectDatasetButton.clicked.connect(self.selectDatasetClicked)
        self.ui.generateEncodingsButton.clicked.connect(self.generateEncodingsClicked)
        self.ui.fromImageButton.clicked.connect(self.recFromImageClicked)
        self.ui.fromVideoFileButton.clicked.connect(self.recFromVideoFileClicked)
        self.ui.fromCamButton.clicked.connect(self.recFromCamClicked)
        self.ui.fromLiveStreamButton.clicked.connect(self.recFromLiveStreamClicked)

    # slots
    def selectDatasetClicked(self):
        Logger.log("clicked")
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog

        self.datasetPath = str(QFileDialog.getExistingDirectory(self, "Select Dataset Folder"))
        self.ui.datasetPathLabel.setText(self.datasetPath)

    def generateEncodingsClicked(self):
        thread = threading.Thread(target=self.computeEncodings)
        thread.start()

    def computeEncodings(self):
        FaceEncoder.getFaceEncoder(self).generate_encodeings(self.datasetPath, "encodings.pickle")

    def recFromImageClicked(self):
        filename = self.selectImageFile()
        if filename:
            FaceRecognizer.getFaceRecognizer(self).recognize_from_image(filename)

    def selectImageFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select image file", "", "Image Files (*.png *.jpg *.bmp)")
        return fileName

    def recFromVideoFileClicked(self):
        filename = self.selectVideoFile()
        if filename:
            FaceRecognizer.getFaceRecognizer(self).recognize_from_video(filename)

    def selectVideoFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select video file", "", "Video Files (*.mp4 *.avi)")
        return fileName

    def recFromCamClicked(self):
        FaceRecognizer.getFaceRecognizer(self).recognize_from_video()

    def recFromLiveStreamClicked(self):
        self.urldialog = URLDialog(self)
        self.urldialog.exec_()

    def urlSet(self, url):
        self.url = url
        FaceRecognizer.getFaceRecognizer(self).recognize_from_video(url)
        print(url)

    def getDetectionMethod(self):
        detMethod = 'cnn'
        if (self.ui.hogRadioButton.isChecked()):
            detMethod = 'hog'
        elif (self.ui.cascadeRadioButton.isChecked()):
            detMethod = 'cascade'

        return detMethod

    def getUpsampleNumber(self):
        return self.ui.numOfTimesToUpsampleSpinBox.value()

    def getJittersNumber(self):
        return self.ui.numOfJittersSmpiBox.value()

    def getTolerance(self):
        return self.ui.toleranceSpinBox.value()

    def getScaleFactor(self):
        return self.ui.scaleFactor.value()

    def getMinNeighbors(self):
        return self.ui.minNeighboursSpinBox.value()