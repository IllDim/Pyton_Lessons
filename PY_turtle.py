from turtle import *

def windows():
    color('yellow')
    begin_fill()
    for i in range(4):
        fd(15)
        lt(90)
    end_fill()

#windows()
penup()
goto(-170, -170)
pendown()
color('grey')
begin_fill()
for i in range(2):
    fd(100)
    lt(90)
    fd(200)
    lt(90)
end_fill()

for row in range(6):
    for column in range(2):
        penup()
        goto(-145 + column * 40, -145 + row * 30)
        print(xcor(), ycor())
        pendown()
        windows()
    # penup()
    # goto(-145 + row*20, -145 + row*30)
    # print(xcor(), ycor())
    # pendown()
    # windows()


# penup()
# goto(-145, -145)
# windows()
# pendown()
# penup()
# goto(-145, -115)
# windows()
# pendown()


mainloop()