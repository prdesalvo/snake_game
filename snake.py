from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0) #turns off animations

STARTING_POSITIONS = [(0,0),(0,0),(-20,0)]
MOVE_DISTANCE = 20

class Snake:
  def __init__(self):
    self.segments = []
    self.segments_reversed = []
    self.create_snake()
    self.move()


  def create_snake(self):
    for position in STARTING_POSITIONS:
      new_segment = Turtle(shape='square')
      new_segment.penup()
      new_segment.color('white')
      new_segment.goto(position) 
      new_segment.speed("slow")
      self.segments.append(new_segment)
      print(new_segment.pos())

  def move(self):
    self.segments_reversed = self.segments[::-1]

    #Move the tail pieces to the position of the piece in front of them
    for index, elem in enumerate(self.segments_reversed):
      
      try:
        new_pos = self.segments_reversed[index+1].pos()
        elem.goto(new_pos)
      except: #ignore the head
        pass

    #move the head
    self.segments[0].fd(MOVE_DISTANCE)

  def up(self):
    self.segments[0].setheading(90)
  

  def down(self):
    self.segments[0].setheading(270)
  

  def left(self):
    self.segments[0].setheading(180)

  def right(self):
    self.segments[0].setheading(0)