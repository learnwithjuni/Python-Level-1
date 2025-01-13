import turtle
import random

t = turtle.Turtle()
t.speed(100000)

# set random number of circles
numCircles = random.randint(0,100)

for i in range(numCircles):
  t.penup()
  
  # set random color
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  
  # set random side length
  sideLength = random.randint(0, 25)
  
  # set random starting position
  x = random.randint(-300,300)
  y = random.randint(-300,300)
  t.goto(x,y)
  
  # draw circle
  t.pendown()
  t.begin_fill()
  for i in range(36):
    t.forward(sideLength)
    t.right(10)
  t.end_fill()
  
  t.penup()