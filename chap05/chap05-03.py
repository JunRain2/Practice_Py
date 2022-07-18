import imp


import random
import turtle
t= turtle.Turtle()

screen = turtle.Screen()
image1 = "C:\\Practice-Python\\chap05\\03-back.gif"
image2 = "C:\\Practice-Python\\chap05\\03-front.gif"
screen.addshape(image1)
screen.addshape(image2) #이미지를 추가


print("동전던지기 게임을 시작합니다.")
coin = random.randrange(2) #0~1에 숫자를 랜덤으로 출력
if coin == 0:
    t.shape(image2)
    t.stamp()
else:  
    t.shape(image1)
    t.stamp()

turtle.exitonclick()