import turtle
t = turtle.Turtle()
t.speed(10)

# draw clock ticks
for i in range(12):
  t.right(360/12)
  t.penup()
  t.goto(0,0)
  t.forward(100)
  t.pendown()
  t.forward(20)

# draw hour hand
t.penup()
t.goto(0,0)
t.pendown()
t.forward(70)

# draw minute hand
t.penup()
t.goto(0,0)
t.pendown()
t.left(90)
t.forward(50)