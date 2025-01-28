import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
t.right(45)
t.speed(5)


screen = turtle.Screen()

def changeColor():
  t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

def drawDiamond():
  sideLength = 20
  for i in range(3):
    changeColor()
    t.begin_fill()
    for i in range(4):
      t.forward(sideLength)
      t.right(90)
    t.end_fill()

def changeLocation():
  t.penup()
  t.goto(random.randint(-200,200),random.randint(-200,200))
  t.pendown()

def drawCircle():
  sideLength = 3
  for i in range(3):
    changeColor()
    t.begin_fill()
    for i in range(36):
      t.forward(sideLength)
      t.right(10)
    t.end_fill()

def drawPyramid():
  sideLength = 30
  for i in range(3):
    changeColor()
    t.begin_fill()
    for i in range(3):
      t.forward(sideLength)
      t.right(120)
    t.end_fill()
      
screen.onkey(drawDiamond, "d")
screen.onkey(drawCircle, "c")
screen.onkey(drawPyramid, "p")
screen.onkey(changeLocation, "space")
screen.listen()