from turtle import Turtle,Screen
import turtle
import random
turtle.colormode(255)
t=Turtle()
turtle.pensize(0)
turtle.speed("fastest")
n=float(input("enter the angle between circles: "))
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return tuple((r,g,b))

for j in range(int(360/n)):
    turtle.color(random_color())
    turtle.circle(100,extent=360,steps=None)
    turtle.left(n)

screen=Screen()
screen.exitonclick()