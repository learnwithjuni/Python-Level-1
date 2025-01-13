import turtle

t = turtle.Turtle()
t.speed(10000)

sideLength = 10

t.penup()
t.goto(0,200)
t.pendown()
t.setheading(300)

for i in range(50):
  for j in range(3):
    t.forward(sideLength)
    t.right(120)
    
  sideLength = sideLength + 10