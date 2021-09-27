import turtle
import math
turtle.shape('turtle')
def pol(a,n):
    turtle.penup()
    turtle.goto(a/(2*math.sin((math.pi)/n)),0)
    turtle.pendown()
    turtle.left(90*(1+2/n))
    b = 0
    while b < n:
        turtle.forward(a)
        turtle.left(360/n)
        b += 1
    turtle.right(90*(n+2)/n)
x=30
y=3
while y<13:
    pol(x, y)
    x += 10
    y += 1
