import turtle
import random

turtle.colormode(255)

# Set up the turtle screen
screen = turtle.Screen()

# Create a turtle for drawing
artist = turtle.Turtle()
artist.speed(0)  # Adjust the drawing speed


def drawCircle():
  # Draw a colorful circle
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  artist.color(r, g, b)

  circleSize = random.randint(1, 10)

  artist.begin_fill()
  for i in range(36):
    artist.forward(circleSize)
    artist.right(10)
  artist.end_fill()


# Function to handle mouse clicks
def move(x, y):
  artist.penup()  # Lift the pen to move to the clicked position
  artist.goto(x, y)
  artist.pendown()  # Lower the pen to start drawing

  drawCircle()


# Set up the event listener
screen.onclick(move)

# Keep the window open
turtle.done()
