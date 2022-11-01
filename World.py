from random import randint
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from constants import *
from Point import Point


class World(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.snake = []
        self.trail = None
        self.food = Point(0, 0)
        self.left_direction = None
        self.right_direction = None
        self.up_direction = None
        self.down_direction = None
        self.listeners = []
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_world)
        self.setFocusPolicy(Qt.StrongFocus)

    def reset(self):
        self.snake.clear()
        self.snake.append(Point(60,120))
        self.snake.append(Point(30,120))
        self.snake.append(Point(0,120))
        self.trail = self.snake[len(self.snake) - 1]
        self.new_food_location()
        self.left_direction = False
        self.right_direction = True
        self.up_direction = False
        self.down_direction = False
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

    def update_world(self):
        self.move_forward()
        self.check_food_consumed()
        self.check_collision()
        self.check_maximum_size()
        self.repaint()

    def move_forward(self):
        self.trail = self.snake[len(self.snake) - 1]
        head = self.snake[0]
        next_px = head.get_px()
        next_py = head.get_py()

        if self.right_direction:
            head.set_location(head.get_px() + POINT_WIDTH, head.get_py())
        elif self.left_direction:
            head.set_location(head.get_px() - POINT_WIDTH, head.get_py())
        elif self.up_direction:
            head.set_location(head.get_px(), head.get_py() - POINT_HEIGHT)
        elif self.down_direction:
            head.set_location(head.get_px(), head.get_py() + POINT_HEIGHT)

        for i in range(1, len(self.snake)):
            point = self.snake[i]
            aux_px = point.get_px()
            aux_py = point.get_py()
            point.set_location(next_px, next_py)
            next_px = aux_px
            next_py = aux_py

    def check_food_consumed(self):
        head = self.snake[0]
        if head.get_px() == self.food.get_px() and head.get_py() == self.food.get_py():
            self.grow()
            self.score_increased()
            self.new_food_location()

    def check_collision(self):
        head = self.snake[0]
        if (head.get_px() == WORLD_WIDTH or head.get_px() < 0 or
                head.get_py() == WORLD_HEIGHT or head.get_py() < 0):
            self.timer.stop()
            self.game_over()
            return
        for i in range(1, len(self.snake)):
            point = self.snake[i]
            if point.get_px() == head.get_px() and point.get_py() == head.get_py():
                self.timer.stop()
                self.game_over()
                return

    def check_maximum_size(self):
        if len(self.snake) == (WORLD_HEIGHT / POINT_WIDTH) * (WORLD_HEIGHT / POINT_HEIGHT):
            self.timer.stop()
            self.game_won()

    def new_food_location(self):
        valid = False
        while not valid:
            px = randint(0, WORLD_WIDTH / POINT_WIDTH - 2)  * POINT_WIDTH
            py = randint(0, WORLD_HEIGHT / POINT_HEIGHT - 2) * POINT_HEIGHT
            for point in self.snake:
                if px == point.get_px() and py == point.get_py():
                    valid = False 
                    break 
            valid = True
        self.food.set_location(px,py)           

    def grow(self):
        self.snake.append(Point(self.trail.get_px(), self.trail.get_py()))

    def game_won(self):
        for listener in self.listeners:
            listener.on_game_won()

    def game_over(self):
        for listener in self.listeners:
            listener.on_game_lost()

    def score_increased(self):
        for listener in self.listeners:
            listener.on_score_increase()

    def add_listener(self, listener):
        self.listeners.append(listener)

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