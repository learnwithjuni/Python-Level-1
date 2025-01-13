# Try this project in the Juniverse! https://app.junilearning.com/juniverse/projects/65e2318a8a9896d5deae7712

import turtle
import random

# create screen object 
screen = turtle.Screen()
# disable screen updates 
screen.tracer(0)

# draw the boundary box
boxDrawer = turtle.Turtle()
boxDrawer.speed(10)
boxDrawer.penup()
boxDrawer.goto(-200, 200)
boxDrawer.pendown()
for i in range(4):
  boxDrawer.forward(400)
  boxDrawer.right(90)
boxDrawer.ht()

balls = []
for i in range(10):
  t = turtle.Turtle()
  t.penup()
  t.speed(1000)
  t.color("red")
  t.shape("circle")
  t.goto(random.randint(-200,200), random.randint(-200,200))
  t.right(random.randint(0,360))
  balls.append(t)

# add a player
player = turtle.Turtle()
player.shape("turtle")
player.penup()

# start with 10 lives
lives = 10
# display lives 
livesWriter = turtle.Turtle()
livesWriter.penup()
livesWriter.goto(-200,210)
livesWriter.write("Lives: " + str(lives))

def checkCollision(ball):
  if ball.xcor() > 200 or ball.xcor() < -200:
    ball.right(180)
  elif ball.ycor() > 200 or ball.ycor() < -200:
    ball.right(180)

# motion commands for player
def left():
  player.left(10)

def right():
  player.right(10)

screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

while lives > 0:
  player.forward(10)
  checkCollision(player)
  for ball in balls:
    checkCollision(ball)
    # check for collision between player and ball 
    if abs(ball.xcor() - player.xcor()) < 10 and abs(ball.ycor() - player.ycor()) < 10:
      lives -= 1
      livesWriter.clear()
      livesWriter.write("Lives: " + str(lives))
      player.goto(random.randint(-200,200), random.randint(-200,200))
    ball.forward(10)
    screen.update()

# after the player loses all lives, display game over
livesWriter.goto(0,0)
livesWriter.write("GAME OVER!")
screen.update()

# for repl.it projects only: keep the window open
turtle.mainloop()
