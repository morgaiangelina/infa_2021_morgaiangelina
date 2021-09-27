import turtle
turtle.shape('turtle')
from random import *
for i in range(80):
    turtle.forward(randint(1,50))
    b=random()
    if b>=0.5:
        turtle.left(randint(1,360))
    else:
        turtle.right(randint(1,360))

