import turtle
import random

t = turtle.Turtle()
t.speed(4)

t.pensize(4)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r,g,b)

# draw the triangle
t.begin_fill()
for i in range(5): 
  t.forward(150)
  t.left(120)
t.end_fill()

# adjust direction the turtle is pointing
t.right(60)

# draw the circle
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
t.color(r,g,b)

t.begin_fill()
for i in range(36): 
  t.right(10)
  t.forward(2)
t.end_fill()