import turtle
t= turtle.Turtle()

def draw_olympic_symbol():
    position=[[0,0,"blue"],[-120,0,"purple"],[60,60,"red"],[-60,60,"yellow"],[-180,60,"green"]]
    for x, y, c in position:#혼성리스트와 반복문의 좋은 예
        t.up()
        t.goto(x,y)
        t.color(c,c)
        t.down()
        t.begin_fill()
        t.circle(30)
        t.end_fill()
        
draw_olympic_symbol()
        