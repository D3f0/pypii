from PyQt4.Qt import *
from ui_imagewidget import Ui_ImageViewWidget



class ImageViewWidget(Ui_ImageViewWidget, QWidget):
    ''' Visualizador de imagenens '''
    __imageFile = None
    qimage = None
    def __init__(self, parent = None):
        super(ImageViewWidget, self).__init__(parent)
        self.setupUi(self)
        self.connectSignals()

    def connectSignals(self):
        pass

    @property
    def imageFile(self):
        return self.__imageFile


    @imageFile.setter
    def imageFile(self, newImageFile):
        qimg = QImage(newImageFile)
        if not qimg.isNull():
            self.qimage = qimg
            self.labelImage.setPixmap(QPixmap(qimg))
            self.__imageFile = newImageFile
        else:
            print "No es una imagen valida"



    