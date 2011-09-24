# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/imagewidget.ui'
#
# Created: Sat Sep 24 19:21:10 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ImageViewWidget(object):
    def setupUi(self, ImageViewWidget):
        ImageViewWidget.setObjectName(_fromUtf8("ImageViewWidget"))
        ImageViewWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(ImageViewWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(ImageViewWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.scrollArea = QtGui.QScrollArea(ImageViewWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 386, 228))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelImage = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.labelImage.setText(_fromUtf8(""))
        self.labelImage.setObjectName(_fromUtf8("labelImage"))
        self.verticalLayout_2.addWidget(self.labelImage)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushOpen = QtGui.QPushButton(ImageViewWidget)
        self.pushOpen.setObjectName(_fromUtf8("pushOpen"))
        self.horizontalLayout.addWidget(self.pushOpen)
        self.pushSave = QtGui.QPushButton(ImageViewWidget)
        self.pushSave.setObjectName(_fromUtf8("pushSave"))
        self.horizontalLayout.addWidget(self.pushSave)
        self.pushButton = QtGui.QPushButton(ImageViewWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(ImageViewWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.sliderZoom = QtGui.QSlider(ImageViewWidget)
        self.sliderZoom.setMinimum(1)
        self.sliderZoom.setProperty(_fromUtf8("value"), 50)
        self.sliderZoom.setOrientation(QtCore.Qt.Horizontal)
        self.sliderZoom.setInvertedAppearance(False)
        self.sliderZoom.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sliderZoom.setObjectName(_fromUtf8("sliderZoom"))
        self.horizontalLayout.addWidget(self.sliderZoom)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ImageViewWidget)
        QtCore.QMetaObject.connectSlotsByName(ImageViewWidget)

    def retranslateUi(self, ImageViewWidget):
        ImageViewWidget.setWindowTitle(QtGui.QApplication.translate("ImageViewWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ImageViewWidget", "Imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOpen.setText(QtGui.QApplication.translate("ImageViewWidget", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.pushSave.setText(QtGui.QApplication.translate("ImageViewWidget", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ImageViewWidget", "Curvas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImageViewWidget", "Zoom", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImageViewWidget = QtGui.QWidget()
    ui = Ui_ImageViewWidget()
    ui.setupUi(ImageViewWidget)
    ImageViewWidget.show()
    sys.exit(app.exec_())

