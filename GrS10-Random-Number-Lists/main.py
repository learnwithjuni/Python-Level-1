import turtle
import random

t = turtle.Turtle()
l = []

for i in range(15):
  l.append(random.randint(0,10))

t.penup()
t.goto(-100, 0)

for num in l:
  t.write(num)
  t.forward(20)

t.goto(-100, -30)
for i in range(len(l)):
  l[i] += 10

for num in l:
  t.write(num)
  t.forward(20)

t.goto(-100, -60)
for i in range(len(l)):
  l[i] *= 10

for num in l:
  t.write(num)
  t.forward(20)

'''
For students who are very comfortable with lists, they should also understand solutions like:

for i in range(len(l)):
   l[i] += 10
   t.write(l[i])
   t.forward(20)
'''