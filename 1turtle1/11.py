import turtle
turtle.shape('turtle')
def circle(rl,R):
    a=0
    while a < 360:
        turtle.forward(R)
        if rl==1:
            turtle.right(4)
        else:
            turtle.left(4)
        a += 4
turtle.right(90)
def twoc(x):
    circle(2, x)
    circle(1, x)
i=2
while i<8:
    twoc(i)
    i+=1


