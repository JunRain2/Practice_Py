from tkinter import *

def change_img():
    path = inputBox.get()
    img = PhotoImage(file = path)
    imageLabel.configure(image = img)
    imageLabel.image = img

window = Tk()

photo = PhotoImage(file = "C:\\Practice-Python\\chap05\\03-back.gif")
imageLabel=Label(window, image=photo)#'label' 속성 'image='을 이용하여 레이블안에 이미지 표시.
imageLabel.pack()

inputBox=Entry(window)
inputBox.pack()

button = Button(window, text='Submit',command=change_img)
button.pack()

window.mainloop()