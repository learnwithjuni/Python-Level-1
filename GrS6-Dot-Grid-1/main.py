

import turtle

score=0
laps=0

ttrack=turtle.Turtle()
btrack=turtle.Turtle()
ri=turtle.Turtle()
le=turtle.Turtle()
t=turtle.Turtle()
w=turtle.Turtle()
e=turtle.Turtle()
l=turtle.Turtle()
w.speed(0)
e.speed(0)
ri.speed(0)
le.speed(0)
l.speed(0)
ttrack.speed(0)
btrack.speed(0)
t.speed(0)
'''
right.shape("turn")
left.shape("turn")
right.penup()
right.goto(100,90)
left.penup()
left.goto(-170,90)
left.left(180)
ttrack=turtle.Turtle()
btrack=turtle.Turtle()
#e.speed(0)
'''
screen=turtle.Screen()

screen.bgcolor("green")
'''
screen.register_shape("turn", ((100, 0), (92, 31), (71, 71), (50, 87), (31, 92), (0, 100), (-31, 92), (-50, 87), (-71, 71), (-92, 31), (-100, 0), (-92, -31), (-71, -71), (-50, -87), (-31, -92), (0, -100), (31, -92), (50, -87), (71, -71), (92, -31)
))

screen.register_shape("turn", ( (150, 0), (141, 51), (115, 96), (75, 130), (26, 148), (-26, 148), (-75, 130), (-115, 96), (-141, 51), (-150, 0), (-75, 0), (-70, 26), (-57, 48), (-37, 65), (-13, 74), (13, 74), (38, 65), (57, 48), (70, 26), (75, 0)))
screen.register_shape("track", ((100,0), (100,75), (400,75), (400,0)))
btrack.shape("track")
btrack.penup()
btrack.goto(210,-60)
btrack.left(90)
ttrack.shape("track")
ttrack.penup()
ttrack.goto(210,162)
ttrack.left(90)
'''

#controls
def left():
  t.left(3)
def right():
  t.right(3)
def rright():
  w.right(3)
def lleft():
  w.left(3)
def forward():
  t.forward(3)
def speed():
  w.forward(3)
screen.register_shape("rect", ((-100,240), (-100,165), (-98,165), (-98,240)))
l.penup()
l.color("white")
l.speed(0)
l.shape("rect")
l.goto(0,280)
l.right(90)
screen.onkey(left,"left")
screen.onkey(right, "right")
screen.onkey(rright, "d")
screen.onkey(lleft,"a")
screen.onkey(forward, "up")
screen.onkey(speed, "w")
screen.listen()

#track
e.penup()
e.color('yellow')
e.goto(-60,0)
e.pendown()
screen.register_shape("turn", ((150, 0), (141, 51), (115, 96), (75, 130), (26, 148), (-26, 148), (-75, 130), (-115, 96), (-141, 51), (-150, 0), (-75, 0), (-70, 26), (-57, 48), (-37, 65), (-13, 74), (13, 74), (38, 65), (57, 48), (70, 26), (75, 0)))
ri.shape("turn")
le.shape("turn")
ri.penup()
ri.goto(80,0)
le.penup()
le.goto(-130,0)
le.left(180)

#e.speed(0)
screen=turtle.Screen()
screen.bgcolor("green")
screen.register_shape("track", ((100,0), (100,75), (400,75), (400,0)))
btrack.shape("track")
btrack.penup()
btrack.goto(210,-130)
btrack.left(90)
ttrack.shape("track")
ttrack.penup()
ttrack.goto(210,60)
ttrack.left(90)

#racers
w.shape("turtle")
t.shape("turtle")
t.color("blue")
w.color("red")
w.penup()
t.penup()
w.goto(-80,115)
t.goto(-80,85)
e.write("red laps"+str(score)+"   blue laps"+str(laps),font=("Arial",15,"normal"))
def isCollide(x,y):
  if abs(x-ttrack.xcor())<50 and abs(y-ttrack.ycor())<50:
    return True
  if abs(x-btrack.xcor())<50 and abs(y-btrack.ycor())<50:
    return True
  if abs(x-ri.xcor())<50 and abs(y-ri.ycor())<50:
    return True
  if abs(x-le.xcor())<50 and abs(y-le.ycor())<50:
    return True
  return False
print(ttrack.xcor())
print(ttrack.ycor())
print(btrack.xcor())
print(btrack.ycor())
while True:
  t.forward(1)
  w.forward(1)
  if laps==10:
    t.write("I win!")
    break
  if score==10:
    w.write("I win!")
    break
  if abs(w.xcor()-l.xcor())<10 and abs(w.ycor()-l.ycor())<=30:
    score=score+1
    e.clear()
    e.write("red laps"+str(score)+"   blue laps"+str(laps),font=("Arial",15,"normal"))
  if abs(t.xcor()-l.xcor())<10 and abs(t.xcor()-l.ycor())<=30:
    laps=laps+1
    e.clear()
    e.write("red laps"+str(score)+"   blue laps"+str(laps),font=("Arial",15,"normal"))
  if not isCollide(w.xcor(), w.ycor()):
    w.backward(5)
  if not isCollide(t.xcor(), t.ycor()):
    t.backward(5)
print(ttrack.xcor())
print(ttrack.ycor())
print(btrack.xcor())
print(btrack.ycor())



'''
  if abs(w.xcor() - ttrack.xcor()) > 100 and abs(w.ycor() - ttrack.ycor()) > 10:  
    w.backward(20)  
  if abs(w.xcor() - btrack.xcor()) > 100 and abs(w.ycor() - btrack.ycor()) > 10:  
    w.backward(20) 
  if abs(w.xcor() - ri.xcor()) > 10 and abs(w.ycor() - ri.ycor()) > 10:  
    w.backward(20)  
  if abs(w.xcor() - le.xcor()) > 10 and abs(w.ycor() - le.ycor()) > 10:  
    w.backward(20)
  if abs(t.xcor() - ttrack.xcor()) > 100 and abs(t.ycor() - ttrack.ycor()) > 60:  
    t.backward(20)
  if abs(t.xcor() - btrack.xcor()) > 100 and abs(t.ycor() - btrack.ycor()) > 60:  
    t.backward(20)
  if abs(t.xcor() - ri.xcor()) > 10 and abs(t.ycor() - ri.ycor()) > 10:  
    t.backward(20)  
  if abs(t.xcor() - le.xcor()) > 10 and abs(w.ycor() - le.ycor()) > 10:
    t.backward(20)  
    '''