import turtle
turtle.shape('turtle')
def circle(x,y):
    a=0
    turtle.begin_fill()
    while a < 360:
        turtle.forward(x)
        turtle.right(4)
        a += 4
    turtle.color(y)
    turtle.end_fill()
    turtle.color('black')

def halfc(R):
    a=0
    while a < 180:
        turtle.width(5)
        turtle.color('red')
        turtle.forward(R)
        turtle.right(4)
        a += 4
def move(a,b):
    turtle.penup()
    turtle.goto(a,b)
    turtle.pendown()
move(0, 0)
circle(5,'yellow')
move(20, -30)
circle(0.4,'blue')
move(-20, -30)
circle(0.4,'blue')
move(0,-50)
turtle.right(90)
turtle.width(5)
turtle.forward(20)
move(30,-90)
halfc(2)
turtle.color('black')
