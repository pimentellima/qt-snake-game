from tkinter import CENTER
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow,QApplication,QLabel,QWidget, QStackedWidget, QShortcut
from PyQt5.QtGui import QPixmap, QPalette, QKeySequence
from PyQt5.QtCore import Qt
from World import World
from Scoreboard import Scoreboard

GAME_COLOR = QtGui.QColor(60, 63, 65)
TEXT_COLOR = QtGui.QColor(151, 117, 170)
DEFAULT_FONT = QtGui.QFont("SANS SERIF", 14)
DEFAULT_FONT.setBold(True)


class Canvas(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()
            self.menu = QLabel()
            self.gameEnd = QLabel()
            self.scoreboard = Scoreboard()
            self.world = World()   

            menu_palette = QPalette()
            menu_palette.setColor(QPalette.WindowText, TEXT_COLOR)
            self.setFont(DEFAULT_FONT)
            self.menu.setAlignment(Qt.AlignCenter)
            self.menu.setText("PRESSIONE ENTER PARA INICIAR \n USE AS SETAS DIRECIONAIS PARA SE MOVER")
            self.menu.setPalette(menu_palette)
             
            board = QStackedWidget()
            board.setFixedSize(600, 450)
            board.addWidget(self.menu)
            board.addWidget(self.world)


            board_palette = QPalette()
            board_palette.setColor(QPalette.Window, GAME_COLOR)
            board.setAutoFillBackground(True)
            board.setPalette(board_palette)

            hbox = QVBoxLayout()
            hbox.setSpacing(0)
            hbox.setContentsMargins(0,0,0,0)
            hbox.addWidget(board)
            hbox.addWidget(self.scoreboard)
            self.setLayout(hbox)
            self.setFocusPolicy(Qt.StrongFocus)


        def keyPressEvent(self, event):
            if event.key() == QtCore.Qt.Key_Space:
                self.menu.setVisible(False)
                self.world.reset()
                self.world.setFocus()
                self.world.setVisible(True) 