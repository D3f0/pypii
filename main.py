#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from PyQt4.QtGui import QApplication
from gui import MainWindow
import sys
def main(argv = sys.argv):
    app = QApplication(argv)
    win = MainWindow()
    win.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
    