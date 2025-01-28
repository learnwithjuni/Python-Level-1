import turtle
import random

t = turtle.Turtle()
t.speed(0)

size = 35

for i in range(25):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  # draw circle
  t.begin_fill()
  for i in range(36):
    t.forward(size)
    t.right(10)
  t.end_fill()

  size = size-1
