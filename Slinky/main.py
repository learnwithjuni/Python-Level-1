import turtle
import random

t = turtle.Turtle()
t.speed(0)

for i in range(10): 
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  for i in range(36): 
    t.forward(10)
    t.right(10)
    
  t.forward(30)

