import turtle
import random
import math

player = turtle.Turtle()
player.left(90)
player.color("blue")
player.shape("turtle")
player.up()
player.speed(0)
screen = player.getscreen()

asteroid = []
for i in range(10):  
    a1 = turtle.Turtle()
    a1.color("red")
    a1.shape("circle")
    a1.up()
    a1.speed(0)
    a1.goto(random.randint(-300,300), random.randint(-300,300))
    asteroid.append(a1)

def turnleft():
    player.left(30)

def turnright():
    player.right(30)
    
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

def play():
    player.forward(2)
    for a in asteroid : 
        a.right(random.randint(-90,90))
        a.forward(2)
    screen.ontimer(play, 10)#10ms가 지나면 play()를 다시 호출
screen.ontimer(play,10)#ontimer 주어진 시간이 지나면 함수를 호출

turtle.mainloop()