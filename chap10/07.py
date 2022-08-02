from email import message
from tkinter import *

mycolor = "black"

def paint(event):#event 매개 변수를 이용하여 마우스의 현재 위치를 알 수 있다.
    x1, y1= (event.x-1), (event.y+1)
    x2, y2 = (event.x-1), (event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill = mycolor)
    
def change_color():
    global mycolor
    mycolor = "red"

def change_color1():
    global mycolor
    mycolor = "green"
    
def change_color2():
    global mycolor
    mycolor = "yellow"


window = Tk()
canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)#<B1-Motion>은 마우스의 첫번째 버튼을 누를 때마다 발생하는 이벤트이다.
button = Button(window, text="빨간색", command = change_color)
button1 = Button(window, text="초록색", command = change_color1)
button2 = Button(window, text="노란색", command = change_color2)
button.pack()
button1.pack()
button2.pack()
window.mainloop()

#canvas = Canvas(window,width=300,height=200)#Canvas()그림을 그리는 위젯.
#canvas.create_oval(x0,y0,x1,y1,option,....)//(x0,y0)와 (x1,y1)에서 정의되는 타원 생성.

