import turtle


# Function to rotate player turtle to face the cursor
def rotate_to_cursor(x, y):
  player.goto(x,y)

 

# Setup screen
screen = turtle.Screen()

# Create player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

player.ondrag(rotate_to_cursor)


# Keep the window open
screen.mainloop()
