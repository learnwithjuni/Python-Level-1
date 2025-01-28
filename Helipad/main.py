import turtle
import random

t = turtle.Turtle()
t.speed(0)

for i in range(36):
  t.forward(20)
  t.right(10)

t.penup()
t.goto(-65,-190)
t.color("Red")
t.write("H", font = ("Arial", 160, "normal"))
