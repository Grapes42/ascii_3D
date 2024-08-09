from shapes import *
from projection import Projection
from data_types import *
from screen import Screen

import time

screen_height = 100
screen_width = 400

def construct_objects(objects):
    for object in objects:
        screen.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs)

screen = Screen(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2))

projection = Projection()


objects = []

cube = Object3D()
cube.array, cube.pairs = cube_by_center(x=0, y=0, z=8,
                                        height=.5, width=1, depth=2)
objects.append(cube)

delay = .2
amount = .2
loop_count = 10

cube.move(axis="x", amount=-amount*(loop_count/2))

while True:
    for i in range(loop_count):
        construct_objects(objects)
        screen.print(clear=True)

        cube.move(axis="x", amount=amount)    

        time.sleep(delay)

    for i in range(loop_count):
        construct_objects(objects)
        screen.print(clear=True)

        cube.move(axis="x", amount=-amount)    

        time.sleep(delay)