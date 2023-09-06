import turtle
from turtle import *
import math

bgcolor("pale turquoise")
speed(1000)

#circle
def circ(len,clr):
    penup()
    home()
    goto(0, -(len+50))
    pendown()
    color(clr)
    begin_fill()
    circle(len)
    end_fill()

#outer circle
circ(300,"#3d0706")

#triangular pattern
home()
goto(0, -50)
def tripatt(len,clr):
    color(clr)
    for i in range(36):
        begin_fill()
        forward(len / math.tan(math.pi / 3.6))
        left(130)
        forward(len / math.sin(math.pi / 3.6))
        left(100)
        forward(len / math.sin(math.pi / 3.6))
        left(130)
        forward(len / math.tan(math.pi / 3.6))
        end_fill()
        left(10)
    left(5)

#outer patterns
tripatt(300,"#cf342b")
tripatt(271, "#f5700a")
tripatt(246,"#fcd349")
tripatt(223,"#ffeeb5")


#middle circle
circ(200,"#014504")

#square pattern
def sqpatt(len,clr):
    penup()
    home()
    goto(0,-50)
    left(45)
    pendown()
    color(clr)
    for i in range(18):
        begin_fill()
        for i in range(4):
            forward(len * math.sqrt(2))
            left(90)
        end_fill()
        penup()
        left(20)
        pendown()

#inner patterns
sqpatt(100,"white")
sqpatt(82,"#3d0706")
sqpatt(70,"#ba3035")

#line patterns
home()
goto(0,-50)
pensize(10)
color("#ba3035")
for i in range(18):
    forward(196)
    backward(196)
    left(20)

#inner circle
circ(110,"#021322")

#FOSS mec
#foss F
penup()
home()
goto(-100,-85)
left(80)
pendown()
pensize(1)
begin_fill()
color("#F7B744")
forward(80)
right(80)
forward(120)
right(100)
forward(10)
right(80)
forward(110)
left(80)
forward(20)
left(100)
forward(17)
right(100)
forward(7)
right(80)
forward(17)
left(80)
forward(43)
right(80)
forward(10)
end_fill()

#foss O
penup()
backward(32)
right(100)
pendown()
begin_fill()
forward(50)
right(80)
forward(27)
right(100)
forward(50)
right(80)
forward(27)
end_fill()

penup()
backward(10)
right(100)
forward(10)
pendown()
color("#021322")
begin_fill()
forward(30)
right(80)
forward(10)
right(100)
forward(30)
right(80)
forward(10)
end_fill()

#foss S
def fos(dw,bk):
    penup()
    backward(bk)
    left(80)
    forward(dw)
    pendown()
    begin_fill()
    color("#F7B744")
    forward(8)
    left(100)
    forward(25)
    left(80)
    forward(29)
    left(100)
    forward(17)
    right(100)
    forward(13)
    right(80)
    forward(17)
    left(80)
    forward(8)
    left(100)
    forward(25)
    left(80)
    forward(29)
    left(100)
    forward(17)
    right(100)
    forward(13)
    right(80)
    forward(17)
    end_fill()

#foss S1
fos(2,25)

#foss S2
fos(0,30)

#mec M
penup()
backward(35)
right(100)
backward(8)
pendown()
pensize(2)
color("light grey")
forward(29)
right(150)
forward(20)
left(120)
forward(24)
right(150)
forward(27)

#mec E
penup()
right(80)
backward(8)
pendown()
backward(15)
forward(15)
right(100)
forward(14)
right(80)
forward(10)
backward(10)
left(80)
forward(14)
right(80)
forward(15)

#mec C
penup()
forward(22)
pendown()
backward(15)
right(100)
forward(28)
left(100)
forward(15)

hideturtle()

#happy onam
penup()
goto(-145,300)
pendown()
color("navy")
write("Happy Onam!",font=("Times New Roman",50, "italic"))

#submitted by
color("#6c55ed")
penup()
goto(-100,-400)
pendown()
color("maroon")
write("- Akash Abraham",font=("Courier",20, "italic"))
penup()
goto(-20,-420)
pendown()
write("CS3A",font=("Courier",20, "italic"))


turtle.Screen().exitonclick()

#thankyou!