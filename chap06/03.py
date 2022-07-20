import math
import turtle


t = turtle.Turtle()
t.shape("turtle")
t.color('red','yellow')

for degree in range(361):
    radian = 3.14 * degree/180.0
    t.goto(degree ,math.sin(radian)*200) #모듈에 내장된 함수를 사용하기 위해서는 "module.함수"와 같은 형식으로 사용.
 
turtle.exitonclick()