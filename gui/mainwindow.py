from PyQt4.Qt import *
from ui_mainwindow import Ui_MainWindow
from os.path import isfile

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


    @pyqtSignature('')
    def on_action_Open_Image_triggered(self):
        startFolder = ""
        f = QFileDialog.getOpenFileName(self,
                                    self.trUtf8("Please chosse an image to open"),
                                    startFolder,
                                    self.trUtf8("Images (*.png *.xpm *.jpg *.tiff *.bmp);; Anything (*.*);;"))
        
        self.widgetSource.imageFile = f # Setter

    