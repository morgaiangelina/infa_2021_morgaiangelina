x = 0
y = 30
import turtle
turtle.shape('turtle')
while x<10:
    a = 0
    while a < 4:
        turtle.forward(y)
        turtle.left(90)
        a += 1
    a=0
    x += 1
    turtle.penup()
    turtle.goto(-15*x, -15*x)
    turtle.pendown()
    y += 30

