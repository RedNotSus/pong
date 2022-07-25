# pong with turtle
import os
import turtle

wn = turtle.Screen()
wn.title("Pong by @Rednotsus")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


# paddel A
paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape("square")
paddel_a.color("white")
paddel_a.shapesize(stretch_wid=5, stretch_len=1)
paddel_a.penup()
paddel_a.goto(-350, 0)


# paddle B
paddel_b = turtle.Turtle()
paddel_b.speed(0)
paddel_b.shape("square")
paddel_b.color("white")
paddel_b.shapesize(stretch_wid=5, stretch_len=1)
paddel_b.penup()
paddel_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# Functions


def paddel_a_up():
    y = paddel_a.ycor()
    y += 20
    paddel_a.sety(y)


def paddel_a_down():
    y = paddel_a.ycor()
    y -= 20
    paddel_a.sety(y)


def paddel_b_up():
    y = paddel_b.ycor()
    y += 20
    paddel_b.sety(y)


def paddel_b_down():
    y = paddel_b.ycor()
    y -= 20
    paddel_b.sety(y)

# Keyboard binding


wn.listen()
wn.onkeypress(paddel_a_up, "w")
wn.onkeypress(paddel_a_down, "s")
wn.onkeypress(paddel_b_up, "Up")
wn.onkeypress(paddel_b_down, "Down")


# Score


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddel_a.ycor() + 50 and ball.ycor() > paddel_a.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddel_b.ycor() + 50 and ball.ycor() > paddel_b.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
