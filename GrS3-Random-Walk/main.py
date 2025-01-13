import turtle
import random

turtle.colormode(255)

t = turtle.Turtle()

t.shape("turtle")
t.pensize(random.randint(1, 10))

num_steps = 100

# Perform random walk
for _ in range(num_steps):
  # Generate random length and angle
  step_length = random.randint(10, 30)
  turn_angle = random.randint(-180, 180)

  # Generate random colors
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  # Set the color of the turtle
  t.color(r, g, b)

  # Move the turtle
  t.forward(step_length)
  t.left(turn_angle)
