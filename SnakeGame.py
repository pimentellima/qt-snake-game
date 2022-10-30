from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from Canvas import Canvas
import sys

class SnakeGame(QMainWindow) :
    def __init__(self):
        super().__init__()
        canvas = Canvas()
        canvas.setVisible(True)
        self.setCentralWidget(canvas)
        self.setWindowTitle("Snake Game")


app = QApplication(sys.argv)
window = SnakeGame()
window.show()
app.exec()
