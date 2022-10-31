from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout, QLabel, QStackedWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from World import World
from Scoreboard import Scoreboard
from constants import *


class Listener:
    def on_game_won(self) -> None:
        pass

    def on_game_lost(self) -> None:
        pass

    def on_score_increase(self) -> None:
        pass


class Canvas(QtWidgets.QWidget, Listener):

    def __init__(self):
        super().__init__()
        self.menu = QLabel()
        self.gameEnd = QLabel()
        self.scoreboard = Scoreboard()
        self.world = World()

        self.world.add_listener(self)

        text_palette = QPalette()
        text_palette.setColor(QPalette.WindowText, TEXT_COLOR)

        self.menu.setAlignment(Qt.AlignCenter)
        self.menu.setText("PRESSIONE ENTER PARA INICIAR \n\n\n USE AS SETAS DIRECIONAIS PARA SE MOVER")
        self.menu.setPalette(text_palette)

        self.gameEnd.setPalette(text_palette)
        self.gameEnd.setAlignment(Qt.AlignCenter)

        board = QStackedWidget()
        board.setFixedSize(WORLD_WIDTH, WORLD_HEIGHT)
        board.addWidget(self.menu)
        board.addWidget(self.world)
        board_palette = QPalette()
        board_palette.setColor(QPalette.Window, GAME_COLOR)
        board.setAutoFillBackground(True)
        board.setPalette(board_palette)

        hbox = QVBoxLayout()
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(board)
        hbox.addWidget(self.scoreboard)

        world_layout = QGridLayout()
        world_layout.addWidget(self.gameEnd)
        self.world.setLayout(world_layout)
        self.setFont(DEFAULT_FONT)
        self.setLayout(hbox)
        self.setFocusPolicy(Qt.StrongFocus)

    def on_game_lost(self) -> None:
        self.gameEnd.setText("PERDEU\n\nPRESSIONE ENTER PARA VOLTAR AO MENU")
        self.setFocus()
        self.gameEnd.setVisible(True)

    def on_game_won(self) -> None:
        self.gameEnd.setText("VENCEU\n\nPRESSIONE ENTER PARA VOLTAR AO MENU")
        self.setFocus()
        self.gameEnd.setVisible(True)

    def on_score_increase(self) -> None:
        self.scoreboard.increase_score()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return and self.menu.isVisible():
            self.world.reset()
            self.menu.setVisible(False)
            self.world.setFocus()
            self.world.setVisible(True)
        elif event.key() == QtCore.Qt.Key_Return and self.gameEnd.isVisible():
            self.scoreboard.reset()
            self.gameEnd.setVisible(False)
            self.world.setVisible(False)
            self.menu.setVisible(True)
