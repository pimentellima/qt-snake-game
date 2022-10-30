from random import randint
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from Point import Point

FRUIT_COLOR = QtGui.QColor(253, 152, 67)
SNAKE_COLOR = QtGui.QColor(103, 133, 88)
REFRESH_RATE = 500
WORLD_HEIGHT = 450
WORLD_WIDTH = 600
POINT_HEIGHT = 30
POINT_WIDTH = 30

class World(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.is_running = False
        self.snake = []
        self.food = Point(0,0)
        self.setFocusPolicy(Qt.StrongFocus)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateWorld)

    def reset(self):
        self.snake.clear
        self.snake.append(Point(60,120))
        self.snake.append(Point(30,120))
        self.snake.append(Point(0,120))
        self.trail = self.snake[len(self.snake) - 1]
        self.left_direction = False
        self.right_direction = True
        self.up_direction = False
        self.down_direction = False
        self.new_food_location()
        self.timer.start(100)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up and (self.left_direction or self.right_direction):
            self.up_direction = True
            self.left_direction = False 
            self.right_direction = False 
        if event.key() == QtCore.Qt.Key_Down and (self.left_direction or self.right_direction):
            self.down_direction = True 
            self.left_direction = False 
            self.right_direction = False 
        if event.key() == QtCore.Qt.Key_Left and (self.up_direction or self.down_direction):
            self.left_direction = True 
            self.up_direction = False
            self.down_direction = False
        if event.key() == QtCore.Qt.Key_Right and (self.up_direction or self.down_direction):
            self.right_direction = True
            self.up_direction = False
            self.down_direction = False

    def updateWorld(self):
        self.move_forward()
        self.check_collision()
        self.check_maximum_size()
        self.check_food_consumed()
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
        head = self.snake[0]
        if head.getPx() == self.food.getPx() and head.getPy() == self.food.getPy():
            self.grow()
            self.new_food_location()

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

    def new_food_location(self):
        valid = False
        while not valid:
            px = random.randint(0, WORLD_WIDTH / POINT_WIDTH - 2)  * POINT_WIDTH
            py = random.randint(0, WORLD_HEIGHT / POINT_HEIGHT - 2) * POINT_HEIGHT
            for point in self.snake:
                if px == point.getPx() and py == point.getPy():
                    valid = False 
                    break 
            valid = True
        self.food.setLocation(px,py)           

    def grow(self):
        self.snake.append(Point(self.trail.getPx(), self.trail.getPy()))

    def game_won(self):
        print("game won")

    def game_over(self):
        self.timer.stop()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)

        qp.setPen(FRUIT_COLOR)
        qp.setBrush(FRUIT_COLOR)        
        self.food.draw(qp)

        qp.setPen(SNAKE_COLOR)
        qp.setBrush(QtGui.QBrush(SNAKE_COLOR))
        for point in self.snake:
            point.draw(qp)