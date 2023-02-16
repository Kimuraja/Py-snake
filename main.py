from turtle import Screen, Turtle
from snake import Snake
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('#ffffff')
s.title("Snake")
s.tracer(0)

snake = Snake()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


is_on = True
while is_on:
    s.update()
    time.sleep(0.05)
    snake.move()


s.exitonclick()
