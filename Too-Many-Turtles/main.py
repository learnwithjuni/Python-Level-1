import turtle
import random

turtleList = []

for i in range(20):
  t = turtle.Turtle()
  t.shape("turtle")
  t.speed(0)
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color(r,g,b)
  t.right(random.randint(0,360))
  t.penup()
  t.goto(random.randint(-200,200), random.randint(-200,200))
  turtleList.append(t)

while True:
  for t in turtleList:
    t.forward(10)
    t.right(random.randint(0,360))