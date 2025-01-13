# FUNCTIONS
#########################################

# Can you write out your import statements and create a turtle?

import turtle
import random

t = turtle.Turtle()
t.speed(500)

# What are functions? If we create a function to help us draw a specific shape, what advantages does it give us over just using a for loop to create a shape? When are functions useful?

  # Ans: Functions allow us to specify inputs, and we only need to define the function once in order to call it whenever we want to use it.

# Define a function called moveForward50() which moves the turtle forward by 50 pixels.

def moveForward50():
  t.forward(50)

# Define a function called drawSquare() which takes in the square's side length as input.

def drawSquare(sideLength):
  for i in range(4):
    t.forward(sideLength)
    t.right(90)

# Can you call both the functions you just wrote? For our square function, specify that we want the side length to be 25. 

moveForward50()
drawSquare(25)

# Using the drawSquare() function, draw 15 squares. The first square should start with a side length of 10, and then the side length for each square should increase by 5 pixels.

sideLength = 10
for i in range(15):
  drawSquare(sideLength)
  sideLength += 5

#########################################

# EVENT LISTENERS

#########################################

# What is an event listener?  What functionality do they help us add to our programs?

  # Ans: Event listeners allow us to assign functions to keys when they are pressed.

# Create the screen variable we need for our event listeners.

screen = turtle.Screen()

# Program an event listener that moves the turtle 50 pixels forward each times the right arrow key is pressed. Hint: You can use one of the functions we created earlier.

screen.onkey(moveForward50, "Right")

# Program an event listener that draws a triangle each time the up arrow key is pressed. Then, add a line of code that also draws a triangle each time the "A" key is pressed.

def drawTriangle():
  for i in range(3):
    t.forward(20)
    t.right(120)

screen.onkey(drawTriangle, "Up")
screen.onkey(drawTriangle, "A")

# If the student has not already added this to their program, what is the last line of code we have to add to make sure that these event listeners actually function?

screen.listen()

#########################################

# CONDITIONALS

#########################################

# What is a conditional statement?
  # Ans: A conditional is an if-then statement that tells the program to do something only if the condition is true (else, do something else).

# Create a variable called num and set it to a random number between 0 and 10. If num is less than 5, set it equal to 0. If num is equal to 5, double it. Otherwise, add 10 to the number.

import turtle
import random
t = turtle.Turtle()

num = random.randint(0,10)
if num < 5:
  num = 0
elif num == 5:
  num *= 2
else:
  num += 10
  

# Use conditionals to write "The turtle is out of bounds!" on the screen, if the turtle's x and y coordinates are outside of -150 and 150.

# Building off the last conditional, if the turtle's x coordinate is between 100 and 150, write "The turtle is near the right boundary!"

# Finally, if neither of the two previous conditions are true, write "The turtle is near the center!"
 
if t.xcor() > 150 or t.xcor() < -150 or t.ycor() > 150 or t.ycor() < -150:
  t.write("The turtle is out of bounds!")
elif t.xcor() > 100 and t.xcor() < 150:
  t.write("The turtle is near right boundary!")
else:
  t.write("The turtle is near the center")

#########################################

# LISTS

#########################################

# What is a list? Why do we use lists in Python?

  # Ans: A list is a variable that helps us store an ordered collection of things, such as numbers, strings, or turtles.

# Create an empty list called whales.
whales = []

# Create three more turtles (name them anything) and add them to the list.

for i in range(3):
  whale = turtle.Turtle()
  whales.append(whale)

# Use a loop to move each turtle in our list backward by 30 pixels.

for turtle in whales:
  turtle.backward(30)

#########################################

# CONDITIONALS AND WHILE TRUE LOOPS

#########################################

# If we wanted our turtle to keep moving until it hit something, what type of loop would we use? Why?

  # Ans: We would use a "while True" loop which lets us continuously move the turtle forward until a condition is triggered that breaks us out of the loop.

# How do we make a "while True" loop stop running?

  # Ans: We have to use the break keyword.

# Using our moveForward50() and the conditional statement, make the turtle move forward until its x coordinate reaches 200.

while True: 
  if t.xcor() > 200:
    break
  else:
    moveForward50()