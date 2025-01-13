import turtle
import random

t = turtle.Turtle()
t.speed(1000)

side = 10

for i in range(50):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  
  t.forward(side)
  t.right(90)
  
  side = side + 5