from turtle import *
import math
def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def colored_star(x,y,size=40,fillclr=None,angle=120,pen_down=False):
	penup()
	chead = heading()
	goto(x,y)
	setheading(60)
	angle = 120
	forward(size)
	x_diff1,y_len1 = pos()
	backward(size)
	for _ in range(2):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	forward(size)
	right(angle)
	y_diff,y_len2 = pos()
	height = y_len2 - y_len1
	x_diff = x_diff1 - x
	goto(x+x_diff,y_len1+(height/2))
	x1,y1 = pos()
	x_diff = x - x1
	y_diff = y - y1
	goto(x+x_diff,y+y_diff)
	setheading(60)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(5):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	if fillclr is not None:
		end_fill()
	goto(x,y)
	setheading(chead)
def draw_ellipse(x,y,major,minor,fillclr=None,pen_down=True):
	penup()
	x_diff,y_diff = calculate_arc_dimensions(minor,90)
	y_center = y + (major / 2) - y_diff
	x_center = x + (x_diff /2)
	goto(x_center,y_center)#-major)
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
	# Draw a reference square, avoided on production
	draw_square(x,y,width,height,fill=True,clr="yellow")
	#some variable used to scale
	non_circle_len = height * 0.20
	len_square_bottom = height * 0.12
	len_half_circle = width * 0.5
	# goto the position to draw the big circle
	goto(x-width/2,y)
	left(90)
	forward(len_square_bottom+non_circle_len)
	fillcolor("#720B26")
	begin_fill()
	circle(-len_half_circle,180) # top circle
	end_fill()
	fillcolor('#D7140E')
	# Second half circle inside the first on the top
	half_circle_gap = width * 0.093
	penup()
	# got to the perticular position
	setheading(90)
	goto(x-width/2+half_circle_gap,y+(len_square_bottom+non_circle_len))
	begin_fill()
	# second top circle
	circle(-len_half_circle + half_circle_gap,180)
	end_fill()
	# draw the third half circle
	setheading(90)
	goto(x-width/2+half_circle_gap*2,y+(len_square_bottom+non_circle_len))
	fillcolor('#FF5C01')
	begin_fill()
	# third top circle
	circle(-len_half_circle + half_circle_gap*2,180)
	end_fill()
	# designs inside fist half circle
	goto(x-(width/2)+(half_circle_gap/2),y+(len_square_bottom+non_circle_len)) # design position
	setheading(90)
	num_dots = 32
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap/2),180/num_dots)
		dot(width*0.024,'#FF9002')
	#designs inside second half circle
	goto(x-width/2+half_circle_gap+(width * 0.015),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 64
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap+(width*0.015)),180/num_dots)
		dot(1.5,'#FFF')
	#second 
	goto(x-width/2+(half_circle_gap*2)-(width * 0.015),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 64
	for _ in range(num_dots - 1):
		circle(-len_half_circle + ((half_circle_gap*2)-(width*0.015)),180/num_dots)
		dot(1.5,'#FFF')
	goto(x-width/2+(half_circle_gap*1.5),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 11
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap*1.5),180/num_dots)
		cx,cy = pos()
		colored_star(cx,cy,size=width*0.01,fillclr="#FFF")
	center_no_circle_rad = width * 0.19 # the area in the circle which doesnt have any designs
	center_mul_circle_gap = width * (0.061 - 0.006) # last circle multiple doted circle gap
	for i  in range(3):
		goto(x-center_no_circle_rad-(center_mul_circle_gap*i),y+(len_square_bottom+non_circle_len))
		setheading(90)
		num_dots = 30 + (i * 10)
		for _ in range(num_dots - 1):
			circle(-(center_no_circle_rad+(center_mul_circle_gap*i)),180/num_dots)
			dot(width*0.012,'#FF9002')
	# return
	# Draw the square below the big half circle
	fillcolor("#720B26")
	begin_fill()
	draw_square(x,y+non_circle_len,width,len_square_bottom) # bottom_square
	end_fill()
	#  Some refernces, to scale the image
	bottom_len = width / 2 # width of the lower square, the square below the big square
	bottom_one_height = width * 0.1 # Height of the square
	# draw reference square, avoided in production
	#draw_square(x,y+(non_circle_len - bottom_one_height),bottom_len,bottom_one_height) # bottom square one
	# radius of the curve in the bottom square with the half width
	bottom_r2 = width * 0.17 / 2
	penup()
	# goto the position
	goto(x+(bottom_r2)-(bottom_len/2),y+(non_circle_len - bottom_one_height))
	setheading(0)
	goto(x - (bottom_len/2),y+(non_circle_len))
	right(90)
	pendown()
	# draw the shape with two circles on the two sides
	fillcolor('#F53F10')
	begin_fill()
	forward(bottom_one_height - bottom_r2)
	circle(bottom_r2,140)
	cur_head = heading() # store the current heading angle to use on future
	setheading(0)
	forward(width * 0.2)
	setheading(cur_head)
	right(100)
	circle(bottom_r2,140)
	forward(bottom_one_height-bottom_r2)
	end_fill()
	# Draw the shape at the bottom, which look like a thaadi
	r = bottom_len / 2#((width**0.1)**2+(width*0.175)**2)/(2*(width*0.1)) + 5
	bottom_band_height = width * 0.115 # height pf the band
	bottom_band_ang = 60 # arc in which the band want to be visible
	penup()
	setheading(0)
	goto(x,y)
	# draw the shape
	fillcolor('#7C0808')
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
	# draw the head of theyyam
	draw_ellipse(x,y+bottom_band_height,width* 0.25 / 2,width* 0.22 / 2,fillclr='#EB5928')
	return
	
tracer(0)
speed(0)
draw_theyyam(0,-300,600)
#draw_ellipse(100,300,100,60)
mainloop()