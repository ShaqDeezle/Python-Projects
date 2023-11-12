from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self, player_number: int, position: tuple):
    super().__init__()
    self.player = player_number
    self.position = position
    self.points = 0
    self.hideturtle()
    self.penup()
    self.color("white")
    self.create_scoreboard()
    
    
  def create_scoreboard(self):
    self.goto(self.position)
    self.write(f"Player {self.player} ScoreBoard: {self.points}", 
               font=("Verdana", 15, "normal"))


  def add_points(self, points: int):
    self.clear()
    self.points += points
    self.create_scoreboard()
