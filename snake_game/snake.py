from turtle import Turtle
start_posi = [(0, 0), (-20, 0), (-40, 0)]
dist=20

class Snake:
    def __init__(self):
        self.segments=[]
        self.createsnake()
        self.head=self.segments[0]
    def createsnake(self):
        for pos in start_posi:
            self.addseg(pos)
    def addseg(self,pos):
        newseg = Turtle("square")
        newseg.color("white")
        if pos==(0,0):
            newseg.color("blue")
        newseg.up()
        newseg.goto(pos)
        self.segments.append(newseg)
    def extend(self):
        self.addseg(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(20)
    def up(self):
        if self.head.heading()==270:
            return
        self.head.setheading(90)
    def down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)
    def left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)
    def right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def newgame(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move old segments off-screen
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]
