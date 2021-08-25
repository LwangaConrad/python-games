import turtle
# import winsound
# import os for linux and MAC

#creating a window
win = turtle.Screen()
win.title("pong by Lwanga")
win.bgcolor("green")
win.setup(width=800, height=600)
#speeds up running by allowing manual update of window
win.tracer()

#scores
player_1_score = 0
player_2_score = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.color("yellow")
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: {}  Player 2: {}".format(player_1_score, player_2_score), align="center", font=("Courier", 24, "bold"))

def paddle_a_up():
    if paddle_a.ycor() < 240:
         y = paddle_a.ycor()
         y += 20
         paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() > -240:
        v = paddle_a.ycor() - 20
        paddle_a.sety(v)

def paddle_b_up():
    if paddle_b.ycor() < 240:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > -240:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

#keyboard binding
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

#main game loop
while True:
    win.update()

    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #ball border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #winsound.PlaySound("boing.wav", winsound.SND_ASYNC)
        #os.system("aplay boing.wav&") for linux
        #os.system("afplay boing.wav&") for MAC

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_1_score += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_1_score, player_2_score), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_2_score += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(player_1_score, player_2_score), align="center", font=("Courier", 24, "bold"))

    #bouncing off paddles
    if paddle_b.ycor()+60 >= ball.ycor() >= paddle_b.ycor()-60 and ball.xcor()+20 == paddle_b.xcor():
        ball.dx *= -1
    if paddle_a.ycor()+60 >= ball.ycor() >= paddle_a.ycor()-60 and ball.xcor()-20 == paddle_a.xcor():
        ball.dx *= -1