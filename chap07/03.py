import turtle
t= turtle.Turtle()
t.shape("turtle")
t.left(90)

def tree():
    t.forward(100)
    t.back(50)
    t.left(60)
    t.forward(50)
    t.back(50)
    t.right(120)
    t.forward(50)

    
tree()