# PYTHON TURTLE BASICS

#########################################

# When working with Python with Turtle, what do we first need to make sure to import? Can you think of anything else we usually import? 
# Write out both import statements. Why do we need to use these import statements?

import turtle
import random 

# Crteate a Turtle named whale.

whale = turtle.Turtle()
whale.speed(100000)

# Make whale move forward 200 pixels.

whale.forward(200)

# Make whale turn 200 degrees to the right.
whale.right(200)

# How many degrees do we have to turn after drawing each side to make a triangle? How do you know?  
  # Ans: 120 degrees. The interior angle of a triangle is 60 degrees, so the exterior angle is 120 degrees. Alternatively, a triangle has 3 sides and 360 / 3 = 120.

# A dodecagon is a shape with 12 sides of equal length. How many degrees would we need to turn after drawing each side?

  # Ans: 30 degrees. 360 / 12 = 30.

#########################################

# LOOPS & MOVEMENT

#########################################

# Can you explain to me what a loop is? Why are loops useful in programming?


# Write a loop that makes whale move forward 2 pixels, repeating 20 times.

for i in range(20):
  whale.forward(2)


# Use a loop to draw a square with a side length of 50 pixels.

for i in range(4):
  whale.forward(50)
  whale.right(90)

# Add another square, starting at the coordinate (-50,-50). Make sure our turtle doesn’t draw a line connecting the two!

whale.penup()
whale.goto(-50,-50)
whale.pendown()
for i in range(4):
  whale.forward(50)
  whale.right(90)

# Program whale to draw a circle using a loop that repeats 36 times.

for i in range(36):
  whale.forward(15)
  whale.right(360/36)

# As mentioned earlier, a dodecagon is a shape with 12 sides of equal length. Write out the code to draw a dodecagon with sides of length 15 pixels.

for i in range(12):
  whale.forward(15)
  whale.right(360/12)


#########################################

# VARIABLES AND RANDOM

#########################################

# Create a variable called numPotatoes and set it to a random number between 42 and 90.

numPotatoes = random.randint(42,90)  

# What are the three variables we often use when defining a color? What do they stand for? What happens if we make one of them a larger number than the rest? 

  # Ans: r,g,b. They stand for red, green, and blue, which are the base colors we combine to make a specific color in computer graphics; the color would be "more" of the base color you made larger (e.g. a shade closer to red) 

# Use these three variables to set the color of whale to a random color. Test it out and see if we get a different color each time!

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
whale.color(r,g,b)
whale.forward(100)

# Bonus: Try to set the color of whale randomly without creating any r,g,b variables. (Hint: You can do this in one line of code.)

whale.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

# Create a variable called sideLength and set it equal to 10.

sideLength = 10

# Write a loop that repeats 50 times. Each time in the loop, whale should move forward by sideLength, turn 90 degrees, and increment sideLength by 5.

# for i in range(50):
#   whale.forward(sideLength)
#   whale.right(90)
#   sideLength += 5

# Update your code from the previous problem so that whale starts out with a random color and progressively becomes more green with each side of the spiral shape.

r = random.randint(0,256)
g = 0
b = random.randint(0,256)

for i in range(50):
  whale.color(r,g,b)
  whale.forward(sideLength)
  whale.right(90)
  sideLength += 5
  g += 3

#########################################

# NESTED LOOPS

#########################################                 

# How do we know when to use nested for loops?

  # Ans: We would use them when we want some code that is already being repeated to repeat within another loop.

# Write out the code to draw a dodecagon 5 times, retracing over itself. Use the code we previously wrote to draw one dodecagon.

for i in range(5):
  for i in range(12):
    whale.forward(50)
    whale.right(360/12)

# Now, make each dodecagon drawn with a random color and in a random location, where the x and y coordinates are between -200 and 200.
   
# for i in range(5):
#   whale.penup()
#   whale.goto(random.randint(-200,200), random.randint(-200,200))
#   whale.pendown()
#   whale.color(random.randint(0,256),random.randint(0,256),random.randint(0,256))

#   for i in range(12):
#     whale.forward(50)
#     whale.right(360/12)


# Update your code for the previous problem so that each dodecagon's side length is 10 larger than the previous one.

sideLength = 50
for i in range(5):
  whale.penup()
  whale.goto(random.randint(-200,200), random.randint(-200,200))
  whale.pendown()
  whale.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))

  for i in range(12):
    whale.forward(sideLength)
    whale.right(360/12)
  
  sideLength += 10

# In the previous problem's code, how many total times does the whale move forward?
  # Ans: 60 times (the outer loop runs 5 times and the inner loop runs 12 times for each iteration of the outer loop)

##########################################################

# Optional Practice Project: Use a loop to draw a zigzagging line, where the line has about 30 zigzags and each line segment is about 20 pixels.

for i in range(30):
  whale.right(150)
  whale.forward(20)
  whale.left(150)
  whale.forward(20)           