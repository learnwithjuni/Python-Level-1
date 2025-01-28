import turtle
import random

t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()
screen.bgcolor("black")

def forward():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  t.forward(10)

def right():
  t.right(5)

def left():
  t.left(5)

screen.onkey(forward, "up")
screen.onkey(left, "left")
screen.onkey(right, "right")

screen.listen()