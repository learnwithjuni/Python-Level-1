import turtle

t = turtle.Turtle()
s = turtle.Screen()
isDrawing = True

def stop():
  global isDrawing
  isDrawing = False

s.onkey(stop, "Left")
s.listen()

while True:
  if isDrawing:
    t.forward(1)
  else:
    break