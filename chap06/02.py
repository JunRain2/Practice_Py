import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(10):
   x=random.randint(1,100)
   y=random.randint(1,100)
   size=random.randint(1,100)
   
   t.up()
   t.goto(x,y)
   t.down()
   t.circle(size)
    