import turtle
t=turtle.Turtle()

def move_forwards():
    t.forward(10)
def move_backwards():
    t.backward(10)
def move_clockwise():
    t.setheading(t.heading()-10)
def move_counter_clockwise():
    t.setheading(t.heading()+10)
def clear_drawing():
    t.clear()
    t.penup()
    t.goto(0,0)
    t.pendown()

s=turtle.Screen()
s.listen()
s.onkey(key="space",fun=move_forwards)
s.onkey(key="w",fun=move_forwards)
s.onkey(key="s",fun=move_backwards)
s.onkey(key="d",fun=move_clockwise)
s.onkey(key="a",fun=move_counter_clockwise)
s.onkey(key="c",fun=clear_drawing)
s.onkey(key="p",fun=t.penup)
s.onkey(key="i",fun=t.pendown)

s.exitonclick()