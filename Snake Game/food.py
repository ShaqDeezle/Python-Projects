from turtle import Turtle
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("blue")
    self.shapesize(stretch_len = .5, stretch_wid = .5)
    self.speed("fastest")
    self.move_food()

  def move_food(self):
    self.random_x = random.randint(-280, 280)
    self.random_y = random.randint(-280, 280)
    super().goto(self.random_x, self.random_y)
