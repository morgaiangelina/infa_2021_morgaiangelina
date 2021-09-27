import turtle as t
t.shape('turtle')
t.penup()
t.goto(-100,0)
t.pendown()
x = -100
y = 0
V = 40
U = 40
g = -20
T = 0.01
b = 0
while b<6:
    a = V
    while V>=-a:
        x += U*T
        y += V*T + g*T**2/2
        t.goto(x,y)
        V += g*T
    V=-0.8*V
    b += 1
