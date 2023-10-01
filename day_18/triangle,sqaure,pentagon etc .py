from turtle import Turtle,Screen
t=Turtle()
# t.shape("turtle")
t.color("red")

for i in range(3):
    t.forward(50)
    t.right(120)
for i in range(4):
    t.color("green")
    t.forward(50)
    t.right(90)
for i in range(5):
    t.color("blue")
    t.forward(50)
    t.right(72)
for i in range(6):
    t.color("pink")
    t.forward(50)
    t.right(60)
for i in range(7):
    t.color("black")
    t.forward(50)
    t.right(180-((7-2)*180/7))
for i in range(8):
    t.color("orange")
    t.forward(50)
    t.right(180-((8-2)*180/8))
for i in range(9):
    t.color("#FFD700")
    t.forward(50)
    t.right(40)
for i in range(10):
    t.color("pink")
    t.forward(50)
    t.right(36)
screen=Screen()
screen.exitonclick()