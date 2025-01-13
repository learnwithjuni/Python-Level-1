import turtle
import random

t = turtle.Turtle()
t.speed(10)

for i in range(4):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  
  length = 20
  
  for j in range(3):
    length += 20
    
    for k in range(4):
      t.forward(length)
      t.right(90)
  
  t.right(90)