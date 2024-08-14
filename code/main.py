import time

# Local imports
from shapes import *
from projection import Projection
from object_3D import *
from graphing import Graphing
from interface import Interface

Y = 0
X = 1
Z = 2

screen_height = 100
screen_width = 300

def construct_objects(objects):
    for object in objects:
        graphing.construct_pairs(points=projection.map_to_2d(object.array),
                               pairs=object.pairs, step_size=.1)

# Defining the object for graphing
graphing = Graphing(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=.7)

# Defining the object for the interface
interface = Interface(chars_height=screen_height, chars_width=screen_width,
                pixel_height=1000, pixel_width=1000,
                font_size=10, line_spacing=10,
                fg_color=(182,242,216), bg_color=(19,30,25),
                frame_rate=20)

# Defining the object for projection
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

sens = .1

move_dir = [0, 0]

#
# Main loop
#
while True:
    construct_objects(objects)
    
    mouse_dir, mouse_button, key_down_dir, key_up_dir = interface.update(graphing.array)

    

    # Rotates cube based on mouse direction
    if mouse_dir[X] != 0:
        cube.rotate(origin=[0, 0, 10], rads=sens*mouse_dir[X], axis=Y)

    if mouse_dir[Y] != 0:
        cube.rotate(origin=[0, 0, 10], rads=sens*mouse_dir[Y], axis=X)



    #
    # Keyboard checks
    #

    # Checks if key is down, sets direction accordingly
    if key_down_dir[X] != 0:
        move_dir[X] += key_down_dir[X]

    if key_down_dir[Y] != 0:
        move_dir[Y] += key_down_dir[Y]


    # Checks if key is up, stops direction
    if key_up_dir[X] != 0:
        move_dir[X] -= key_up_dir[X]

    if key_up_dir[Y] != 0:
        move_dir[Y] -= key_up_dir[Y]


    # Rotates cube based on direction
    if move_dir[X] != 0:
        cube.rotate(origin=[0, 0, 10], rads=sens*move_dir[X], axis=Y)

    if move_dir[Y] != 0:
        cube.rotate(origin=[0, 0, 10], rads=sens*move_dir[Y], axis=X)

    # Resets the 2D graph
    graphing.clear()

            