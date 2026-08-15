from turtle import *
from time import sleep
from random import randint

def catch1(x, y):
    t1.penup()
    t1.goto(randint(-w, h), randint(-w, h))
    t1.pendown()
    t1.lt(randint(0, 180))

def gameFinished(t1):
    t1_outside = abs(t1.xcor())> w or abs(t1.ycor()) > h
    return t1_outside

w = 300
h = 300

t1 = Turtle()
t1.color('red')
t1.shape('turtle')
t1.width(5)
#t1.speed(0.3)

t1.onclick(catch1)

#t2 = Turtle()
penup()
goto(-w, -h)
pendown()
color('black')
fillcolor('green')
begin_fill()
for _ in range(4):
    fd(w * 2)
    lt(90)
end_fill()


while not gameFinished(t1):
    t1.fd(7)
    #sleep(0.3)

#t1.shapesize(0)
t1.penup()
t1.goto(-50, 0)
t1.clear()
t1.write('Игра закончена', font = ("Times New Roman", 24, 'bold'))
t1.hideturtle()

# while True:
#     t1.fd(7)
#     sleep(0.3)
#     if abs(t1.xcor()) > 300 or abs(t1.ycor()) > 300:
#         break

mainloop()