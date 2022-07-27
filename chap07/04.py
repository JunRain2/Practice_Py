import turtle

def graph(size):
    t.begin_fill()
    t.left(90)
    t.forward(size)
    t.write(str(size),font=('Ti,es New Roman', 16, 'bold'))
    t.right(90)
    
    t.forward(40)
    t.right(90)
    t.forward(size)
    t.left(90)
    t.end_fill()
    
t=turtle.Turtle()
t.shape("turtle")

data = [120,56,309,220,156,23,98]
t.color("blue")
t.fillcolor("red")

t.pensize(3)

for d in data:
    graph(d)