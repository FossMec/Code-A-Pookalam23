import turtle

s = turtle.Turtle()



def drawCircle(color,colorfill, radius):
    s.color(color, colorfill)
    s.begin_fill()
    for i in range(12):
        s.circle(radius)
        s.left(30)
    s.end_fill()

def drawCircle2(color,colorfill, radius):
    s.color(color, colorfill)
    s.begin_fill()
    for i in range(12,0,-2):
        s.circle(radius)
        s.left(60)
    s.end_fill()

def drawtriangle(color,colorfill, length):
 
    s.color(color, colorfill)
    s.begin_fill()
    for i in range(8):
        s.left(15)
        s.forward(240)
        s.left(90)
        s.circle(240, 30)
        s.left(90)
        s.forward(240)
    s.end_fill()


def square(radius,colour):
    s.color('purple', 'purple')
    
    s.begin_fill()
    for i in range(30):
       

        if(i%4==0):
            s.color(colour, colour)
            s.begin_fill()
        else:
            s.color(colour, colour)
            s.begin_fill()
      
        s.left(12)
        s.forward(radius)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.forward(radius)
        s.left(90)
        s.end_fill()

s.speed(800)



square(270,'#e9d8a6')
square(250,'#ae2012')


drawCircle2('#005f73','#005f73', 160)


drawCircle2('#ee9b00','#ee9b00', 150)
square(152,'#e9d8a6')

drawCircle2('#005f73','#005f73',120)




square(90,'#005f73')

square(60,'#ee9b00')


drawCircle2('#005f73','#005f73', 25)

drawCircle2('#ee9b00','#ee9b00', 15)

square(5,'#005f73')
turtle.Screen().exitonclick()
