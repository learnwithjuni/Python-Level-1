# needs work -> kind of hacky with no timer module.
# juni playground version: https://app.junilearning.com/teacher/playground/project?projectId=65b13e46abd839001fba6bb8&projectName=WhackaMole&projectType=pythonTurtle&viewState=0

import turtle
import random

# Function to create a mole at a random position
def create_mole():
    mole.penup()
    mole.hideturtle()
    mole.shape("circle")
    mole.color("brown")
    x = random.randint(-180, 180)
    y = random.randint(-180, 180)
    mole.goto(x, y)
    mole.showturtle()

# Function to handle a click on the mole
def mole_clicked(x, y):
    global score
    if abs(mole.xcor() - x) < 20 and abs(mole.ycor() - y) < 20:
      score += 1
      update_score()
      mole.hideturtle()
      create_mole()

# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write("Score: {}".format(score), align="center", font=("Arial", 16, "normal"))

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")

# Create the player turtle
player = turtle.Turtle()
player.penup()
player.hideturtle()
player.shape("turtle")
player.color("blue")

# Create the mole turtle
mole = turtle.Turtle()
create_mole()

# Create a turtle to waste time
timer = turtle.Turtle()
timer.penup()
timer.ht()

# Create the score and score display turtle
score = 0
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.color("black")
score_display.goto(0, 180)
update_score()

# Set up the click event
screen.onclick(mole_clicked)


# Main game loop
while score < 10:
    timer.forward(500)
    create_mole()
    #screen.update()

# Display "Game Over" when the loop ends
score_display.clear()
score_display.write("Game Over", align="center", font=("Arial", 16, "normal"))

#Keep the window open - this line is only needed for Replit implementations
turtle.mainloop()