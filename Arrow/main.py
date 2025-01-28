import turtle
import random

t = turtle.Turtle()
t.speed(0)

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r,g,b)

t.begin_fill()
t.forward(130)
t.left(90)
t.forward(75)
t.right(135)
t.forward(120)
t.right(90)
t.forward(120)
t.right(135)
t.forward(75)
t.left(90)
t.forward(130)
t.right(90)
t.forward(20)

t.end_fill()

