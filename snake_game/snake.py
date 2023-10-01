import turtle
from turtle import Screen,Turtle
import time
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        # new_segment.shape("turtle")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        # segments[0].left(90)

    def up(self):
        for seg in self.segments:
            if seg==self.segments[0]:
                if seg.heading()!=270.0:
                    seg.setheading(90)

    def down(self):
        for seg in self.segments:
            if seg==self.segments[0]:
                if seg.heading()!=90:
                    seg.setheading(270)

    def left(self):
        for seg in self.segments:
            if seg==self.segments[0]:
                if seg.heading()!=0:
                    seg.setheading(180)

    def right(self):
        for seg in self.segments:
            if seg==self.segments[0]:
                if seg.heading()!=180:
                    seg.setheading(0)


