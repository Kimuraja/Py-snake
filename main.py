from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('#ffffff')
s.title("Snake")
s.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")


is_on = True
while is_on:
    s.update()
    time.sleep(0.07)
    snake.move()
    score.update_scoreboard()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        score.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()
s.exitonclick()
