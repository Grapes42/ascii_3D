import time

from shapes import *
from projection import Projection
from data_types import *
from screen import Screen

screen_height = 100
screen_width = 300

def construct_objects(objects):
    for object in objects:
        screen.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs, char="#", step_size=.1)

screen = Screen(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=.5)

projection = Projection()


objects = []

cube = Object3D()
cube.array, cube.pairs = cube_by_center(x=0, y=0, z=10,
                                        height=1, width=1, depth=1)
objects.append(cube)
construct_objects(objects)
screen.print()

delay = .05
step = .2
loop = 10

while True:
    for i in range(loop):
        cube.rotate(origin=[0,0,10], rads=step, axis=Y)

        time.sleep(delay)

        construct_objects(objects)
        screen.print()
    for i in range(loop):
        cube.rotate(origin=[0,0,10], rads=step, axis=X)

        time.sleep(delay)

        construct_objects(objects)
        screen.print()
    for i in range(loop):
        cube.rotate(origin=[0,0,10], rads=step, axis=Z)

        time.sleep(delay)

        construct_objects(objects)
        screen.print()