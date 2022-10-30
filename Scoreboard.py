from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPalette
from Point import Point

SCOREBOARD_COLOR = QtGui.QColor(43, 43, 44)

class Scoreboard(QtWidgets.QWidget):
     def __init__(self):
        super().__init__()
        self.setFixedSize(600,100)
        scoreboard_palette = QPalette()
        scoreboard_palette.setColor(QPalette.Window, SCOREBOARD_COLOR)
        self.setAutoFillBackground(True)
        self.setPalette(scoreboard_palette)
