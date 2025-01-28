import turtle
import random

t = turtle.Turtle()
t.speed(0)

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r, g, b)

x = 0
y = 0

for i in range(5):
  t.goto(x,y)

  t.begin_fill()
  for i in range(2):
    t.forward(80)
    t.right(90)
    t.forward(40)
    t.right(90)
  t.end_fill()

  x += 40
  y -= 40