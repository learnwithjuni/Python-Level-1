import turtle
t = turtle.Turtle()
screen = turtle.Screen()

screen.register_shape("rect", ((5,10), (5,-10), (-5,-10), (-5,10)))
t.shape("rect")

t.forward(100)
t.right(90)
t.forward(100)