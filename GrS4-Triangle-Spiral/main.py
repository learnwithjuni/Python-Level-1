import turtle
import random

t = turtle.Turtle()
t.speed(100)
screen = turtle.Screen()
screen.bgcolor('black')

length = 10

r = random.randint(0,255)
g = 0
b = random.randint(0,255)
t.color(r,g,b)

for i in range(40):
  g += 5
  length *= 1.1

  t.color(r,g,b)

  t.forward(length)
  t.left(120)
