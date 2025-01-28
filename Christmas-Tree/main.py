import turtle
import random 

t = turtle.Turtle()
t.speed(3)
t.color("green")

y = 0

for i in range(4):
  # draw triangle
  t.begin_fill()
  for i in range(3):
    t.forward(150)
    t.left(360/3)
  t.end_fill()

  # move up to draw next triangle
  y = y + 30
  t.penup()
  t.goto(0,y)
  t.pendown()