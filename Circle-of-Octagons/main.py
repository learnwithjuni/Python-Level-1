import turtle
import random

t = turtle.Turtle()
t.speed(0)

for i in range(36):
  # set random color
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  # draw octagon
  for i in range(8):
    t.forward(50)
    t.right(360/8)
  
  # turn 10 degrees
  t.right(10)