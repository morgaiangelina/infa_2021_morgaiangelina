import turtle
turtle.shape('turtle')
def halfc(R):
    a=0
    while a < 180:
        turtle.forward(R)
        turtle.right(4)
        a += 4
turtle.left(90)
i=0
while i<4:
    halfc(5)
    halfc(1)
    i+=1
