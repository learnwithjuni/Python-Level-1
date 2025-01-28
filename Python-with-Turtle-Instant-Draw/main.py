import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def drawCircle():
  for i in range(36):
    t.forward(5)
    t.right(10)

screen.tracer(0)  # this disables animation
t.ht()

while True:
  t.clear()
  t.forward(1)
  drawCircle()

  # this updates the canvas with what has been drawn
  screen.update()