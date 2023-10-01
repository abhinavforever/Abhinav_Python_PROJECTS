from turtle import Turtle,Screen
import random
import turtle
t=Turtle()
screen=Screen()
t.shape("turtle")
t.color("red")
t.speed("fastest")
directions=[0,90,180,270]
t.pensize(10)
turtle.colormode(255)
r=0
g=0
b=0
for i in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color((r, g, b))
    t.forward(20)
    t.setheading(random.choice(directions))

screen.exitonclick()