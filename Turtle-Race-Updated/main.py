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

# race the turtles until at least one of them reaches the finish line at x = 100
while t1.xcor() < 100 and t2.xcor() < 100 and t3.xcor() < 100:
  t1.forward(random.randint(1,5))
  t2.forward(random.randint(1,5))
  t3.forward(random.randint(1,5))

# check who won or tied
if t1.xcor() > t2.xcor() and t1.xcor() > t3.xcor():
  t1.write("I win!", font=("Arial", 16, "normal"))
if t2.xcor() > t1.xcor() and t2.xcor() > t3.xcor():
  t2.write("I win!", font=("Arial", 16, "normal"))
if t3.xcor() > t1.xcor() and t3.xcor() > t2.xcor():
  t3.write("I win!", font=("Arial", 16, "normal"))
if t1.xcor() == t2.xcor() and t2.xcor() == t3.xcor():
  t1.write("Tie!", font=("Arial", 16, "normal"))
  t2.write("Tie!", font=("Arial", 16, "normal"))
  t3.write("Tie!", font=("Arial", 16, "normal"))
if t1.xcor() == t2.xcor():
  t1.write("Tie!", font=("Arial", 16, "normal"))
  t2.write("Tie!", font=("Arial", 16, "normal"))
if t1.xcor() == t3.xcor():
  t1.write("Tie!", font=("Arial", 16, "normal"))
  t3.write("Tie!", font=("Arial", 16, "normal"))
if t2.xcor() == t3.xcor():
  t2.write("Tie!", font=("Arial", 16, "normal"))
  t3.write("Tie!", font=("Arial", 16, "normal"))

# Keep the window open (this is only needed if running in replit)
turtle.mainloop()