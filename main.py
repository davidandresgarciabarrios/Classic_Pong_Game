from turtle import Screen
from paddle import Paddle
from ball import Ball
from board import Board
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
board = Board()

# Flags to check if keys are pressed
r_paddle_up = False
r_paddle_down = False
l_paddle_up = False
l_paddle_down = False

def move_r_paddle():
    if r_paddle_up:
        r_paddle.go_up()
    if r_paddle_down:
        r_paddle.go_down()
    screen.ontimer(move_r_paddle, 20)

def move_l_paddle():
    if l_paddle_up:
        l_paddle.go_up()
    if l_paddle_down:
        l_paddle.go_down()
    screen.ontimer(move_l_paddle, 20)

# Key press and release functions for right paddle
def r_paddle_up_press():
    global r_paddle_up
    r_paddle_up = True

def r_paddle_up_release():
    global r_paddle_up
    r_paddle_up = False

def r_paddle_down_press():
    global r_paddle_down
    r_paddle_down = True

def r_paddle_down_release():
    global r_paddle_down
    r_paddle_down = False

# Key press and release functions for left paddle
def l_paddle_up_press():
    global l_paddle_up
    l_paddle_up = True

def l_paddle_up_release():
    global l_paddle_up
    l_paddle_up = False

def l_paddle_down_press():
    global l_paddle_down
    l_paddle_down = True

def l_paddle_down_release():
    global l_paddle_down
    l_paddle_down = False

# Listen to key press and release events
screen.listen()
screen.onkeypress(r_paddle_up_press, "Up")
screen.onkeyrelease(r_paddle_up_release, "Up")
screen.onkeypress(r_paddle_down_press, "Down")
screen.onkeyrelease(r_paddle_down_release, "Down")

screen.onkeypress(l_paddle_up_press, "w")
screen.onkeyrelease(l_paddle_up_release, "w")
screen.onkeypress(l_paddle_down_press, "s")
screen.onkeyrelease(l_paddle_down_release, "s")

# Initialize the movement
move_r_paddle()
move_l_paddle()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with walls:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle "misses":
    if ball.xcor() > 380:
        ball.reset_position()
        board.l_point()

    # Detect left paddle "misses":
    if ball.xcor() < -380:
        ball.reset_position()
        board.r_point()

screen.exitonclick()