from turtle import Turtle

MOVEMENT = 20


class Paddle(Turtle):

  def __init__(self, position: tuple):
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.color("white")
    self.position = position
    self.goto(self.position)

  def up(self):
    self.y = (self.ycor() + MOVEMENT)

    if self.y > 250:
      self.y = 250

    self.goto(self.xcor(), self.y)

  def down(self):
    self.y = (self.ycor() - MOVEMENT)

    if self.y < -250:
      self.y = -250

    self.goto(self.xcor(), self.y)
