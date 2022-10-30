from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QHBoxLayout, QMainWindow,QApplication,QLabel,QWidget, QStackedWidget, QShortcut
from Point import Point

SCOREBOARD_COLOR = QtGui.QColor(43, 43, 44)
TEXT_COLOR = QtGui.QColor(151, 117, 170)

class Scoreboard(QtWidgets.QWidget):

   def __init__(self):
      super().__init__()
      self.score = 0
      self.high_score = 0

      self.score_label = QLabel()
      self.high_score_label = QLabel() 
      score_palette = QPalette()
      score_palette.setColor(QPalette.WindowText, TEXT_COLOR)
      self.score_label.setText("Pontuação: " + str(self.score))
      self.high_score_label.setText("Maior pontuação: " + str(self.high_score))
      self.score_label.setPalette(score_palette)
      self.high_score_label.setPalette(score_palette)

      scoreboard_palette = QPalette()
      scoreboard_palette.setColor(QPalette.Window, SCOREBOARD_COLOR)
      self.setAutoFillBackground(True)
      self.setPalette(scoreboard_palette)
      self.setFixedSize(600,100)
      grid = QGridLayout()
      self.setLayout(grid)
      grid.addWidget(self.score_label, 0, 1)
      grid.addWidget(self.high_score_label, 0, 2)

   def increase_score(self):
      self.score += 1
      self.score_label.setText("Pontuação: " + str(self.score))

   def reset(self):
      if self.score > self.high_score:
         self.high_score = self.score
      self.high_score_label.setText("Maior pontuação: " + str(self.high_score))
      self.score = 0
      self.score_label.setText("Pontuação: " + str(self.score))
