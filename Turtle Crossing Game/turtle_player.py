from turtle import Turtle


class Player(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.color("orange")
    self.go_to_start()
    self.setheading(90)

  def f(self):
    self.forward(10)

  def go_to_start(self):
    self.goto((0, -280))
