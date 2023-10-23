from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while (game_is_on):
  screen.update()
  time.sleep(.1)
  snake.move()

  # Detect Collision of Food

  if (snake.snake_head.distance(food) < 15):
    food.move_food()
    scoreboard.increase_points()
    snake.extend_tail()

  # Detect Collision with Wall
  
  if (snake.snake_head.xcor() > 280) or (snake.snake_head.ycor() > 280) or (snake.snake_head.xcor() < -280) or (snake.snake_head.ycor() < -280):
    scoreboard.game_over()
    game_is_on = False

  # Detect Collision with Any Part of the Snake

  for i in snake.snake_pieces[1::]:
    if (snake.snake_head.distance(i) < 15):
      scoreboard.game_over()
      game_is_on = False


screen.exitonclick()
