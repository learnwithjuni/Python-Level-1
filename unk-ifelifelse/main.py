import turtle
import random
import time

# Change the "color" and "using" variable to show the student the behavior between if and elif

#traffic light color set to
color = "green"

# Set using to "if" to show how if statements work
# set using to "elif" to show how elif's work
using = "elif"

# Set up the screen
screen = turtle.Screen()
screen.setup(width=700, height=800)

screen.tracer(0)

# Set up Turtle
juni = turtle.Turtle()


# Function to draw the traffic light
def draw_traffic_light():

  juni.pu()
  juni.goto(-200, 280)
  juni.pd()
  for i in range(2):
    juni.forward(200)
    juni.right(90)
    juni.forward(480)
    juni.right(90)

  juni.pu()
  juni.goto(-100, 250)
  juni.pd()

  juni.color("red")
  juni.begin_fill()

  for i in range(36):
    juni.forward(10)
    juni.right(10)
  juni.end_fill()

  juni.pu()
  juni.goto(-100, 100)
  juni.pd()

  juni.color("yellow")
  juni.begin_fill()

  for i in range(36):
    juni.forward(10)
    juni.right(10)
  juni.end_fill()

  juni.pu()
  juni.goto(-100, -50)
  juni.pd()

  juni.color("green")
  juni.begin_fill()

  for i in range(36):
    juni.forward(10)
    juni.right(10)
  juni.end_fill()


draw_traffic_light()
screen.update()
screen.tracer(1)

while True:
  if using == "if":
    juni.pu()
    juni.goto(10, 200)
    juni.pd()

    juni.color("black")

    juni.write("Is the color red?", font=("arial", 20, "normal"))
    time.sleep(1)
    if color == "red":
      juni.write("Is the color red? Yes", font=("arial", 20, "normal"))
    else:
      juni.write("Is the color red? No", font=("arial", 20, "normal"))

    juni.pu()
    juni.goto(10, 50)
    juni.pd()

    juni.write("Is the color yellow?", font=("arial", 20, "normal"))
    time.sleep(1)
    if color == "yellow":
      juni.write("Is the color yellow? Yes", font=("arial", 20, "normal"))
    else:
      juni.write("Is the color yellow? No", font=("arial", 20, "normal"))

    juni.pu()
    juni.goto(10, -100)
    juni.pd()

    juni.write("Is the color green?", font=("arial", 20, "normal"))
    time.sleep(1)
    if color == "green":
      juni.write("Is the color green? Yes", font=("arial", 20, "normal"))
    else:
      juni.write("Is the color green? No", font=("arial", 20, "normal"))

    break
  elif using == "elif":
    juni.pu()
    juni.goto(10, 200)
    juni.pd()

    juni.color("black")

    juni.write("Is the color red?", font=("arial", 20, "normal"))
    time.sleep(1)
    if color == "red":
      juni.write("Is the color red? Yes", font=("arial", 20, "normal"))
      break
    else:
      juni.write("Is the color red? No", font=("arial", 20, "normal"))

    juni.pu()
    juni.goto(10, 50)
    juni.pd()

    juni.write("Is the color yellow?", font=("arial", 20, "normal"))
    time.sleep(1)
    if color == "yellow":
      juni.write("Is the color yellow? Yes", font=("arial", 20, "normal"))
      break
    else:
      juni.write("Is the color yellow? No", font=("arial", 20, "normal"))

    juni.pu()
    juni.goto(10, -100)
    juni.pd()

    juni.write("The color must be green", font=("arial", 20, "normal"))
    time.sleep(1)
    break

screen.mainloop()
