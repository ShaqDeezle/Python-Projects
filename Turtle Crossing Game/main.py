import turtle
import time
from car_manager import CarManager
from scoreboard_points import ScoreBoard
from turtle_player import Player

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("white")
screen.tracer(0)

continue_game = True
level = 1
score = ScoreBoard(level)
car = CarManager()
player = Player()

while (continue_game):
  time.sleep(.1)
  screen.update()
  car.create_car()
  car.move_cars(level)
  screen.listen()
  screen.onkey(player.f, "Up")

  for i in car.all_cars:
    if (player.distance(i) < 22):
      continue_game = False
      score.game_over()

  if (player.ycor() > 300):
    print("You've reached the finish line")
    player.go_to_start()

    level += 1
    score.new_level(level)

screen.exitonclick()
