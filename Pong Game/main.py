from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
game_is_on = True

paddle_1 = Paddle((325, 0))
paddle_2 = Paddle((-325, 0))
scoreboard_1 = Scoreboard(1, (-380, 200))
scoreboard_2 = Scoreboard(2, (140, 200))
ball = Ball((0, 0))
x = .1


while (game_is_on):
  time.sleep(x)
  screen.update()
  ball.move_ball()
  screen.listen()
  screen.onkey(paddle_1.up, "Up")
  screen.onkey(paddle_1.down, "Down")
  screen.onkey(paddle_2.up, "w")
  screen.onkey(paddle_2.down, "s")

  if (ball.ycor() < -300) or (ball.ycor() > 300):
    ball.bounce_of_wall()

  a_distance = ball.xcor() - paddle_1.xcor()
  b_distance = ball.ycor() - paddle_1.ycor()
  c_distance = ball.xcor() - paddle_2.xcor()
  d_distance = ball.ycor() - paddle_2.ycor()

  net_a_distance = abs(a_distance)
  net_b_distance = abs(b_distance)
  net_c_distance = abs(c_distance)
  net_d_distance = abs(d_distance)

  # ball is close enough to be hit on both x and y coordinates.
  if (net_a_distance <= 20 and net_b_distance <= 80):
    # ball has not gone past the paddle.
    if a_distance >= -17:
      ball.bounce_of_paddle()
      x *= .9

  if (net_c_distance <= 20 and net_d_distance <= 80):
    # ball has not gone past the paddle.
    if c_distance >= 0:
      ball.bounce_of_paddle()
      x *= .9

  if (ball.xcor() > 410):
    scoreboard_1.add_points(1)
    ball.reset_ball()
    x = .1

  if (ball.xcor() < -410):
    scoreboard_2.add_points(1)
    ball.reset_ball()
    x = .1    

screen.exitonclick()
