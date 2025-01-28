import turtle
import random

t = turtle.Turtle()
t.speed(0)

numSquares = int(input("How many squares should I draw? "))
lengthChange = int(input("Each square will start with a side length of 25. How many pixels should the side length increase by for each square? "))
size = 25
for i in range(numSquares):
  x = random.randint(-250,250)
  y = random.randint(-250,250)
  t.penup()
  t.goto(x,y)
  t.pendown()
  for j in range(4):
    t.forward(size)
    t.right(90)
  size += lengthChange
