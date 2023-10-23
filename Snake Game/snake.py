# snake.py

from turtle import Turtle

# static variable needs all CAPS at the top of a module
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

  def __init__(self):

    POSITIONS
    self.snake_pieces = []

    for position in POSITIONS:
      self.add_to_tail(position)

    self.snake_head = self.snake_pieces[0]
    self.snake_tail = self.snake_pieces[(len(self.snake_pieces) - 1)]

  def move(self):
    for i in range(len(self.snake_pieces) - 1, 0, -1):
      new_x = self.snake_pieces[i - 1].xcor()
      new_y = self.snake_pieces[i - 1].ycor()
      self.snake_pieces[i].goto(new_x, new_y)

    self.snake_head.forward(MOVE_DISTANCE)

  def add_to_tail(self, position):
    key = Turtle(shape="square")
    key.penup()
    key.goto(position)
    key.color("white")
    self.snake_pieces.append(key)

  def extend_tail(self):
    self.add_to_tail(self.snake_pieces[-1].position())

  def up(self):
    if (self.snake_head.heading() != DOWN):
      self.snake_head.setheading(UP)

  def down(self):
    if (self.snake_head.heading() != UP):
      self.snake_head.setheading(DOWN)

  def left(self):
    if (self.snake_head.heading() != RIGHT):
      self.snake_head.setheading(LEFT)

  def right(self):
    if (self.snake_head.heading() != LEFT):
      self.snake_head.setheading(RIGHT)
