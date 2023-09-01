from turtle import * 
import math

tracer(0)
speed(0)
def draw_squash(rad,num_rows,len_row,num_peaces,colors):
  circle (rad)
  left(90)
  penup()
  initial = rad - (num_rows*len_row)
  forward(rad - initial)
  right(90)
  pendown()
  ang = 360 / num_peaces
  counter = 0
  right(90)
  for j in range(0,num_rows):
    # cur_peaces = int(2*(20+(10*j))*math.pi / prev_peace_length)
    for i in range(0,num_peaces):
        penup()
        fillcolor(colors[counter % len(colors)])
        begin_fill()
        left(90)
        circle(initial+(len_row*j),ang)
        right(90)
        forward(len_row)
        right(90)
        circle(-(initial+len_row+(len_row*j)),ang)
        right(90)
        forward(len_row)
        right(90)
        circle(initial+(len_row*j),ang)
        right(90)
        end_fill()
        counter += 1
    forward(len_row)

rad = 300
num_rows = 8
len_row = 10
num_peaces = 35
colors = ["#536F3D","#5B0B16","#D6325C","#F06D0A",'#FACA27','#EDE9DE']

draw_squash(rad,num_rows,len_row,num_peaces,colors)

mainloop()