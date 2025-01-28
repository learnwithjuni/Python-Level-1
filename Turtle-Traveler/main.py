import turtle

t = turtle.Turtle()
t.speed(0)

color = input("What color should I change into? ")
t.color(color)

print("Where should the turtle go?")
x = input("What is the x coordinate I should go to?" )
y = input("What is the y coordinate I should go to?" )

t.penup()
t.goto(x,y)
t.pendown()

t.write("Look I made it to " + x + ", " + y + "!")