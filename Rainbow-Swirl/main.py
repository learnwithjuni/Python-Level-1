import turtle
import random 

t = turtle.Turtle()
t.speed(0)

r = random.randint(0,255)
g = random.randint(0,255)
b = 0

for i in range(36):
  t.penup()
  t.goto(0,0)
  t.pendown()
  t.right(10)
  t.color(r,g,b)
  b += 10
  for i in range(18):
    t.right(10)
    t.forward(20)
  t.right(180)
