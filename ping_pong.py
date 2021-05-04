import turtle

# setup the screen
screen = turtle.Screen()
screen.bgcolor('#000000')
screen.screensize(800, 600)
screen.tracer(0)
screen.title("Ping pong")   

#player scores
score_a = 0
score_b = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.goto(-350, 0)
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.shapesize(5,1)
paddle_a.speed(0)
paddle_a.penup()

#paddle b
paddle_b = turtle.Turtle()
paddle_b.goto(350, 0)
paddle_b.color('white')
paddle_b.shape('square')
paddle_b.shapesize(5,1)
paddle_b.speed(0)
paddle_b.penup()

#ball
ball = turtle.Turtle()
ball.color('white')
ball.shape('square')
ball.speed(0)
ball.penup()
ball.dx = 0.2
ball.dy = 0.2

#pen
pen = turtle.Turtle()
pen.hideturtle()
pen.color('white')
pen.penup()
pen.speed(0)
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align='center', font=('Courier', 18, 'normal'))

#on key press functions
def move_up_a():
    y = paddle_a.ycor()
    if y+50 > 290:
        return
    y += 20
    paddle_a.sety(y)

def move_down_a():
    y = paddle_a.ycor()
    if y-50 < -290:
        return
    y -= 20
    paddle_a.sety(y)

def move_up_b():
    y = paddle_b.ycor()
    if y+50 > 290:
        return
    y += 20
    paddle_b.sety(y)

def move_down_b():
    y = paddle_b.ycor()
    if y-50 < -290:
        return
    y -= 20
    paddle_b.sety(y)

#event listening
screen.listen()
screen.onkeypress(move_up_a, 'w')
screen.onkeypress(move_down_a,'s')
screen.onkeypress(move_up_b, 'Up')
screen.onkeypress(move_down_b,'Down')

while True:
    screen.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align='center', font=('Courier', 18, 'normal'))

    if ball.xcor()<-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align='center', font=('Courier', 18, 'normal'))

    #paddle and ball collision
    if (ball.xcor()+10>340 and ball.xcor()+10<360) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor()-10<-340 and ball.xcor()-10>-360) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-330)
        ball.dx *= -1
