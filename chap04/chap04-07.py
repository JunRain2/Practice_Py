color = []
color.append(input("색상 #1을 입력하시오 : "))
color.append(input("색상 #2을 입력하시오 : "))
color.append(input("색상 #3을 입력하시오 : "))

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.fillcolor(color[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100,0)
t.down()

t.fillcolor(color[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200,0)
t.down()

t.fillcolor(color[2])
t.begin_fill()
t.circle(50)
t.end_fill()