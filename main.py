import sys
from functools import partial
# import module from pyqt5
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
        # initialize view
        super().__init__()

        # set main window properties
        self.setWindowTitle("Kalkulator")
        self.setFixedSize(235, 235)

        # set central widget dan general layout
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        # create display and button object
        self._createDisplay()
        self._createButton()

    # create function display
    def _createDisplay(self):
        # creating display
        self.display = QLineEdit()

        # set display properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # add display to general layout
        self.generalLayout.addWidget(self.display)

    def _createButton(self):
        self.buttons = {}
        # set layout
        buttonsLayout = QGridLayout()

        # button text      | position on grid layout
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
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }
        # create button and add to grid layout
        for btnText, position in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnText], position[0], position[1])

        # add button layout to general layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')


class CalcController:
    def __init__(self, model, views):
        # initialize controller
        self._views = views
        self._evaluate = model

        # connecting to signal and slots
        self._connectSignals()

    # calculate result
    def _calculateResult(self):
        result = self._evaluate(expression=self._views.displayText())
        self._views.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._views.displayText() == ERROR_MSG:
            self._views.clearDisplay()
        expression = self._views.displayText() + sub_exp
        self._views.setDisplayText(expression)

    def _connectSignals(self):
        # connect to signal
        for btnText, btn in self._views.buttons.items():
            if btnText not in {'=': 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        self._views.buttons['='].clicked.connect(self._calculateResult)
        self._views.display.returnPressed.connect(self._calculateResult)
        self._views.buttons['C'].clicked.connect(self._views.clearDisplay)

#ERROR MESSAGE
ERROR_MSG = 'Errors'

# create model
def evaluateExpressionModel(expression):
    # evaluate expression
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result

def main():
    pycalc = QApplication(sys.argv)
    views = CalcUI()
    views.show()
    # create instance model of controller
    model = evaluateExpressionModel
    CalcController(model=model, views=views)

    sys.exit(pycalc.exec_())


if __name__ == '__main__':
    main()
