import turtle
t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("light blue")

t.speed(0)
t.pensize(4)

t.color("blue")
t.penup()
t.goto(-110, -25)
t.pendown()
for i in range(36): 
  t.forward(10)
  t.right(10)

t.color("black")
t.penup()
t.goto(-20, -25)
t.pendown()
for i in range(36): 
  t.forward(10)
  t.right(10)

t.color("red")
t.penup()
t.goto(90, -25)
t.pendown()
for i in range(36): 
  t.forward(10)
  t.right(10)

t.color("yellow")
t.penup()
t.goto(-55, -75)
t.pendown()
for i in range(36): 
  t.forward(10)
  t.right(10)

t.color("green")
t.penup()
t.goto(45, -75)
t.pendown()
for i in range(36): 
  t.forward(10)
  t.right(10)