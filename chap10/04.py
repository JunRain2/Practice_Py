from tkinter import *

def process():
    print("안녕하세요")
    
window = Tk()
button = Button(window,text = "클릭하세요", command= process)#'command=' 를 추가, 버튼을 클릭시 지정된 함수 호출. 
button.pack()
window.mainloop()