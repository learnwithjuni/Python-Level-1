import turtle
import random

turtle.colormode(255)

t = turtle.Turtle()
t.speed(1000)

for i in range(100):
    t.pendown()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)

    t.begin_fill()
    for i in range(6):
        t.right(60)
        t.forward(50)
    t.end_fill()

    t.penup()
    t.right(10)
