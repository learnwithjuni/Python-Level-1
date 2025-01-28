import turtle
import random

t = turtle.Turtle()
t.speed(0)
for i in range(8):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  t.begin_fill()

  # draw first rectangle
  for i in range(2):
    t.forward(40)
    t.right(90)
    t.forward(200)
    t.right(90)
  
  # draw second rectangle
  for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(40)
    t.right(90)

  t.end_fill()
  t.right(360/8)