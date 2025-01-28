import turtle
import random

t = turtle.Turtle()
t.speed(0)

sideLength = 10 
for i in range(30):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  t.forward(sideLength)
  t.right(144)
  sideLength += 10 