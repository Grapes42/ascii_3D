import math

from screen import Screen

Y = 0
X = 1

pi = 3.14159265359

def rotate(origin, object, rads):
    for point in object:
        x_o = origin[X]
        y_o = origin[Y]
        x_i = point[X]
        y_i = point[Y]

        x_from_origin = abs(x_i) - abs(x_o)
        y_from_origin = abs(y_i) - abs(y_o)

        radius = math.sqrt((x_from_origin)**2 + y_from_origin**2)

        if x_i > 0 and y_i > 0:
            angle_corrector = math.atan( (y_from_origin) / (x_from_origin) )

        elif y_i > 0 and x_i < 0:
            angle_corrector = math.atan( (x_from_origin) / (y_from_origin) ) + (.5 * pi)

        elif y_i < 0 and x_i < 0:
            angle_corrector = math.atan( (y_from_origin) / (x_from_origin) ) + (pi)

        elif y_i < 0 and x_i > 0:
            angle_corrector = math.atan( (x_from_origin) / (y_from_origin) ) + (1.5 * pi)

        x_f = radius * math.cos(rads+angle_corrector)
        y_f = radius * math.sin(rads+angle_corrector)

        screen.plot(y=y_f, x=x_f, char="F")


screen_height = 30
screen_width = 100

screen = Screen(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2), y_correction=.5)

origin = [0, 0]

screen.plot(y=origin[Y], x=origin[X], char="O")

length = 10

square = [[-2*length, -length], [-2*length, length], [2*length, -length], [2*length, length]]


for point in square:
    screen.plot(y=point[Y], x=point[X], char="I")



rotate(origin=origin, object=square, rads=.4)

screen.print(clear=False)