import turtle, random, time, winsound
from sys import exit

game = turtle.Screen()
game.title("Pong Game")
game.mode('standard')
game.bgcolor("black")
game.setup(width=800,height=600)
game.tracer(0)

paddle_velo = 10
ball_velo = 2
paddle_offset = 50
paddle_color = '#0802A3'

# Score
score_a = 0
score_b = 0

# Funtions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += paddle_velo
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= paddle_velo
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += paddle_velo
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= paddle_velo
        paddle_b.sety(y)

def random_ball_velo():
    return random.choice([ball_velo, -ball_velo])

def update_score():
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}",align="center",font=("Consolas",16,"normal"))

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color(paddle_color)
paddle_a.penup()
paddle_a.goto(-370, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color(paddle_color)
paddle_b.penup()
paddle_b.goto(370, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('#FF4B91')
ball.penup()
ball.goto(0, 0)
ball.dx = random_ball_velo()
ball.dy = random_ball_velo()

# Keyboard Bindings
game.listen()
game.onkeypress(paddle_a_up, "w")
game.onkeypress(paddle_a_down, "s")
game.onkeypress(paddle_b_up, "Up")
game.onkeypress(paddle_b_down, "Down")

# Scoring
pen=turtle.Turtle()
pen.speed(0)
pen.color("#FFCD4B")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
update_score()

running = True
while running:
    game.update()

    time.sleep(1/60)

    try:
        # move the ball
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)
    except:
        exit()

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = -ball.dy
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy = -ball.dy
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.dx = random_ball_velo()
        score_a += 1
        update_score()

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx = random_ball_velo()
        score_b += 1
        update_score()

    # Check paddle and ball collisions
    if (ball.xcor() > 350 and ball.xcor() < 370) and (ball.ycor()<paddle_b.ycor()+paddle_offset and ball.ycor()>paddle_b.ycor()-paddle_offset):
        ball.setx(350)
        ball.dx=-ball.dx
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)


    if (ball.xcor() < -350 and ball.xcor() > -370) and (ball.ycor()<paddle_a.ycor()+paddle_offset and ball.ycor()>paddle_a.ycor()-paddle_offset):
        ball.setx(-350)
        ball.dx=-ball.dx
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)