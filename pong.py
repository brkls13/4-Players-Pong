import turtle





wn = turtle.Screen()

wn.title("Updated Pong Game")

wn.bgcolor("black")

wn.setup(width=800, height=600)

wn.tracer(0)

score_a = 0

score_b = 0

pen = turtle.Turtle()

pen.speed(0)

pen.color("white")

pen.penup()

pen.hideturtle()

pen.goto(0, 260)

pen.write("Team 1: 0  Team 2: 0", align="center", font=("Courier", 24, "normal"))

#Paddle a



paddle_a = turtle.Turtle()

paddle_a.speed(0)

paddle_a.color("red")

paddle_a.shape("square")

paddle_a.shapesize(stretch_wid=4, stretch_len=1)

paddle_a.penup()

paddle_a.goto(-350, -200)



#paddle b



paddle_b = turtle.Turtle()

paddle_b.speed(0)

paddle_b.color("blue")

paddle_b.shape("square")

paddle_b.shapesize(stretch_wid=4, stretch_len=1)

paddle_b.penup()

paddle_b.goto(-350, 200)





#Paddle c



paddle_c = turtle.Turtle()

paddle_c.speed(0)

paddle_c.color("green")

paddle_c.shape("square")

paddle_c.shapesize(stretch_wid=4, stretch_len=1)

paddle_c.penup()

paddle_c.goto(350, -200)



#paddle d



paddle_d = turtle.Turtle()

paddle_d.speed(0)

paddle_d.color("yellow")

paddle_d.shape("square")

paddle_d.shapesize(stretch_wid=4, stretch_len=1)

paddle_d.penup()

paddle_d.goto(350, 200)





#ball



ball = turtle.Turtle()

ball.speed(0)

ball.color("white")

ball.shape("square")

ball.penup()

ball.goto(0, 0)

ball.dx = 0.2

ball.dy = 0.2



def paddle_a_up():

    y = paddle_a.ycor()

    if y < 250:

        y += 20

        paddle_a.sety(y)




def paddle_a_down():

    y = paddle_a.ycor()

    if y > -250:

        y -= 20

        paddle_a.sety(y)




def paddle_b_up():

    y = paddle_b.ycor()

    if y < 250:

        y += 20

        paddle_b.sety(y)




def paddle_b_down():

    y = paddle_b.ycor()

    if y > -250:

        y -= 20

        paddle_b.sety(y)




def paddle_c_up():
    y = paddle_c.ycor()
    if y < 250:
        y += 20
        paddle_c.sety(y)




def paddle_c_down():

    y = paddle_c.ycor()

    if y > -250:

        y -= 20

        paddle_c.sety(y)




def paddle_d_up():

    y = paddle_d.ycor()

    if y < 250:

        y += 20

        paddle_d.sety(y)




def paddle_d_down():

    y = paddle_d.ycor()

    if y > -250:

        y -= 20

        paddle_d.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "e")
wn.onkeypress(paddle_b_down, "d")
wn.onkeypress(paddle_c_up, "Up")
wn.onkeypress(paddle_c_down, "Down")
wn.onkeypress(paddle_d_up, "l")
wn.onkeypress(paddle_d_down, "k")

#game loop

while True:

    wn.update()

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:

        ball.sety(290)

        ball.dy *= -1

    if ball.ycor() < -290:

        ball.sety(-290)

        ball.dy *= -1

    if ball.xcor() > 390:

        ball.goto(0, 0)

        ball.dx *= -1

        score_a += 1

        pen.clear()

        pen.write("Team 1: {}  Team 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:

        ball.goto(0, 0)

        ball.dx *= -1

        score_b += 1

        pen.clear()

        pen.write("Team 1: {}  Team 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_c.ycor() + 50 and ball.ycor() > paddle_c.ycor() - 50) or (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_d.ycor() + 50 and ball.ycor() > paddle_d.ycor() - 50):

        ball.setx(340)

        ball.dx *= -1



    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50) or (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):

        ball.setx(-340)

        ball.dx *= -1
