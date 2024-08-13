from shapes import *
from projection import Projection
from data_types import *
from screen import Screen

import time

screen_height = 150
screen_width = 600

def construct_objects(objects):
    for object in objects:
        screen.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs)

screen = Screen(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=.75)

projection = Projection()


objects = []

cube = Object3D()
cube.array, cube.pairs = cube_by_center(x=-1.5, y=-.4, z=7,
                                        height=-.5, width=1, depth=2)
objects.append(cube)
construct_objects(objects)
screen.print()

def move_over_period(object, axis, period, amount, steps):
    
    step_size = amount/steps
    delay = period/steps

    for i in range(steps):
        object.move(axis=axis, amount=step_size)
        time.sleep(delay)
        construct_objects(objects)
        screen.print()
    

period = .5

x_amount = 3
y_amount = .8
z_amount = 4

while True:
    move_over_period(object=cube, axis="x", period=period, amount=x_amount, steps=5)
    move_over_period(object=cube, axis="z", period=period, amount=z_amount, steps=5)
    move_over_period(object=cube, axis="y", period=period, amount=y_amount, steps=5)

    move_over_period(object=cube, axis="x", period=period, amount=-x_amount, steps=5)
    move_over_period(object=cube, axis="z", period=period, amount=-z_amount, steps=5)
    move_over_period(object=cube, axis="y", period=period, amount=-y_amount, steps=5)