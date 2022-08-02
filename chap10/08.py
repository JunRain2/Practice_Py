from tkinter import *

def click(key):
    if key == "=":
        result = eval(display.get())#eval()함수는 문자열로 된 수식을 전달하면 이것을 해석하여서 계산결과를 출력//eval("2+3") = 5
        s= str(result)
        display.insert(END, "=" + s)#엔트리의 끝에 문자열을 추가.
    else:
        display.insert(END, key) 

window = Tk()
window.title("My Calculate")#창의 이름을 설정
display = Entry(window, width=33, bg="yellow")
display.grid(row = 0, column=0, columnspan=5)#columnspan=5의 의미는 0행의 5개셀을 합치라는 의미.

button_list = ['7','8','9','/','C'
               ,'4','5','6','*',' '
               ,'1','2','3','-',' '
               ,'0', '.','=','+',' ']

row_index = 1
col_index = 0
for button_text in button_list:
    def process(t=button_text):
        click(t)#파이썬은 click()와 같이 써있을 경우 바로실행 따라서 command = click과 같이 괄호를 빼고 작성해야지 특정 상황에 실행.
    Button(window, text=button_text, width=5, command= process).grid(row=row_index, column=col_index)#click이 바로 실행되는것을 막고자 따로 process함수를 생성.
    col_index+=1
    if col_index > 4:
        row_index += 1
        col_index = 0

       

window.mainloop()