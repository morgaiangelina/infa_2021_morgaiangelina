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
i=0
while i<3:
    circle(1,5)
    circle(2,5)
    turtle.right(60)
    i+=1
