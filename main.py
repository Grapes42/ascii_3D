from shapes import *
from projection import Projection
from data_types import *
from screen import Screen

screen_height = 150
screen_width = 300

def construct_objects(objects):
    for object in objects:
        screen.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs)

screen = Screen(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2))

projection = Projection()


objects = []

cube = Object3D()
cube.array, cube.pairs = cube_by_center(y=0, x=0, z=10,
                                        width=2, height=1, depth=2)

objects.append(cube)

construct_objects(objects)

screen.print(clear=False)