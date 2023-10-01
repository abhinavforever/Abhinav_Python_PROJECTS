from turtle import Turtle,Screen
import turtle
import random
turtle.colormode(255)
t=Turtle()
t.shape("turtle")
turtle.pensize(3)
turtle.speed(0)
n=30
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return tuple((r,g,b))

for i in range (5):
    for j in range(12):
        turtle.color(random_color())
        turtle.circle(100,extent=360,steps=None)
        turtle.left(n)
    n=n+1



screen=Screen()
screen.exitonclick()