import turtle
import random

# draw starting lines
laneDrawer = turtle.Turtle()
laneDrawer.right(90)
laneDrawer.speed(1000)
for i in range(15):
  laneDrawer.penup()
  laneDrawer.goto(-200+20*i, 100)
  laneDrawer.write(i)
  laneDrawer.pendown()
  laneDrawer.forward(100)
# draw finish line
laneDrawer.penup()
laneDrawer.goto(-200+20*(i+1), 100)
laneDrawer.write("Finish")
laneDrawer.pendown()
laneDrawer.forward(100)
laneDrawer.ht()

# set up the race turtles
t1 = turtle.Turtle()
t1.penup()
t1.color("red")
t1.shape("turtle")
t1.goto(-200, 80)
t1.pendown()

t2 = turtle.Turtle()
t2.penup()
t2.color("blue")
t2.shape("turtle")
t2.goto(-200, 50)
t2.pendown()

t3 = turtle.Turtle()
t3.penup()
t3.color("orange")
t3.shape("turtle")
t3.goto(-200, 20)
t3.pendown()

# YOUR CODE HERE 
