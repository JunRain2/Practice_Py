from tkinter import *

window = Tk()

l1 = Label(window, text="화씨")#Lable : 텍스트나 이미지를 표시한다.
l2 = Label(window, text="섭씨")
#l2['text'] = "새로운 텍스트" //실행 도중에 레이블의 텍스트를 변경함.
l1.pack()
l2.pack()

e1 = Entry(window)#Entry: 한줄의 텍스트를 입력받는 필드/ 변수로 window를 준 이유는 window가 가르키는 최상위 윈도우 안에 엔트리 위젯을 생성하라는 의미이다.
e2 = Entry(window)
e1.pack()
e2.pack()

b1 = Button(window,text="화씨 -> 섭씨")
b1.pack()
b2 = Button(window,text="섭씨 -> 화씨")
b2.pack()

window.mainloop()