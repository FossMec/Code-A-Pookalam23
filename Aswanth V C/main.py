from turtle import * 
import math

def reset_position(x=0,y=0):
   setheading(0)
   goto(x,y)

def draw_squash(rad,num_rows,len_row,num_peaces,colors):
  # circle (rad)
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
  return rad - initial

def draw_circular(rad,rad_len,sub_circle_count=3,colors=['red','green','blue'],num_peaces = 20,pen_down = True):
  x,y = pos()
  penup()
  vis_len = rad_len * 1
  second_rad_diff = rad_len / sub_circle_count
  ruler_circle_rad = rad - rad_len * 2
  ruler_ang = 360 / num_peaces
  circle(rad)
  for j in range(0,int(num_peaces)):
    # circle(rad_len)
    for i in range(0,sub_circle_count):
      # Draw the circles normally
      left(90)
      forward((second_rad_diff if i != 0 else 0 ))
      right(90)
      fillcolor(colors[i % len(colors)])
      begin_fill()
      if pen_down:pendown()
      circle(rad_len - (second_rad_diff * i))
      penup()
      end_fill()
    right(90)
    forward(rad_len-second_rad_diff)
    left(90)
    circle(rad,ruler_ang) # change the angle of circle
  # reset to normal position
  reset_position(x,y)
  left(180)
  # redraw the overflowing part at the end
  fillcolor(colors[0])
  begin_fill()
  if pen_down:pendown()
  circle(-rad_len,180) # first round
  right(90)
  penup()
  forward(second_rad_diff)
  right(90)
  if pen_down:pendown()
  circle((rad_len - second_rad_diff),180) # first round
  end_fill()
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  fillcolor(colors[1])
  begin_fill()
  if pen_down:pendown()
  circle(-(rad_len - (second_rad_diff * 2)),180) # second round
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  if pen_down:pendown()
  circle(rad_len-second_rad_diff,180) # second round
  end_fill()
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  fillcolor(colors[2])
  begin_fill()
  if pen_down:pendown()
  circle(-(rad_len - (second_rad_diff * 2)),180) # third half round
  end_fill()
  penup()
  reset_position(x,y)
  circle(rad,ruler_ang) # redraw the second circle overflowed part
  left(180)
  fillcolor(colors[0])
  begin_fill()
  if pen_down:pendown()
  circle(-rad_len,180) # first round, second
  right(90)
  penup()
  forward(second_rad_diff)
  right(90)
  if pen_down:pendown()
  circle(rad_len - second_rad_diff,180) # first round, second 
  end_fill()
  penup()
  reset_position(x,y+rad_len)
  fillcolor('#2A3B1A')
  begin_fill()
  circle(rad-vis_len)
  end_fill()
  return vis_len
tracer(0)
speed(0)
penup() 
rad = 300 # Circle all total 
reset_position(0,-rad)
x,y = pos()
# draw squash
num_rows = 8 # Number of rows in the squash
len_row = 10 # height of a row in the squash
num_peaces = 35 # the number of peaces in which the circle want to be divided
colors = ["#536F3D","#5B0B16","#D6325C","#F06D0A",'#FACA27','#EDE9DE'] # the colors of the boxes in squash
occ_squash = draw_squash(rad,num_rows,len_row,num_peaces,colors) # Draw the squash, it will return how much radius of total radius it 
reset_position(0,y=y+occ_squash) # reset the position to the occupied position before
# a background for the next draw_circular
padding_circle = 2
fillcolor('#2A3B1A')
begin_fill()
circle(rad-occ_squash)
end_fill()
reset_position(y=y+occ_squash+padding_circle) # reset position to the next occupied position
# draw circular
circular_width = 40
cut_threshold = 1.3
new_rad = rad-occ_squash - padding_circle # the new radius for next shape
colors2 = ['#9B232E','#BB5C08','#DEC727','#CCCDB4']
occ_circular = draw_circular(new_rad,circular_width,colors=colors2,num_peaces=int(((new_rad)*math.pi*2)/(circular_width*cut_threshold)),sub_circle_count=4,pen_down=False) # draw circular shape 
reset_position(0,y+occ_squash+padding_circle+occ_circular+5)
fillcolor('#D5D1AD')
begin_fill()
circle(rad - occ_squash-padding_circle-occ_circular-5)
end_fill()

# continue ...

mainloop() # main loooooop