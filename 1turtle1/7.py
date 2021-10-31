import turtle
import math
turtle.shape('turtle')
a = 0
while a < 10:
    turtle.right(4*math.atan(a))
    turtle.forward(math.sqrt(0.1+(a)**2))
    a += 0.02
