from PyQt4.Qt import *
from ui_mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.connectSignals()

    def connectSignals(self):
        self.action_Open_Image.triggered.connect(self.openFile)

    def openFile(self):
        startFolder = ""
        f = QFileDialog.getOpenFileName(self,
                                    self.trUtf8("Please chosse an image to open"),
                                    startFolder,
                                    self.trUtf8("Images (*.png *.xpm *.jpg *.tiff *.bmp);; Anything (*.*);;"))
        print f

    