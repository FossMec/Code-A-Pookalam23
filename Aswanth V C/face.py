from turtle import *
import math
def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def find_triangle_height_and_base(a, theta_degrees):
    theta_radians = math.radians(theta_degrees)
    h = a * math.sin(theta_radians)
    b = 2 * math.sqrt(a**2 - h**2)
    return h, b
def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def calculate_arc_radius_and_angle(width, height):
    half_width = width / 2
    radius = math.sqrt(half_width**2 + height**2)
    angle_rad = 2 * math.atan(half_width / height)
    angle_deg = math.degrees(angle_rad)
    return radius, angle_deg
def draw_pentagon(x, y, side_length,pen_down=False,fillclr=None):
		penup()
		angle = 360 / 6
		h,a = find_triangle_height_and_base(side_length,angle)
		goto(x-side_length/2, y-a)
		if pen_down:pendown()
		
		if fillclr is not None:
				fillcolor(fillclr)
				begin_fill()
		for _ in range(5):
			forward(side_length)
			left(angle)
		if fillclr is not None:end_fill()
def draw_eye(x,y,major,minor,fillclr=None,pen_down=True):
	goto(x,y)
	penup()
	x_diff,_ = calculate_arc_dimensions(minor,90)
	penup()
	left(45)
	forward(major*0.02)
	y_center = pos()[1]
	x_center = x + (x_diff /2)
	goto(x_center,y_center)#-major)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(2):
		# circle(major,90)
		chead = heading()
		forward(major*0.02)
		left(60)
		forward(major*0.02)
		setheading(chead+90)
		circle(minor,90)
	if fillclr is not None:end_fill()
