import turtle
import random

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(0,100)
t.pendown()
t.color("gold")
t.begin_fill()

t.setheading(240)
t.forward(100)
t.left(110)
t.forward(50)
t.right(110)
t.forward(100)
t.left(170)
t.forward(130)
t.left(120)
t.forward(50)
t.right(93)
t.forward(80)

t.end_fill()