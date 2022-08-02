from tkinter import *

window = Tk()

w=Label(window, text="박스 #1", bg = 'red',fg='white')
w.place(x=0,y=0)#.place(x=,y=), 절대 위치 배치 관리자는 절대위치를 사용하여 위젯을 배치
w=Label(window, text="박스 #2",bg='green',fg='black')
w.place(x=20,y=20)
w=Label(window, text="박스 #3", bg='blue', fg='white')
w.place(x=40,y=40)

window.mainloop()