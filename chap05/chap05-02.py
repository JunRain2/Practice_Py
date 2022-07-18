import turtle
t=turtle.Turtle()
t.shape("turtle")
t.shapesize(3,3)

while True:
    order = input("명령을 입력하시오")
    if order == "l":
        t.left(90)
        t.forward(100)
    if order == "r":
        t.right(90)
        t.forward(100)
        
