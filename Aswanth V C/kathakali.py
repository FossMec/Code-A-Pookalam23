from turtle import *
import math
def draw_ellipse(x,y,major,minor,fillclr=None,pen_down=True):
	penup()
	goto(x+major/2 - 5,y+minor/2)#-major)
	setheading(45)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(2):
		circle(major,90)
		circle(minor,90)
	if fillclr is not None:end_fill()
def draw_square(x,y,width,height,angle=0,clr="black",fill=False,border=1,border_clr="black"):
	penup()
	goto(x,y)
	if border > 0:pendown()
	setheading(angle)
	color(border_clr)
	pensize(border)
	if fill:
		fillcolor(clr)
		begin_fill()
	forward(width/2)
	left(90)
	forward(height)
	left(90)
	forward(width)
	left(90)
	forward(height)
	left(90)
	forward(width/2)
	if fill:end_fill()

def draw_theyyam(x,y,width):
	height = width * 0.67
	draw_square(x,y,width,height,fill=True,clr="yellow")
	non_circle_len = height * 0.18
	len_square_bottom = height * 0.12
	len_half_circle = width * 0.5
	goto(x-width/2,y)
	left(90)
	forward(len_square_bottom+non_circle_len)
	fillcolor("red")
	begin_fill()
	circle(-len_half_circle,180) # top circle
	end_fill()
	fillcolor('pink')
	# Second half circle inside the first on the top
	second_half_circle_gap = 50
	penup()
	setheading(0)
	goto(x-width/2,y)
	left(90)
	forward(len_square_bottom+non_circle_len)
	right(90)
	forward(second_half_circle_gap)
	left(90)
	begin_fill()
	# second top circle
	circle(-len_half_circle + second_half_circle_gap,180)
	end_fill()
	fillcolor("brown")
	begin_fill()
	draw_square(x,y+non_circle_len,width,len_square_bottom) # bottom_square
	end_fill()
	bottom_len = width / 2
	bottom_one_height = width * 0.1
	#draw_square(x,y+(non_circle_len - bottom_one_height),bottom_len,bottom_one_height) # bottom square one
	bottom_r2 = width * 0.17 / 2
	penup()
	goto(x+(bottom_r2)-(bottom_len/2),y+(non_circle_len - bottom_one_height))
	setheading(0)
	goto(x - (bottom_len/2),y+(non_circle_len))
	right(90)
	pendown()
	fillcolor('orange')
	begin_fill()
	forward(bottom_one_height - bottom_r2)
	circle(bottom_r2,140)
	cur_head = heading()
	setheading(0)
	forward(width * 0.2)
	setheading(cur_head)
	right(100)
	circle(bottom_r2,140)
	forward(bottom_one_height-bottom_r2)
	end_fill()
	
	r = bottom_len / 2#((width**0.1)**2+(width*0.175)**2)/(2*(width*0.1)) + 5
	bottom_band_height = 30
	bottom_band_ang = 60
	penup()
	setheading(0)
	goto(x,y)
	fillcolor('green')
	right(180)
	circle(-r,bottom_band_ang/2)
	begin_fill()
	right(180)
	circle(r,bottom_band_ang)
	cur_head = heading()
	setheading(90)
	forward(bottom_band_height)
	setheading(cur_head+180)
	circle(-r,bottom_band_ang)
	setheading(270)
	forward(bottom_band_height)
	end_fill()
	draw_ellipse(x,y+non_circle_len - len_square_bottom,width/7,width/9,fillclr='red')
	return
	#setheading(0)
	#goto(x,)
	#penup()
	setheading(0)
	goto(x,y+30)
	pendown()
	draw_arc(r,80)
	end_fill()
	cur_head = heading()
	goto(pos()[0],pos()[1]-10)
	left(60)
	forward(10)
	left(60)
	forward(10)
	

speed(0)
draw_theyyam(0,0,600)
#draw_ellipse(100,300,100,60)
mainloop()