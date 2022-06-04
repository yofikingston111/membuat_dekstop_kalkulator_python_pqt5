import sys
from functools import partial
#import module from pyqt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication

class CalcUI(QMainWindow):
    def __init__(self):
        #initialize view
        super(). __init__()

        # set main window properties
        self.setWindowTitle("Kalkulator")
        self.setFixedSize(235, 235)

        #set central widget dan general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        #create display and button object
        self._createDisplay()
        self._createButton()

    #create function display
    def _createDisplay(self):
        #creating display
        self.display = QLineEdit()

        #set display properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        #add display to general layout
        self.generalLayout.addWidget(self.display)

    def _createButton(self):
        self.buttons = {}
        #set layout
        buttonsLayout = QGridLayout()

        #button text      | position on grid layout
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                    '1':(2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),


        }