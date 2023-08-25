
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('green')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.grid_size = 20
        self.square_size = 27
        self.refresh()

    def refresh(self):
        random_x = random.randint(-self.grid_size // 2 * self.square_size, (self.grid_size // 2 - 1) * self.square_size)
        random_y = random.randint(-self.grid_size // 2 * self.square_size, (self.grid_size // 2 - 1) * self.square_size)
        self.goto(random_x, random_y)





 