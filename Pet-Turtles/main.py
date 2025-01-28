import turtle
import random

names = []
numPets = int(input("How many pet turtles are there?") )
for i in range(numPets): 
  name = input("Enter pet turtle #" + str(i + 1) + "'s name: ")
  names.append(name)

for name in names: 
  t = turtle.Turtle()
  t.shape("turtle")
  t.penup()
  t.goto(random.randint(-100,100), random.randint(-100,100))

  randomAge = random.randint(1,100)
  t.write("     " + str(name) + ": your pet turtle is " + str(randomAge) + " years old!", font=("Arial", 12, "normal"))