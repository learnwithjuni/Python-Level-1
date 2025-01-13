import turtle
import random

screen = turtle.Screen()
screen.bgcolor('black')

t = turtle.Turtle()
t.speed(10000)
t.penup()

for i in range(100):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  x = random.randint(-200,200)
  y = random.randint(-200,200)
  t.goto(x,y)

  size = random.randint(10,100)

  t.pendown()
  t.begin_fill()
  for i in range(5):
    t.forward(size)
    t.right(144)
  t.end_fill()
  t.penup()