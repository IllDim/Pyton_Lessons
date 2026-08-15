from turtle import *
from time import sleep
from random import randint

def catch1(x, y):
    t1.penup()
    t1.goto(randint(-w, h), randint(-w, h))
    t1.pendown()
    t1.lt(randint(0, 180))

def catch2(x, y):
    t2.penup()
    t2.goto(randint(-w, h), randint(-w, h))
    t2.pendown()
    t2.lt(randint(0, 180))

def catch3(x, y):
    t3.penup()
    t3.goto(randint(-w, h), randint(-w, h))
    t3.pendown()
    t3.lt(randint(0, 180))

def gameFinished(t1, t2, t3):
    t1_outside = (abs(t1.xcor())> w or abs(t1.ycor()) > h
                  or abs(t2.xcor()) > w or abs(t2.ycor()) > h
                  or abs(t3.xcor()) > w or abs(t3.ycor()) > h)
    return t1_outside

w = 300
h = 300

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

t1 = Turtle()
t1.color('yellow')
t1.shape('turtle')
t1.width(5)
t1.speed(0.3)

t2 = Turtle()
t2.color('red')
t2.shape('turtle')
t2.lt(120)
t2.width(5)
t2.speed(0.3)

t3 = Turtle()
t3.color('blue')
t3.shape('turtle')
t3.lt(240)
t3.width(5)
t3.speed(0.3)

t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

while not gameFinished(t1, t2, t3):
    t1.fd(7)
    t2.fd(7)
    t3.fd(7)
    sleep(0.4)

penup()
goto(-50, 0)
t1.clear()
t2.clear()
t3.clear()
write('Игра закончена', font = ("Times New Roman", 24, 'bold'))
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

mainloop()
