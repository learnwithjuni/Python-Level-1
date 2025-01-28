import turtle
import random

t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()
screen.bgcolor('black')

for i in range(100):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)

  size = random.randint(1,5)

  t.penup()
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  t.goto(x,y)
  t.pendown()

  # draw semicircle
  t.setheading(90)
  t.begin_fill()
  for i in range(36):
    t.forward(size)
    t.right(5)
  t.right(90)

  t.forward(size * 28) 
  t.left(90)
  
  # draw rectangle
  for i in range(2): 
    t.forward(size * 5) 
    t.left(90)
    t.forward(size * 34)
    t.left(90)
  
  t.end_fill()
  t.penup()


