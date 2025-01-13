import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

# draw the boundary box
screen.tracer(0)
boxDrawer = turtle.Turtle()
boxDrawer.speed(10)
boxDrawer.color("red")
boxDrawer.penup()
boxDrawer.goto(-200, 200)
boxDrawer.pendown()
for i in range(4):
  boxDrawer.forward(400)
  boxDrawer.right(90)
boxDrawer.penup()
screen.update()

# create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()

# write score
score = 0
scoreTurtle = turtle.Turtle()
scoreTurtle.penup()
scoreTurtle.color("white")
scoreTurtle.goto(-200,210)
scoreTurtle.write("Score: 0")

# create targets
targets = []
for i in range(10):
	targets.append(turtle.Turtle())
	targets[i].color("red")
	targets[i].shape("circle")
	targets[i].penup()
	targets[i].speed(0)
	targets[i].setposition(random.randint(-190, 190), random.randint(-190, 190))
	targets[i].right(random.randint(0,360))
screen.update()

# create functions for keyboard events
def left():
	player.left(30)
	
def right():
	player.right(30)

# create function for checking for player/target collisions
def isCollision(target):
  if abs(player.xcor()-target.xcor()) < 10 and abs(player.ycor()-target.ycor()) < 10:
    return True
  else:
    return False
	
# bind keyboard events to screen
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

# main loop for game
while True:
  screen.update()
  player.forward(1)
	
  # check for collisions with boundary
  if player.xcor() > 190 or player.xcor() < -190:
    player.right(180)
  elif player.ycor() > 190 or player.ycor() < -190:
    player.right(180)
	
  for target in targets:
    target.forward(1)
    
    # check for collisions with boundary
    if target.xcor() > 190 or target.xcor() < -190:
      target.right(180)
    elif target.ycor() > 190 or target.ycor() < -190:
      target.right(180)
      
    if isCollision(target):
      target.setposition(random.randint(-200, 200), random.randint(-200, 200))
      target.right(random.randint(0,360))
      score += 1
      scoreTurtle.clear()
      scoreTurtle.write("Score: " + str(score))