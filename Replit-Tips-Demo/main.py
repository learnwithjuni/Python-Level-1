import turtle
import random 

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Set the colormode
turtle.colormode(255)

# Create a turtle 
t = turtle.Turtle()
t.speed(100)
t.penup()

# Draw 10 random shapes in random locations and random colors
for i in range(10):

  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  x = random.randint(-200,200)
  y = random.randint(-200,200)
  t.goto(x,y)
  t.pendown()

  sideLength = random.randint(5,50)
  numSides = random.randint(3,5)

  t.begin_fill()
  for i in range(numSides):
    t.forward(sideLength)
    t.left(360/numSides)
  t.end_fill()
  
  t.penup()

# Keep the screen open
#screen.mainloop()
