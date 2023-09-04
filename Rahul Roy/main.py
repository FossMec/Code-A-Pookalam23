import turtle as t
import colorsys as cs
t.bgcolor('black')
t.pensize(4)
t.tracer(20)
h = 0
t.up()
t.goto(40, -10)
t.down()

for i in range(360):
    c  = cs.hsv_to_rgb(h,1,1)
    t.color(c)
    t.fillcolor('black')
    t.up()
    t.circle(i, 60)
    t.down()
    t.begin_fill()
    t.circle(45, 145)
    t.left(80)
    t.circle(-40,145)
    t.end_fill()
    h += 0.005

t.done()
