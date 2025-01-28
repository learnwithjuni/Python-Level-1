import turtle
t = turtle.Turtle()
t.speed(5)

t.color("red")
t.left(60)
t.begin_fill()
for i in range(3):
  t.forward(100)
  t.right(120)
t.end_fill()

t.color("blue")
t.right(120)
t.begin_fill()
for i in range(3):
  t.forward(100)
  t.left(120)
t.end_fill()