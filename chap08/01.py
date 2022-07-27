import turtle
import random
t1=turtle.Turtle()
t2=turtle.Turtle()

t1.shape("turtle")
t1.color("pink")
t1.shapesize(5)
t1.pensize(5)
t1.up()
t1.goto(-400,0)
t1.down()

t2.shape("turtle")
t2.color("blue")
t2.shapesize(5)
t2.pensize(5)
t2.up()
t2.goto(-400,-100)
t2.down()

for i in range(100):
    d1 = random.randint(1,60)#1~60난수 생성
    t1.forward(d1)
    d2 = random.randint(1,60)#1~60난수 생성
    t2.forward(d2)