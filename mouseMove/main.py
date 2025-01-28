import turtle

# Function to move player turtle to follow the mouse
def moveTurtle(x, y):
    player.goto(x, y)

def movePenUp():
  player.pu()

def movePenDown():
  player.pd()


# Setup screen
screen = turtle.Screen()


# Create player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.speed(0)
player.left(90)
player.penup()

# Bind mouse movement to move player turtle
player.ondrag(moveTurtle)

# assign keys to functions
screen.onkey(movePenUp, "w")
screen.onkey(movePenDown, "s")

screen.listen()

# Keep the window open
screen.mainloop()
