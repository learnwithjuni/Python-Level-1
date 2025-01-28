import turtle
import random

t = turtle.Turtle()
t.speed(0)

for i in range(36):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  # draw top triangle
  t.begin_fill()
  for i in range(3):
    t.forward(100)
    t.right(120)
  
  # draw bottomo triangle
  for i in range(3):
    t.forward(100)
    t.left(120)
  t.end_fill()
  t.right(10)