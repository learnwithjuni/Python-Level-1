import turtle
import random

t = turtle.Turtle()
t.speed(0)

# starter code (provided): draws gold square for the block of cheese
t.penup()
t.goto(-250, 200)
t.pendown()

t.color("gold")
t.begin_fill()
for i in range(4):
  t.forward(500)
  t.right(90)
t.end_fill()