from turtle import Turtle


class Ball(Turtle):

  def __init__(self, position: tuple):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(stretch_wid=1, stretch_len=1)
    self.color("purple")
    self.position = position
    self.goto(self.position)
    self.x_movement = 10
    self.y_movement = 10

  def move_ball(self):
    self.x = (self.xcor() + self.x_movement)
    self.y = (self.ycor() + self.y_movement)
    self.goto(self.x, self.y)     

  def bounce_of_wall(self):
    self.y_movement *= -1

  def bounce_of_paddle(self):
    self.x_movement *= -1

  def reset_ball(self):
    self.goto((0, 0))
    self.x_movement *= -1
    self.y_movement *= -1
      
