from PyQt4.Qt import *
from ui_imagewidget import Ui_ImageViewWidget



class ImageViewWidget(Ui_ImageViewWidget, QWidget):
    ''' Visualizador de imagenens '''
    ZOOM_MAX = 2
    ZOOM_MIN = .1
    __imageFile = ""
    qimage = QImage()
    
    def __init__(self, parent = None):
        super(ImageViewWidget, self).__init__(parent)
        self.setupUi(self)
        self.setupZoom()
        
    def setupZoom(self):
        self.slidemin, self.slidemax = self.sliderZoom.minimum(), self.sliderZoom.maximum()
        self.slidemed = (self.slidemax - self.slidemin) / 2

        self.zoom_under = (1 - self.ZOOM_MIN) / float(self.slidemax - self.slidemed)
        self.zoom_over = (self.ZOOM_MAX - 1) / float(self.slidemax - self.slidemed)
        
    def on_sliderZoom_sliderReleased(self):
        value = self.sliderZoom.value()
        if value == self.slidemed:
            self.zoom = 1
        elif value > self.slidemed:
            self.zoom = self.zoom_over * value
        else:
            self.zoom = self.zoom_under * value

    _zoom = 1
    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        if self.qimage.isNull():
            print "Can't zoom null image"
            return
        h, w = self.qimage.width() * value, self.qimage.height() * value
        print h, w
        zoomedPixmap = QPixmap(self.qimage).scaled(h, w)
        self.labelImage.setPixmap(zoomedPixmap)

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



    