import turtle
import random

juni = turtle.Turtle()

for j in range(4):
  # r = random.randint(0,255)
  # g = random.randint(0,255)
  # b = random.randint(0,255)
  # juni.color(r, g, b)

  sideLength = 30
  if j == 0:
    juni.color('red')
  else:
    juni.color('black')

  for i in range(3):
    for i in range(4):
      juni.forward(sideLength)
      juni.right(90)

    sideLength += 20

  juni.right(90)