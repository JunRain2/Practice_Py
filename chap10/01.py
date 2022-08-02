from tkinter import *#thinker 모듈에 있는 모든 함수를 포함시키라는 의미.(from을 통해 '모듈.함수'에서 '모듈.' 생략가능)


window = Tk()#최상위 윈도우 생성
button = Button(window, text="클릭하세요")#버튼 위젯 생성 첫번째 매개 변수로 최상위 윈도우 객체 window가 전달, 두번째 매개 변수로 버튼에 표시되는 텍스트가 전달
button.pack()#pack()은 버튼을 최대한 압축하여 윈도우에 표시하라는 의미, pack()함수를 호출하지 않으면 화면에 버튼이 나타나지 않는다.

window.mainloop()#윈도우에서 발생하는 여러가지 이벤트를 처리하는 함수