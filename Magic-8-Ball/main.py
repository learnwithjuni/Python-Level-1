import turtle
import random

t = turtle.Turtle()
t.speed(0)

# draw outer circle
t.begin_fill()
for i in range(36):
  t.forward(20)
  t.right(10)
t.end_fill()

# draw inner circle
t.penup()
t.goto(5, -45)
t.pendown()
t.color("white")
t.begin_fill()
for i in range(36):
  t.forward(12)
  t.right(10)
t.end_fill()

# draw the 8
t.penup()
t.goto(-5, -130)
t.pendown()
t.color("black")
t.write("8", font=("Arial", 50, "normal"))
t.ht()