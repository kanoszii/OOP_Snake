from turtle import Turtle

class Frame(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.goto(-270, -270)
        self.pendown()
        self.goto(-270, 270)
        self.goto(270, 270)
        self.goto(270, -270)
        self.goto(-270, -270)