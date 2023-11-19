from turtle import Turtle

FONT = ("Verdana", 15, "normal")


class ScoreBoard(Turtle):

  def __init__(self, level):
    super().__init__()
    self.penup()
    self.hideturtle()
    self.goto((-280, 260))
    self.write(f"Level {level}", font=FONT)

  def new_level(self, level):
    self.clear()
    self.goto((-280, 260))
    self.write(f"Level {level}", font=FONT)
    # return level

  def game_over(self):
    self.goto((-50, 0))
    self.write("Game Over", font=FONT)
