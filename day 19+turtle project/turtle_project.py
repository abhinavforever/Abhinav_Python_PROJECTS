import turtle
import random

turtle.speed("fastest")
turtle.colormode(255)
s=turtle.Screen()
# s.setup(width=500,height=500)
user_bet = s.textinput(title="enter your bet",prompt="which turtle will win the race:")
colors=["red","orange","yellow","green","blue","purple"]
s.screensize(canvwidth=500,canvheight=500)
y=-125
x=-230
turtles=[]
race_is_on=False
for i in range(6):
    t=turtle.Turtle(shape="turtle")
    turtles.append(t)
    new_color=colors[i]
    t.color(new_color)
    t.penup()
    t.goto(x,y)
    y=y+50

if user_bet:
    race_is_on=True
while race_is_on:
    for turtle in turtles:
        if not(turtle.pos()[0]>=230):
            rand_dist=random.randint(0,10)
            turtle.forward(rand_dist)
        else:
            winner=turtle.color()[0]
            if winner==user_bet:
                print("user has won",winner,"wins")
            else:
                print("user has lost",winner,"wins")

            race_is_on=False
            break

s.exitonclick()

