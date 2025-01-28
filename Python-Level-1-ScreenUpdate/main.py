
import turtle

# Create the drawing turtle
juni = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()

#Disable all animation
screen.tracer(0)

while True:
  juni.clear()

  # Draw a circle
  for i in range(360):
    juni.forward(1)
    juni.right(1)
    # First have the student draw the circle and update screen inside of the for loop.
    screen.update()

  juni.forward(1)
  juni.right(10)
  
  # Then move the screen.update after the for loop to show the student how the entire circle is shown/drawn at once.
  #screen.update()

turtle.done()

#EXTRA EXERCISE:
'''

import turtle
import random 

# Create the drawing turtle
juni = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()

#Disable all animation
screen.tracer(0)

while True:
  juni.pu()
  juni.goto(random.randint(-250,250), random.randint(-250,250))
  juni.pd()
  for i in range (36):

    #juni.clear()

    # Draw a circle
    for i in range(360):
      juni.forward(1)
      juni.right(1)
      # First have the student draw the circle and update screen inside of the for loop
      #screen.update()

    #juni.forward(10)
    juni.right(10)


    # Then move the screen.update after the for loop to show the student how the entire circle is shown/drawn at once
  screen.update()



turtle.done()
'''