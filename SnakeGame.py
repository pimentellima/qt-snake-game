from PyQt5.QtWidgets import *
from Canvas import Canvas

import sys


def main():
    app = QApplication(sys.argv)
    window = SnakeGame()
    window.show()
    app.exec()


class SnakeGame(QMainWindow, Canvas):
    def __init__(self, *args, **kwargs):
        super(SnakeGame, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Box Filter")

