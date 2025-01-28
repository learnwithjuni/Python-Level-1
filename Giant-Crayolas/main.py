import turtle
import random

t = turtle.Turtle()
t.speed(0)

def drawCrayola(r,g,b,size):
  t.penup()
  t.goto(random.randint(-300,300), 0)
  t.pendown()

  t.color(r,g,b)
  t.begin_fill()
  for i in range(3):
    t.forward(size)
    t.left(120)
  for i in range(4):
    t.forward(size)
    t.right(90)
  t.end_fill()

for i in range(50):
  red = random.randint(0,255)
  green = random.randint(0,255)
  blue = random.randint(0,255)
  size = random.randint(100,200)
  drawCrayola(red, green, blue, size)