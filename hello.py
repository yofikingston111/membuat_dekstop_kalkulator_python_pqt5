import sys
#Import module from pqt5
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
#create instance
app = QApplication(sys.argv)
window = QWidget()
#create title, and instance app
window.setWindowTitle('Simple App QT')
window.setGeometry(100, 100, 200, 80)
window.move(60, 15)
window.move(60, 16)

#create simple message
hello = QLabel('<H1> Halo saya sedang belajar membuat aplikasi dekstrop</h1>', parent=window)
web = QLabel('<h2> pesonainformatika.com</h2>', parent=window)
web.move(60, 60)
hello.move(60, 30)

#display app
window.show()

#run app
sys.exit(app.exec_())

