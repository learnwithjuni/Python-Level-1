import turtle
import random

# create our drawing turtle
drawer = turtle.Turtle()
drawer.speed(0)

# screen turtle meant to color the turtle
screen = turtle.Screen()
screen.bgcolor("purple")

# function that given a radius, will draw a single petal
def drawPetal(radius):
  # get direction of the turtle
  heading = drawer.heading()
  
  # draw a small slice of a circle; first half of our petal
  drawer.circle(radius, 90)

  # turn to complete the petal
  drawer.left(120)
  
  # draw the other slice of the circle
  drawer.circle(radius, 90)
  
  # reset the heading to the original direction
  drawer.setheading(heading)
  
# function that draws a flower
def drawFlower():

  # get a random radius that will determine the size of the petals
  radius = random.randint(100, 200)

  # get a random number of petals for our flower
  petals = random.randint(6, 12)
  
  # get random colors for the flower
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  
  # set the drawer's color
  drawer.color(r,g,b)
  
  # get random x,y positions
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)

  # move to random location
  drawer.penup()
  drawer.goto(x,y)
  drawer.pendown()
  
  # uncomment below line and end_fill line to fill the shape with the desired color
  # drawer.begin_fill()
  
  # draw petals according to the number of petals we got earlier
  for i in range(petals):
    drawPetal(radius)
    drawer.left(360 / petals)
  
  # drawer.end_fill()

# draw 10 random flowers
for i in range(10):  
  drawFlower()