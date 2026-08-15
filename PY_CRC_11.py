from turtle import *

colormode(255)
#shape('turtle')
color((117, 2, 84), (238, 242, 22))

pensize(4)
speed(0.5)

#1
# r = 191
# g = 33
# b = 142
#
# for i in range(60, 10, -20):
#     fillcolor(r, g, b)
#
#     begin_fill()
#
#     circle(i)
#     end_fill()
#
#     r += 27
#     b -= 55
#     g += 96
#
#     penup()
#
#     goto(i*5 -120, 0)
#     pendown()

#2
# r = 191
# g = 33
# b = 142
#
# #прямоугольник
# begin_fill()
# fillcolor(r, g, b)
# for i in range(4):
#     if i == 0 or i == 2:
#         fd(100)
#         lt(90)
#     else:
#         fd(140)
#         lt(90)
# end_fill()
#
# penup()
# goto(-170, 0)
# pendown()
#
# r += 50
# g += 40
# b += 30
#
# begin_fill()
# fillcolor(r, g, b)
# # Трапеция
# fd(150)   # нижнее основание
# lt(120)      # угол 60 градусов
# fd(70)    # боковая сторона
# lt(60)       # угол 60 градусов
# fd(80)    # верхнее основание
# lt(60)      # угол 60 градусов
# fd(70)    # боковая сторона
#
# end_fill()
#
# penup()
# goto(-200, 175)
# pendown()
#
# r -= 30
# g += 40
# b += 30
#
# begin_fill()
# fillcolor(r, g, b)
#
# for _ in range(2):
#     fd(100)
#     lt(60)
#     fd(100)
#     lt(120)
#
# end_fill()

#3
# fillcolor('green')
# pos = 0
# for i in range(3):
#     pendown()
#     begin_fill()
#     for _ in range (3):
#         penup()
#         fd(100)
#         lt(120)
#         pendown()
#     end_fill()
#     penup()
#     goto(0, pos := pos - 50)
#     pendown()
#
#
# #рисуем ствол
# penup()
# goto(35, -140)
# #goto(-15, -50)
# pendown()
# fillcolor("brown")
# begin_fill()
# for _ in range(2):
#     penup()
#     fd(30)
#     lt(90)
#     fd(40)
#     lt(90)
#     pendown()
# end_fill()

#4
# pos =0
# color("green")
# for _ in range(3):
#     for _ in range(4):
#         fd(30)
#         lt(90)
#     penup()
#     goto(pos := pos - 60 , 0)
#     pendown()

#5
#Задача не имеет решения. Она абсурдна)

#6
# pensize(5)
# for r in range(40, 0, -10):
#   for i in range(6):
#     color(255, 165, r * 6)
#     fillcolor(162, r * 6, 255)
#     begin_fill()
#     circle(r)
#     end_fill()
#     rt(60)

#7
# pensize(5)
# for r in range(40, 0, -10):
#   for i in range(6):
#     color(255, 165, r * 6)
#     fillcolor(162, r * 6, 255)
#     begin_fill()
#     for _ in range(4):
#         fd(r)
#         lt(90)
#     end_fill()
#     rt(60)

#8
pensize(5)
for r in range(40, 0, -10):
  for i in range(6):
    color(255, 165, r * 6)
    fillcolor(162, r * 6, 255)
    begin_fill()
    for _ in range(3):
        fd(r)
        lt(120)
    end_fill()
    rt(60)

mainloop()