from random import randint
import turtle as t
t.penup()
t.goto(-300,300)
t.pendown()
for a in range(4):
    t.forward(600)
    t.right(90)

number_of_turtles = 25
steps_of_time_number = 500

x = [randint(-300,300) for e in range(number_of_turtles)]
y = [randint(-300,300) for f in range(number_of_turtles)]
pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
speedx = [randint(-300,300) for s in range(number_of_turtles)]
speedy = [randint(-300,300) for s in range(number_of_turtles)]
g=0

for unit in pool:
    unit.shapesize(0.5)
    unit.penup()
    unit.speed(300)
    unit.goto(x[g], y[g])
    g += 1
for i in range(steps_of_time_number):
    d = 0
    for unit in pool:
        if y[d]>300:
            speedy[d]=-speedy[d]
        if y[d]<-300:
            speedy[d]=-speedy[d]
        if x[d]>300:
            speedx[d]=-speedx[d]
        if x[d]<-300:
            speedx[d]=-speedx[d]
        
        x[d] += 0.02*speedx[d]
        y[d] += 0.02*speedy[d]
        unit.goto(x[d],y[d])
        d += 1
