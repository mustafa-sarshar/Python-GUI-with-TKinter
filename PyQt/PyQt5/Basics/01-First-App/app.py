from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def windows():
    app = QApplication(sys.argv)
    win = QMainWindow()
    x_pos, y_pos, width, height = 0, 0, 200, 250
    win.setGeometry(x_pos, y_pos, width, height)
    win.setWindowTitle("Test 1")

    label = QtWidgets.QLabel(win)
    label.setText("Label 1")
    label.move(50 ,50)

    win.show()
    sys.exit(app.exec_())

windows()