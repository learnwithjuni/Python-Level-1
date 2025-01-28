import turtle
import random

t = turtle.Turtle()
t.speed(0)

for i in range(8):
  # move to starting position
  t.penup()
  t.forward(150)
  t.pendown()
  
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

# draw circle
  t.begin_fill()
  for i in range(36):
    t.forward(5)
    t.right(10)
  t.end_fill()
  t.penup()
  
  # go back to (0,0) and turn
  t.goto(0,0)
  t.pendown()
  t.right(360/8)