from food import Food
from turtle import Turtle
from snake import Snake


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\Users\Kanoszi\Desktop\Python_Projects\score.txt", 'r') as file:
            self.highest_score = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(x=0, y=270)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}  Highest Score: {self.highest_score}', move=False, align='center', font=('Arial', 16, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("C:\Users\Kanoszi\Desktop\Python_Projects\score.txt", 'w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()
    

