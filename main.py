from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from frame import Frame
from pygame import mixer

mixer.init()
mixer.music.load('C:\Users\Kanoszi\Desktop\Python_Projects\sound.mp3')
mixer.music.set_volume(0.2)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake by Jareczek')
screen.tracer(0)

frame = Frame()
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(snake.up, 'W')
screen.onkeypress(snake.down, 'S')
screen.onkeypress(snake.left, 'A')
screen.onkeypress(snake.right, 'D')

screen.update()

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        mixer.music.play()
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()
    
    #detect collision with wall
    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:    
            scoreboard.reset()
            snake.reset()

    

        

screen.exitonclick()