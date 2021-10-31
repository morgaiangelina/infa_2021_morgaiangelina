import turtle
turtle.shape('turtle')
def star(n):
    a=0
    while a < n:
        turtle.forward(100)
        turtle.left(180*(n-1)/n)
        a += 1
star(5)
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
star(11)
