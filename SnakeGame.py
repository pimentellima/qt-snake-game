from PyQt5.QtWidgets import *
from MainWindow import Ui_MainWindow

import sys


def main():
    app = QApplication(sys.argv)
    window = SnakeGame()
    window.show()
    app.exec()


class SnakeGame(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(SnakeGame, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Box Filter")

