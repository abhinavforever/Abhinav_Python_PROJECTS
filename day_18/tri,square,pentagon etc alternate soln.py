from turtle import Turtle,Screen,colormode
import random
colormode(255)
t=Turtle()
# t.shape("turtle")
n=3
r=0
g=0
b=0
for i in range(8):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t.color((r,g,b))
    for j in range(n):
        t.forward(50)
        t.right(180-((n-2)*180/n))
    n=n+1
screen=Screen()
screen.exitonclick()