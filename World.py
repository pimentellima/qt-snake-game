from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from Point import Point

FRUIT_COLOR = QtGui.QColor(253, 152, 67, 255)
SNAKE_COLOR = QtGui.QColor(103, 133, 88, 255)
REFRESH_RATE = 0.1
WORLD_HEIGHT = 450
WORLD_WIDTH = 600
POINT_HEIGHT = 30
POINT_WIDTH = 30


class World(QtWidgets.QWidget):
    def __init__(self, params):
        super().__init__(params)
        self.timer = threading.Timer(REFRESH_RATE, self.update)
        self.is_running = False
        self.snake = None
        self.food = None
        self.trail = None
        self.left_direction = False
        self.right_direction = True
        self.up_direction = False
        self.down_direction = False

    def update(self):
        self.move_forward()
        self.check_food_consumed()
        self.check_collision()
        self.check_maximum_size()
        self.repaint()

    def move_forward(self):
        self.trail = self.snake[len(self.snake) - 1]
        head = self.snake[0]
        next_px = head.getPx()
        next_py = head.getPy()

        if self.right_direction:
            head.setLocation(head.getPx() + POINT_WIDTH, head.getPy())
        elif self.left_direction:
            head.setLocation(head.getPx() - POINT_WIDTH, head.getPy())
        elif self.up_direction:
            head.setLocation(head.getPx(), head.getPy() - POINT_HEIGHT)
        elif self.down_direction:
            head.setLocation(head.getPx(), head.getPy() + POINT_HEIGHT)

        for i in range(1, len(self.snake)):
            point = self.snake[i]
            aux_px = point.getPx()
            aux_py = point.getPy()
            point.setLocation(next_px, next_py)
            next_px = aux_px
            next_py = aux_py

    def check_food_consumed(self):
        head = self.snake.get[0]
        if head.getPx() == self.food.getPx() and head.getPy() == self.food.getPy():
            self.grow()
            self.score_increase()
            self.new_fruit_location()

    def check_collision(self):
        head = self.snake[0]
        if (head.getPx() == WORLD_WIDTH or head.getPx() < 0 or
                head.getPy() == WORLD_HEIGHT or head.getPy() < 0):
            self.timer.stop()
            self.game_over()
            return
        for i in range(1, len(self.snake)):
            point = self.snake[i]
            if point.getPx() == head.getPx() and point.getPy() == head.getPy():
                self.timer.cancel()
                self.game_over()
                return

    def check_maximum_size(self):
        if len(self.snake) == (WORLD_HEIGHT / POINT_WIDTH) * (WORLD_HEIGHT / POINT_HEIGHT):
            self.timer.cancel()
            self.game_won()

    def grow(self):
        self.snake.append(Point(self.trail.getPx(), self.trail.getPy()))

