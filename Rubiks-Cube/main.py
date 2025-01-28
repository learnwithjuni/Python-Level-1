import turtle
import random

t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()
screen.bgcolor("black")

y = 0 
for i in range(3):
  for j in range(3):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    t.color(r, g, b)
    y -= 20

    t.begin_fill()  
    for k in range(4):
      t.forward(50)
      t.right(90)
    t.end_fill()

    t.penup()
    t.forward(60)
    t.pendown()

  t.penup()
  t.goto(0,y)
  t.pendown()