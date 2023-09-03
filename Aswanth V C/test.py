from turtle import *
import math
def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def draw_eye(x,y,major,minor,fillclr=None,pen_down=True):
  penup()
  x_diff,y_diff = calculate_arc_dimensions(minor,90)
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
	
draw_ellipse(0,0,30,50,'red')
goto(0,0)
dot(3)
exitonclick()