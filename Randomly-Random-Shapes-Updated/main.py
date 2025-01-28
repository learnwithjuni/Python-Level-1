import turtle
import random
turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

# define a function that draws a shape with a random number of sides
def draw_random_shape():
  numSides = random.randint(3, 9) 
  t.begin_fill()
  turnAngle = 360.0 / numSides 
  # you can also use a random side length for more randomness! 
  sideLength = 15
  for i in range(numSides):
    t.forward(sideLength)
    t.right(turnAngle)
  t.end_fill()

# call your function a random number of times, programming the turtle to go to a new random location and turn a new random color each time
numShapes = random.randint(10,50)

for i in range(numShapes):
  # Go to random position
  t.penup()
  x = random.randint(-200, 200)
  y = random.randint(-200, 200)
  t.goto(x, y)
  t.pendown()

  # Make the turtle turn a random color
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r, g, b)

  draw_random_shape()


