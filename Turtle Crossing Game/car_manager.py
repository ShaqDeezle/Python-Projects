from turtle import Turtle
# from scoreboard_points import ScoreBoard
import random as r

COLORS = ["red", "black", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

  def __init__(self):
    self.all_cars = []

  def move_cars(self, level):

    self.my_dict = {
      1: STARTING_MOVE_DISTANCE,
      2: STARTING_MOVE_DISTANCE + MOVE_INCREMENT,
      3: 2 * (STARTING_MOVE_DISTANCE + MOVE_INCREMENT),
      4: 3 * (STARTING_MOVE_DISTANCE + MOVE_INCREMENT),
      5: 4 * (STARTING_MOVE_DISTANCE + MOVE_INCREMENT),
      6: 5 * (STARTING_MOVE_DISTANCE + MOVE_INCREMENT)
    }

    if (level > 6):
      level = 6

    for i in self.all_cars:
      self.x_axis = i.xcor() - self.my_dict[level]
      i.goto(self.x_axis, i.ycor())
      # i.backward(self.my_dict[level])

  def create_car(self):
    self.num = r.randint(1, 6)
    if (self.num == 1):
      self.new_car = Turtle(shape="square")
      self.new_car.penup()
      self.new_car.shapesize(stretch_wid=1, stretch_len=2)

      self.y_axis = r.randint(-250, 250)

      self.new_car.goto(310, self.y_axis)

      self.color_picked = r.choice(COLORS)

      self.new_car.color(self.color_picked)
      self.all_cars.append(self.new_car)
