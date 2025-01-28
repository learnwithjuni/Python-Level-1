import turtle

t = turtle.Turtle()
signDrawer = turtle.Turtle()

# draw a stop sign
signDrawer.penup()
signDrawer.goto(50,50)
signDrawer.pendown()
signDrawer.color("red")
signDrawer.begin_fill()
for i in range(8):
  signDrawer.forward(50)
  signDrawer.right(360/8)
signDrawer.end_fill()
# draw text on sign, then hide the turtle
signDrawer.penup()
signDrawer.color("white")
signDrawer.goto(75,-20)
signDrawer.pendown()
signDrawer.write("STOP", align="center", font=("Arial", 16, "normal"))
signDrawer.ht()


t.goto(-200,0)
t.color("green")
t.shape("turtle")
t.pendown()


# Program the turtle to move forward as long as the x coordinate is less than 0
while (t.xcor() < 0):
  # print the x cordinate of the turtle
  t.write(t.xcor(), font=("Arial", 16, "normal"))
  t.clear()
  t.forward(1)

# Keep the window open: this line is only needed when running projects in repl.it
turtle.mainloop()

