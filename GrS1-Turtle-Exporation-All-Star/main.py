import turtle

juni = turtle.Turtle()

#draw square
juni.forward(100)
juni.right(90)
juni.forward(100)
juni.right(90)
juni.forward(100)
juni.right(90)
juni.forward(100)
juni.right(90)

#move turtle
juni.penup()
juni.goto(100, 100)
juni.pendown()

juni.color("blue")

#draw triangle and fill color
juni.begin_fill()
juni.forward(100)
juni.right(120)
juni.forward(100)
juni.right(120)
juni.forward(100)
juni.right(120)
juni.end_fill()

#NOT NEEDED ON JUNI'S SCREEN, keeps the turtle window open on repl.it
turtle.mainloop()
