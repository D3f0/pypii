from PyQt4.Qt import *
from ui_imagewidget import Ui_ImageViewWidget



class ImageViewWidget(Ui_ImageViewWidget, QWidget):
    def __init__(self, parent = None):
        super(ImageViewWidget, self).__init__(parent)
        self.setupUi(self)