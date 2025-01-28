import turtle
import random 

screen = turtle.Screen()
t = turtle.Turtle()

# this section of the script matches "when green flag clicked"
t.penup()
screen.clear()
t.pensize(1)
t.color("blue")
t.goto(0,0)
t.setheading(90)

# this section of the script matches "when 1 key pressed"
def one():
  t.pendown()
  for i in range(4):
    t.forward(100)
    t.right(90)
  t.penup()

# this section of the script matches "when 2 key pressed"
def two():
  t.pendown()
  for i in range(3):
    t.forward(100)
    t.left(120)
  t.penup()

# this section of the script matches "when 3 key pressed"
def three():
  t.pendown()
  t.forward(100)
  t.right(150)
  t.forward(30)
  t.forward(-30)
  t.left(300)
  t.forward(30)
  t.forward(-30)
  t.right(150)
  t.forward(-100)
  t.penup()

# this section of the script matches "when up arrow key pressed"
def up():
  t.setheading(90)
  t.forward(10)

# this section of the script matches "when down arrow key pressed"
def down():
  t.setheading(270)
  t.forward(10)

# this section of the script matches "when left arrow key pressed"
def left():
  t.setheading(180)
  t.forward(10)

# this section of the script matches "when right arrow key pressed"
def right():
  t.setheading(0)
  t.forward(10)

screen.onkey(one, "1")
screen.onkey(two, "2")
screen.onkey(three, "3")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()