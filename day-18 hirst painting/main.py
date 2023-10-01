# import colorgram
# l=colorgram.extract("hirst painting.jpg",30)
# colors=[]
# for i in l:
#     r=i.rgb.r
#     g=i.rgb.g
#     b=i.rgb.b
#     colors.append(tuple((r,g,b)))
#
# print(colors)
# after getting a list in your output by running the above code copy and paste the list here and assign it to colors list
import random

colors=[(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8),  (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214),  (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

import turtle

turtle.colormode(255)
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
height=turtle.window_height()
turtle.goto(0,height/2)

for i in range(10):
    for j in range(10):
        turtle.dot(20,random.choice(colors))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)
    turtle.left(90)
    turtle.backward(50*10)
    turtle.pendown()

screen=turtle.Screen()
screen.exitonclick()