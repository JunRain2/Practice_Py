import turtle
t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(100,100)
t.down()
t.write("거북이가 여기로 오면 양수입니다.")

t.up()
t.goto(100,0)
t.down()
t.write("거북이가 여기로 오면 0 입니다.")

t.up()
t.goto(100,-100)
t.down()
t.write("거북이가 여기로 오면 음수입니다.")

t.up()
t.goto(0,0)
t.down()

num = int(turtle.textinput("","숫자를 입력하시오 : "))

if num > 0 :
    t.goto(100,100)
if num == 0 :
    t.goto(100,0)
if num < 0 :
    t.goto(100,-100)

