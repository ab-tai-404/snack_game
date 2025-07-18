from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() >280  or  snake.head.xcor() < -280 or  snake.head.ycor() >280  or  snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.snack_reset()

    for segment in snake.segments[1:] :
        if snake.head.distance(segment) < 10 :
            scoreboard.reset()
            snake.snack_reset()

print(scoreboard.high_score)
screen.exitonclick()


