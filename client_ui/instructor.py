import sys
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *


class NewWindow(QMainWindow):
    def __init__(self):
        super(NewWindow, self).__init__()
        self._new_window = None
        self._label = QLabel('Hello, is it me you\'re looking for?')
        self.setCentralWidget(self._label)


#if __name__ == '__main__':
#    app =QApplication([sys.argv])
#	ins_win = NewWindow()
#	sys.exit(app.exec_())