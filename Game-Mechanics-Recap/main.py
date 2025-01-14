import turtle
t = turtle.Turtle()

# Why would you use a while True loop?


# Write a while True loop which causes a turtle to go forward by 1px 100 times and then breaks.

counter = 0
while True:
  t.forward(1)
  if counter >= 100:
    break

# Change your while True loop to break instead when the turtle's y-coordinate is above 50.

while True:
  t.forward(1)
  if t.ycor() > 50:
    break

# Change your while True loop to break as well if the turtle is more than 100px to the left side of the screen.

while True:
  t.forward(1)
  if t.ycor() > 50 or t.xcor() < 100:
    break

# Explain how the above code works:
# 
# Explain how we use an or if statement to end a while True loop at an appropriate time
# 
