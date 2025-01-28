import turtle
import random

t = turtle.Turtle()
t.speed(0)

# draw roof
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r,g,b)
t.begin_fill()
for i in range(3):
  t.forward(150)
  t.left(360/3)
t.end_fill()

# draw walls
t.forward(150)
t.setheading(270)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r,g,b)
t.begin_fill()
for i in range(4):
  t.forward(150)
  t.right(90)
t.end_fill()