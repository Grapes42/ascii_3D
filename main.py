import time

from shapes import *
from projection import Projection
from object_3D import *
from graphing import Graphing
from gui_interface import GUIInterface

Y = 0
X = 1
Z = 2

screen_height = 100
screen_width = 300

def construct_objects(objects):
    for object in objects:
        graphing.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs, step_size=.1)

graphing = Graphing(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=.7)

interface = GUIInterface(chars_height=screen_height, chars_width=screen_width,
                         pixel_height=1000, pixel_width=1000,
                         font_size=10, line_spacing=10,
                         fg_color=(182,242,216), bg_color=(19,30,25),
                         frame_rate=20)

projection = Projection()

#
# Creating 3D objects
#
objects = []

# Test cube
cube = Object3D()
cube.array, cube.pairs = cube_by_center(x=0, y=0, z=10,
                                        height=1, width=1, depth=1)
objects.append(cube)

#cube.rotate(origin=[0, 0, 10], rads=.4, axis=Z)
#cube.rotate(origin=[0, 0, 10], rads=.5, axis=X)

while True:
    construct_objects(objects)
    
    mouse_dir, mouse_button, keyboard_dir = interface.update(graphing.array)

    print(mouse_dir)

    if mouse_dir[X] != 0:
        cube.rotate(origin=[0, 0, 10], rads=.2*mouse_dir[X], axis=Y)

    if mouse_dir[Y] != 0:
        cube.rotate(origin=[0, 0, 10], rads=.2*mouse_dir[Y], axis=X)

    if keyboard_dir[X] != 0:
        cube.rotate(origin=[0, 0, 10], rads=.2*keyboard_dir[X], axis=Y)

    if keyboard_dir[Y] != 0:
        cube.rotate(origin=[0, 0, 10], rads=.2*keyboard_dir[Y], axis=X)

    graphing.clear()

            