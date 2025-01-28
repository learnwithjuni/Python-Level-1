import turtle
import random

t = turtle.Turtle()
t.speed(5)

# draw randomly colored box
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r, g, b)
t.begin_fill()
for i in range(4):
  t.forward(150)
  t.right(90)
t.end_fill()

# draw randomly colored cross
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r, g, b)
t.right(45)
t.pensize(4)
t.forward(212)
t.left(135)
t.penup()
t.forward(150)
t.pendown()
t.left(135)
t.forward(212)