import turtle

t = turtle.Turtle()
signDrawer = turtle.Turtle()

# Go to the starting position
signDrawer.penup()
signDrawer.goto(50,50)
signDrawer.pendown()

# Draw a stop sign 
signDrawer.color("red")
signDrawer.begin_fill()
for i in range(8):
  signDrawer.forward(50)
  signDrawer.right(360/8)
signDrawer.end_fill()

# Draw text on sign, then hide the turtle
signDrawer.penup()
signDrawer.color("white")
signDrawer.goto(75,-20)
signDrawer.pendown()
signDrawer.write("STOP", align="center", font=("Arial", 16, "normal")) 
signDrawer.ht()

# Configure the main turtle
t.goto(-200,0)
t.color("green")
t.shape("turtle")
t.pendown()

# Program the turtle to move forward as long as the x coordinate is less than 0
while (t.xcor() < 0):
  # Print the x coordinate of the turtle
  t.clear()
  t.write(t.xcor(), font=("Arial", 16, "normal"))
  t.forward(1)

# Keep the window open: note this line is only needed when running projects in repl.it
turtle.mainloop()