def draw_theyyam_face(x,y,height):
	ellipse_height = height * 0.594
	ellipse_width = height * 0.451
	eye_pos = height * 0.22
	mouth_pos = height * 0.10
	head_design_pos = height * 0.309
	top_band_pos = height * 0.516
	top_band_height = height * 0.098
	top_band_radius = height * 0.32
	top_band_angle = 95
	penup()
	# kireedam (crown)
	crown_height = height * 0.5
	crown_bottom_width = height * 0.94
	crown_top_circle_gap = height * 0.05
	crown_top_circle_penta_gap = height * 0.1
	goto(x - (crown_bottom_width/2),y+crown_height)
	setheading(90)
	fillcolor('#A01005')
	begin_fill()
	circle(-crown_bottom_width/2,180)
	end_fill()
	# dots
	goto(x - ((crown_bottom_width/2)-(crown_top_circle_gap)),y+crown_height)
	setheading(90)
	num_peaces = 40
	for _ in range(num_peaces):
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap)),180/num_peaces/2)
		dot(height*0.02,'#fff')
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap)),180/num_peaces/2)
	# hexagons
	goto(x - ((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),y+crown_height)
	setheading(90)
	num_peaces = 4
	for _ in range(num_peaces):
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),180/num_peaces/2)
		chead = heading()
		setheading(0)
		cx,cy = pos()
		draw_pentagon(cx,cy,height*0.082,fillclr='#FC8505')
		setheading(chead)
		goto(cx,cy)
		setheading(0)
		draw_pentagon(cx,cy,height*0.053,fillclr='#FEA901')
		setheading(chead)
		goto(cx,cy)
		setheading(0)
		draw_pentagon(cx,cy,height*0.037,fillclr='#D51510')
		setheading(chead)
		goto(cx,cy)
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),180/num_peaces/2)
	setheading(0)
	# Draw the face
	face_bottom_circle_ang = 152
	goto(x,y)
	circle(height*0.2196,-face_bottom_circle_ang/2)
	chead = heading()
	tmp_x1,tmp_y1 = pos()
	chead = heading()
	setheading(90)
	forward(top_band_pos - height * 0.16)
	setheading(270)
	fillcolor('#EB5928')
	begin_fill()
	forward(top_band_pos- height * 0.16)
	setheading(chead)
	circle(height*0.2196,face_bottom_circle_ang)
	setheading(90)
	forward(top_band_pos - height * 0.16)
	end_fill()
	#decoration1
	goto(tmp_x1+height*0.02,tmp_y1+height*0.02)
	setheading(chead)
	num_peaces = 50
	for _ in range(num_peaces-1):
		circle(height*0.2196 - height * 0.02,face_bottom_circle_ang/num_peaces)
		dot(height * 0.005,'#fff')
	# draw the band above face
	goto(x,y+top_band_pos)
	setheading(0)
	pendown()
	circle(-top_band_radius,-top_band_angle/2)
	dec_tmp_x1,dec_tmp_y1 = pos()
	dec_tmp_head1 = heading()
	fillcolor('#7F080C')
	begin_fill()
	circle(-top_band_radius,top_band_angle)
	band_tmp_ang = heading()
	band_circle_pos_x,band_circle_pos_y = pos()
	setheading(90)
	forward(top_band_height)
	setheading(band_tmp_ang+180)
	circle(top_band_radius,top_band_angle)
	setheading(270)
	forward(top_band_height)
	band_circle_pos_x1,band_circle_pos_y1 = pos()
	end_fill()
	band_side_circle_rad = height*0.085
	penup()
	#decorations
	# outside
	goto(dec_tmp_x1,dec_tmp_y1- height * 0.02)
	setheading(dec_tmp_head1)
	num_dots = 50
	for _ in range(num_dots):
		dot(height*0.005,'#FFf')
		circle(-top_band_radius,top_band_angle/num_dots)
	# inside
	for i in range(1,3):
		goto(dec_tmp_x1,dec_tmp_y1 + ((top_band_height/3)*i))
		setheading(dec_tmp_head1)
		num_dots = 20
		for _ in range(num_dots):
			dot(height*0.02,'#FF9002')
			circle(-top_band_radius,top_band_angle/num_dots)
	
	# draw the side circle in the band
	goto(band_circle_pos_x1,band_circle_pos_y1+(band_side_circle_rad - top_band_height))
	setheading(0)
	fillcolor('#6E1109')
	begin_fill()
	circle(band_side_circle_rad)
	end_fill()
	# decoirations
	setheading(90)
	forward(height*0.054)
	setheading(0)
	fillcolor('#EB5928')
	begin_fill()
	circle(band_side_circle_rad - height*0.054)
	end_fill()
	setheading(270)
	# decorations
	forward(height * 0.027)
	setheading(0)
	num_dots = 13
	for _ in range(num_dots):
		circle((band_side_circle_rad - height * 0.027),360/num_dots)
		dot(height*0.02,'#FF9002')

	goto(band_circle_pos_x,band_circle_pos_y+(band_side_circle_rad - top_band_height))
	setheading(0)
	fillcolor('#6E1109')
	begin_fill()
	circle(band_side_circle_rad)
	end_fill()
	setheading(90)
	forward(height*0.054)
	setheading(0)
	fillcolor('#EB5928')
	begin_fill()
	circle(band_side_circle_rad - height*0.054)
	end_fill()
	setheading(270)
	forward(height * 0.027)
	setheading(0)
	num_dots = 13
	for _ in range(num_dots):
		circle((band_side_circle_rad - height * 0.027),360/num_dots)
		dot(height*0.024,'#FF9002')
	
	# lips
	goto(x,y+mouth_pos)
	setheading(0)
	lip_bottom_rad = height * 0.087
	lip_bottom_ang = 93
	fillcolor('#A60F06')
	circle(lip_bottom_rad,-lip_bottom_ang/2)
	begin_fill()
	circle(lip_bottom_rad,lip_bottom_ang)
	end_fill()
	
	# eyes
	eye_gap = height * 0.121
	eye_bottom_rad = 	height * 0.101
	eye_bottom_angle = 114
	eye_eye_gap = height * 0.046
	eye_right_cir_rad = height * 0.075
	eye_right_cir_ang = 106
	goto(x-eye_gap,y+eye_pos)
	setheading(0)
	circle(eye_bottom_rad,-eye_bottom_angle/2)
	chead = heading()
	left(80)
	circle(eye_right_cir_rad,eye_right_cir_ang)
	fillcolor('#382030')
	begin_fill()
	left(180)
	circle(-eye_right_cir_rad,eye_right_cir_ang)
	setheading(chead)
	tmp_x1,tmp_y1 = pos()
	tmp_head = heading()
	circle(eye_bottom_rad,eye_bottom_angle)
	left(110)
	eye_left_cir_rad = height * 0.1793
	eye_left_cir_ang = 42
	circle(-eye_left_cir_rad,eye_left_cir_ang)
	end_fill()
	setheading(0)
	draw_eye(x-eye_gap,tmp_y1,height*0.03,height*0.06,fillclr='#fff',pen_down=False)
	goto(x-eye_gap,tmp_y1-height*0.015)
	setheading(0)
	fillcolor('#5A3137')
	begin_fill()
	circle(height*0.015)
	end_fill()
	goto(x-eye_gap,tmp_y1-height*0.005)
	setheading(0)
	fillcolor('#EEE5E6')
	begin_fill()
	circle(height*0.005)
	end_fill()
	#decorations left eye
	setheading(tmp_head)
	goto(tmp_x1,tmp_y1-height * 0.02)
	num_peaces = 10
	for _ in range(num_peaces):
		circle(eye_bottom_rad,eye_bottom_angle/num_peaces)
		dot(height * 0.009,'#fff')
	# eye right
	goto(x+eye_gap,y+eye_pos)
	setheading(0)
	circle(eye_bottom_rad,eye_bottom_angle/2)
	chead = heading()
	left(100)
	circle(-eye_right_cir_rad,eye_right_cir_ang)
	color('pink')
	fillcolor('#382030')
	begin_fill()
	left(180)
	circle(eye_right_cir_rad,eye_right_cir_ang)
	setheading(chead)
	tmp_x1,tmp_y1 = pos()
	tmp_head = heading()
	circle(eye_bottom_rad,-eye_bottom_angle)
	left(70)
	eye_left_cir_rad = height * 0.1793
	eye_left_cir_ang = 42
	circle(eye_left_cir_rad,eye_left_cir_ang)
	end_fill()
	setheading(0)
	draw_eye(x+eye_gap,tmp_y1,height*0.03,height*0.06,fillclr='#fff',pen_down=False)
	goto(x+eye_gap,tmp_y1-height*0.015)
	setheading(0)
	fillcolor('#5A3137')
	begin_fill()
	circle(height*0.015)
	end_fill()
	goto(x+eye_gap,tmp_y1-height*0.005)
	setheading(0)
	fillcolor('#EEE5E6')
	begin_fill()
	circle(height*0.005)
	end_fill()
	#decorations right eye
	setheading(tmp_head)
	goto(tmp_x1,tmp_y1-height * 0.02)
	num_peaces = 10
	for _ in range(num_peaces):
		circle(eye_bottom_rad,-eye_bottom_angle/num_peaces)
		dot(height * 0.009,'#fff')
	nose_gap = height * 0.184
	goto(x,y+nose_gap)
	setheading(90)
	pensize(height*0.02)
	pendown()
	color('#9E1205')
	forward(height* 0.081)
	penup()
	angle_top_circles = 95
	top_circles_mul_gap = height * 0.025
	top_circles_gap = height * 0.364
	goto(x,y+top_circles_gap)
	fillcolor('#9E1205')
	setheading(0)
	circle(-height * 0.1,-angle_top_circles/2)
	begin_fill()
	chead1 = heading()
	circle(-height * 0.1,angle_top_circles)
	chead = heading()
	left(90)
	forward(height*0.01)
	setheading(chead+180)
	circle(height * 0.1+height*0.01,angle_top_circles)
	end_fill()

	setheading(chead1)
	left(90)
	forward(height*0.067)
	right(90)
	begin_fill()
	circle(-(height * 0.1 + height*0.067),angle_top_circles)
	chead = heading()
	left(90)
	forward(height*0.01)
	setheading(chead+180)
	circle(height * 0.1 + height*0.067 + height * 0.01,angle_top_circles)
	end_fill()
	
	# top dot dot



	

tracer(0)
# speed(0)
draw_theyyam_face(0,-300,600)
exitonclick()