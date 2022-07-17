x = []
y = []

x.append(int(input("x1 : ")))
y.append(int(input("y1 : ")))
x.append(int(input("x2 : ")))
y.append(int(input("y2 : ")))
x.append(int(input("x3 : ")))
y.append(int(input("y3 : ")))

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.goto(x[0],y[0])
t.goto(x[1],y[1])
t.goto(x[2],y[2])