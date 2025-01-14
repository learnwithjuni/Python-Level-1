import turtle

t = turtle.Turtle()
t.speed(10000)

# start at (-200, 200)
t.penup()
t.goto(-200,200)
t.pendown()

# draw horizontal lines
for i in range(21):
  t.penup()
  t.goto(-200, 200-i*20)
  t.pendown()
  t.forward(400)

# go back to (-200,200)
t.penup()
t.goto(-200,200)
t.pendown()

# draw vertical lines
t.right(90)   # important!
for i in range(21):
  t.penup()
  t.goto(-200+i*20, 200)
  t.pendown()
  t.forward(400)