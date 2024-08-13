import time

from shapes import *
from projection import Projection
from data_types import *
from screen import Screen

screen_height = 200
screen_width = 300

def construct_objects(objects):
    for object in objects:
        screen.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs)

screen = Screen(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=.5)

projection = Projection()


objects = []

cube = Object3D()
cube.array, cube.pairs = cube_by_center(x=0, y=1.5, z=10,
                                        height=1, width=1, depth=1)
objects.append(cube)
construct_objects(objects)
screen.print()


while True:
    cube.rotate(origin=[10,0], rads=.2)

    time.sleep(.1)

    construct_objects(objects)
    screen.print()