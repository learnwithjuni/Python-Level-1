import turtle
import random

juni = turtle.Turtle()

for l in range(4):
  # r = random.randint(0,255)
  # g = random.randint(0,255)
  # b = random.randint(0,255)
  # juni.color(r, g, b)

  sideLength = 30

  for j in range(3):
    for i in range(4):
      if i == 0:
        juni.color('red')
      else:
        juni.color('green')
      juni.forward(sideLength)
      juni.right(90)

    sideLength += 20

  juni.right(90)