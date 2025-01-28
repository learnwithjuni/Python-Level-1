import turtle
import random

t = turtle.Turtle()
t.speed(0)

# starter code (provided): draws gold square for the block of cheese
t.penup()
t.goto(-250, 200)
t.pendown()

t.color("gold")
t.begin_fill()
for i in range(4):
  t.forward(500)
  t.right(90)
t.end_fill()

# draw 10 cheese holes (circles) within the gold square
for j in range(10):
  t.penup()
  t.goto(random.randint(-200,200), random.randint(-250,150))
  t.pendown()
  t.color("yellow")

  # draw one randomly sized circle
  t.begin_fill()
  sideLength = random.randint(2,8)
  for k in range(36):
    t.forward(sideLength)
    t.right(10)
  t.end_fill()

