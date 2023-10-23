# scoreboard.py

from turtle import Turtle
FONT = ("Verdana", 15, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
  def __init__(self):
    self.num_of_wins = 0
    super().__init__()
    self.goto(0, 260)
    self.color("white")
    self.hideturtle()
    self.update_score()
    
  def increase_points(self):
    self.num_of_wins += 1
    self.clear()
    self.update_score()

  def update_score(self):
    self.write(f"Scoreboard = {self.num_of_wins}", 
       font = FONT, align = ALIGNMENT)
    
  def game_over(self):
    self.goto(0, 0)
    self.write("You Lost. Game Over.", 
       font = FONT, align = ALIGNMENT)
    
