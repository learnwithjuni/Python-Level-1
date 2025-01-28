import turtle
import random 

t = turtle.Turtle()
t.speed(0)

for j in range(8):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  #draw parallelogram
  t.begin_fill()
  for i in range(2):
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
  t.end_fill()

  t.right(360/8)
