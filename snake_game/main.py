from turtle import Screen,Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# delay=float(input("choose speed from 0.1 to 0.5 as screen delay(note: speed decreases from 0.1 to 0.5): "))

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    # time.sleep(1/(scoreboard.score+2)) #delay for 0.1 seconds and then refresh the screen
    time.sleep(0.1)
    snake.move()

    #DETECT collision with food.
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall.
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

    #if head collides with any segment in the tail:
    #trigger game_over
screen.exitonclick()
