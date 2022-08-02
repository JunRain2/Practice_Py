from tkinter import *

def process():
    tmeperature = float(e1.get())
    mytmp = (tmeperature-32)/1.8
    e2.insert(0,str(mytmp))

def process2():
    tmeperature = float(e2.get())#get함수를 통해 entry에 입력받은 데이터를 불러옴.
    mytmp = (tmeperature*1.8)+32
    e1.insert(0,str(mytmp))#엔트리 위젯의 0번째 위치에 mytmp 출력.
    
#button.configure(font= ~~)로 폰트 변경가능
    

window = Tk()

l1 = Label(window, text="화씨",font='helvetica 16 italic')#'font='으로 글씨폰트 변경
l2 = Label(window, text="섭씨",font='helvetica 16 italic')
l1.grid(row = 0,column= 0)#grid(row =, column = ) 격자 배치 관리자.//place함수는 절대 배치 관리자이다.
l2.grid(row = 1,column = 0)

e1 = Entry(window,bg="yellow",fg="white")#bg로 배경, fg로 전경의 색을 변경
e2 = Entry(window,bg="yellow",fg="white")
e1.grid(row = 0,column = 1)
e2.grid(row = 1,column = 1)

b1 = Button(window,text="화씨 -> 섭씨",command= process)
b1.grid(row = 2,column = 0)
b2 = Button(window,text="섭씨 -> 화씨",command= process2)
b2.grid(row = 2,column = 1)

window.mainloop()