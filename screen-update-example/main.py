import turtle

# Create the drawing turtle
juni = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Draw a square, without disabling animation
for i in range(4):
  juni.forward(100)
  juni.left(90)

# Disable all animation
screen.tracer(0)

# Program the turtle to move to another spot to draw another square
juni.penup()
juni.goto(-200, 0)
juni.pendown()

# Draw another square and update the screen after the square is drawn
for i in range(4):
  juni.forward(100)
  juni.left(90)
screen.update()

screen.mainloop()