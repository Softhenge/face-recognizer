
class Logger:
    def __init__(self, logWigdet):
        self.logWidget = logWigdet

    @staticmethod
    def log(text):
        Logger.logWidget.appendPlainText(text)