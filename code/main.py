import time
import sys

# Local imports
from shapes import *
from projection import Projection
from object_3D import *
from graphing import Graphing
from interface import Interface

Y = 0
X = 1
Z = 2

pi = 3.14159265359

screen_height = 100
screen_width = 300

fps = 60
time_per_frame = 1/60


def construct_world():
    for object in world:
        points, pairs = projection.map_to_2d(object.array, object.pairs)
        graphing.construct_pairs(points=points, pairs=pairs, step_size=1, char=object.char)
        
def move_world(axis, amount):
    for object in world:
        object.move(axis=axis, amount=amount)
    
def rotate_world(axis, amount):
    for object in world:
        object.rotate(origin=[0, 0, 0], rads=amount, axis=axis)

fg_color = [182,242,216]
bg_color=[19,30,25]

for i in range(len(sys.argv)):
    if sys.argv[i] == "-fg":
        parts = sys.argv[i+1].split(",")

        fg_color = [int(parts[0]),int(parts[1]),int(parts[2])]

    elif sys.argv[i] == "-bg":
        parts = sys.argv[i+1].split(",")

        bg_color = [int(parts[0]),int(parts[1]),int(parts[2])]

# Defining the object for graphing
graphing = Graphing(height=screen_height, width=screen_width, 
                origin_y=round(screen_height/2), origin_x=round(screen_width/2),
                y_correction=.7)

# Defining the object for the interface
interface = Interface(chars_height=screen_height, chars_width=screen_width,
                pixel_height=1000, pixel_width=1000,
                font_size=10, line_spacing=10,
                fg_color=fg_color, bg_color=bg_color)

fov = 100
# Defining the object for projection
projection = Projection(fy=fov, fx=fov, height=screen_height, width=screen_width)

#
# Creating 3D objects
#
world = []

# Test shapes
cube = Object3D(char="F")
cube.array, cube.pairs = cube_by_center(x=0, y=0, z=5,
                                        height=1, width=1, depth=1)
world.append(cube)

#cube.rotate(origin=[0, 0, 10], rads=.4, axis=Z)
#cube.rotate(origin=[0, 0, 10], rads=.5, axis=X)



#
# Main loop
#
sens = .05
move_speed = .1

move_dir = [0, 0]
while True:
    construct_world()
    
    move_dir, turn_dir = interface.update(graphing.array)

    if move_dir[X] != 0:
        move_world(axis=X, amount=move_dir[X]*move_speed)

    if move_dir[Y] != 0:
        move_world(axis=Z, amount=move_dir[Y]*move_speed)


    if turn_dir[X] != 0:
        rotate_world(axis=Y, amount=turn_dir[X]*sens)

    if turn_dir[Y] != 0:
        rotate_world(axis=X, amount=turn_dir[Y]*sens)

    time.sleep(time_per_frame)

    # Resets the 2D graph
    graphing.clear()

            