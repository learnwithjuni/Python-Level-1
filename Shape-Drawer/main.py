import turtle
import random

t = turtle.Turtle()
t.speed(0)

numSides = int(input("How many sides should I draw? "))

for i in range(20):
  x = random.randint(-250,250)
  y = random.randint(-250,250)

  size = random.randint(25,100)

  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)

  t.penup()
  t.goto(x,y)
  t.pendown()

  t.color(r,g,b)
  for j in range(numSides):
    t.forward(size)
    t.right(360/numSides)
