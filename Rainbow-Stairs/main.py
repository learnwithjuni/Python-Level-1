import turtle
import random

juni = turtle.Turtle()

sideLength = 70

for i in range(3):
  
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  juni.color(r, g, b)
  
  juni.begin_fill()
  for i in range(4):
    juni.forward(sideLength)
    juni.right(90)
  juni.end_fill()

  sideLength -= 20
