from PyQt5.uic.properties import QtGui

from World import POINT_WIDTH, POINT_HEIGHT

class Point:
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

    def draw(self, painter):
        painter.drawRect(self.px, self.py,  POINT_WIDTH, POINT_HEIGHT)
