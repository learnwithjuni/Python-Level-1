import turtle
import random

t = turtle.Turtle()
t.speed(2)
t.penup()

for i in range(100):

  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  
  x = random.randint(-100,100)
  y = random.randint(-100,100)
  t.goto(x,y)
  t.pendown()
  
  sideLength = random.randint(100,150)
  
  for i in range(50):
    t.forward(sideLength)
    t.left(123)
  
  t.penup()