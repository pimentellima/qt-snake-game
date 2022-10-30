from PyQt5.uic.properties import QtGui
from PyQt5 import QtGui, QtWidgets
from constants import *

class Point(QtWidgets.QWidget):

    def __init__(self, px, py):
        self.px = px
        self.py = py

    def setLocation(self, px, py):
        self.px = px
        self.py = py

    def getPx(self):
        return self.px

    def getPy(self):
        return self.py

    def draw(self, qp):
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        qp.drawRoundedRect(self.px, self.py,  POINT_WIDTH, POINT_HEIGHT, 8, 8)