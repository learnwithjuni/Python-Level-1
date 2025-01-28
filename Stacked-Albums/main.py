import turtle
import random

t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()
screen.bgcolor('black')

size = 10
for i in range(10):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  # draw square
  t.begin_fill()
  for i in range(4): 
    t.forward(size)
    t.right(90)
  t.end_fill()
  
  # setup for next square
  t.penup()
  t.goto(size * 2,size * 2)
  t.pendown()
  size += 10
