# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/mainwindow.ui'
#
# Created: Sat Sep 24 19:02:59 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(598, 356)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widgetSource = ImageViewWidget(self.centralwidget)
        self.widgetSource.setObjectName(_fromUtf8("widgetSource"))
        self.horizontalLayout.addWidget(self.widgetSource)
        self.widgetDest = ImageViewWidget(self.centralwidget)
        self.widgetDest.setObjectName(_fromUtf8("widgetDest"))
        self.horizontalLayout.addWidget(self.widgetDest)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open_Image = QtGui.QAction(MainWindow)
        self.action_Open_Image.setObjectName(_fromUtf8("action_Open_Image"))
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setObjectName(_fromUtf8("action_Close"))
        self.actionAboutthis_application = QtGui.QAction(MainWindow)
        self.actionAboutthis_application.setObjectName(_fromUtf8("actionAboutthis_application"))
        self.menuFile.addAction(self.action_Open_Image)
        self.menuFile.addAction(self.action_Close)
        self.menuHelp.addAction(self.actionAboutthis_application)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open_Image.setText(QtGui.QApplication.translate("MainWindow", "&Open Image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open_Image.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutthis_application.setText(QtGui.QApplication.translate("MainWindow", "Aboutthis application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutthis_application.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))

from imageviewwidget import ImageViewWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

