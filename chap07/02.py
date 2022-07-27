import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length = 50):
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawit(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()
    
s = turtle.Screen()#그림이 그려지는 화면을 얻는다
s.onscreenclick(drawit)# 마우스 클릭 이벤트 처리 함수를 등록한다.
