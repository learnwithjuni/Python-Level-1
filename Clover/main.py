import turtle
import random 

t = turtle.Turtle()
t.speed(0)

t.color("green")
t.begin_fill()
for j in range(4):
  for i in range(18):
    t.right(10)
    t.forward(20)
  t.right(90)
t.end_fill()
